import json
import os
from datetime import time, datetime
from connect.db_utils import DbUtils
import core.local_constants as cons
from core.local_utils import time_to_str, str_to_time, datetime_parser

config_path = 'config/conf.json'
sql_folder = 'sql/'


def json_default(value):
    if isinstance(value, datetime):
        return value.strftime('%Y-%m-%d %H:%M:%S')
    else:
        return value.__dict__


class SqlItem:
    def __init__(self, id: int, db_name, show_name, file_name, create_time: datetime, remark):
        self.id = id
        self.db_name = db_name
        self.show_name = show_name
        self.file_name = file_name
        self.create_time = create_time
        self.remark = remark

    def __eq__(self, other):
        return self.id == other.id and self.db_name == other.db_name

    def __repr__(self) -> str:
        return json.dumps(self, ensure_ascii=False, default=lambda o: o.__dict__, indent=4)


class DbConfig:
    def __init__(self, version, ip, username, password, cursor, charset, items, recent_dbs: list):
        self.version = version
        self.username = username
        self.ip = ip
        self.password = password
        self.cursor = cursor
        self.charset = charset
        self.items = []
        self.recent_dbs = recent_dbs
        for item in items:
            self.items.append(SqlItem(**item))

    def add_recent_dbs(self, db):
        self.recent_dbs.insert(0, db)
        if len(self.recent_dbs) > 10:
            self.recent_dbs.pop()

    def get_appear_count(self, db):
        count = 0
        for item in self.recent_dbs:
            if item == db:
                count = count + 1
        return count

    def __repr__(self) -> str:
        return json.dumps(self, ensure_ascii=False, default=lambda o: o.__dict__, indent=4)


def get_filename(id: int, db_name: str, show_name: str, create_time: datetime, remark: str):
    return str(id).zfill(
        6) + db_name + '_' + show_name + '.sql'


class DbContainer:
    def __init__(self):
        self.refresh()

    def refresh(self):
        self.db_config = self.load_config()
        self.db_utils = DbUtils(self.db_config.ip, self.db_config.username, self.db_config.password,
                                self.db_config.charset)
        self.sort_item()

    def add_item(self, db_name, show_name, remark, sql=None):
        if sql is None:
            sql = self.db_utils.print_tables(db_name)
        if sql is None:
            return
        # add cursor
        self.db_config.cursor = self.db_config.cursor + 1
        # file name
        now_time = datetime.now()
        file_name = get_filename(self.db_config.cursor, db_name, show_name, now_time, remark)
        # add item
        item = SqlItem(self.db_config.cursor, db_name, show_name, file_name, now_time, remark)
        self.db_config.items.append(item)
        self.db_config.add_recent_dbs(db_name)
        # save sql
        self.save_file(sql, item)
        # save config
        self.save_config()
        self.sort_item()

    def import_item(self, sql):
        lines = sql.split(';\n')
        db_name = lines[0][1:]
        show_name = lines[1][1:]
        remark = lines[2][1:]

        result = ";\n".join(lines[3:])
        self.add_item(db_name, show_name, remark, result)

    def do_item(self, item_id):
        sql = self.load_file(item_id)
        if sql is None:
            return None

        item = self.read_item(item_id)
        # execute sql
        self.db_utils.execute(item.db_name, sql)
        return True

    def delete_item(self, item_id):
        item = self.read_item(item_id)
        if item is None:
            return None
        self.db_config.items.remove(item)
        # delete sql
        self.db_utils.delete_sql(self.get_sql_path(item.file_name))
        # save config
        self.save_config()
        self.refresh()
        return True

    def read_item(self, item_id):
        for sql_item in self.db_config.items:
            if sql_item.id == item_id:
                return sql_item
        return None

    def sort_item(self):
        self.db_config.items = sorted(self.db_config.items, key=lambda item: item.id, reverse=True)

    def load_config(self):
        with open(config_path, mode='r', encoding='utf-8') as fp:
            config = json.load(fp=fp, object_hook=datetime_parser)
            return DbConfig(**config)

    def save_config(self):
        config_str = json.dumps(self.db_config, ensure_ascii=False, default=json_default, indent=4)
        with open(config_path, mode='w', encoding='utf') as fp:
            fp.write(config_str)
        self.db_utils = DbUtils(self.db_config.ip, self.db_config.username, self.db_config.password,
                                self.db_config.charset)

    def load_file(self, item_id):
        item = self.read_item(item_id)
        return self.db_utils.read_sql(self.get_sql_path(item.file_name))

    def save_file(self, sql, item: SqlItem):
        header = ''
        header += "#" + str(item.db_name) + ';\n'
        header += "#" + str(item.show_name) + ';\n'
        header += "#" + str(item.remark) + ';\n'
        return self.db_utils.save_sql(header + sql, self.get_sql_path(item.file_name))

    def get_sql_path(self, file_name):
        return os.path.join(sql_folder, file_name)

    def test_connection(self):
        return self.db_utils.connection_test()

    def get_dbs(self):
        dbs = self.db_utils.get_dbs()
        dbs.sort(key=self.db_config.get_appear_count, reverse=True)
        return dbs
