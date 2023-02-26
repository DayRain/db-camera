import os

import pymysql


class DbUtils:
    def __init__(self, host, user, password, charset):
        self.host = host
        self.user = user
        self.password = password
        self.charset = charset

    def get_connection(self):
        con = pymysql.connect(host=self.host, user=self.user, password=self.password,
                              charset=self.charset, connect_timeout=3)
        return con

    def get_dbs(self):
        db_list = []
        try:
            con = self.get_connection()
            executor = con.cursor()
            executor.execute('show databases;')
            res = executor.fetchall()
            con.commit()
            except_list = ['information_schema', 'performance_schema', 'mysql']
            for db in res:
                if db[0] in except_list:
                    continue
                db_list.append(db[0])
            con.close()
        except Exception as err:
            return db_list
        return db_list

    def get_tables(self, db_name):
        con = self.get_connection()
        executor = con.cursor()
        executor.execute('use ' + db_name + ';')
        executor.execute('show full tables;')
        tables = executor.fetchall()
        con.commit()
        con.close()

        return tables

    def get_data_sql(self, table, tup):
        if len(tup) == 0:
            return None
        sql_sum = ''
        for columns in tup:
            sql = 'INSERT INTO ' + table + ' VALUES('
            for item in columns:

                if type(item) is (int or float):
                    sql = sql + ' ' + str(item) + ','
                else:
                    sql = sql + " '" + str(item) + "',"
            sql = sql[:-1] + ' )'
            sql_sum = sql_sum + sql + ';\n'

        return sql_sum

    def print_tables(self, db):
        if not self.exist(db):
            return None
        con = self.get_connection()

        tables = self.get_tables(db)
        executor = con.cursor()
        executor.execute('use ' + db + ';')
        res_str = ''
        for table in tables:
            executor.execute('show create table ' + table[0] + ';')
            for state in executor.fetchall():
                create = state[1] + ';' + '\n'

                kind = "TABLE"
                if table[1] == 'VIEW':
                    kind = 'VIEW'
                drop = 'DROP ' + kind + ' IF EXISTS `' + table[0] + '`;\n'

                executor.execute('select * from ' + table[0])
                data_sql = self.get_data_sql(table[0], executor.fetchall())

                res_str = res_str + drop + create
                if data_sql is not None:
                    res_str = res_str + data_sql

                res_str = res_str + '\n'
        con.commit()
        con.close()

        return res_str

    def exist(self, db):
        con = self.get_connection()
        executor = con.cursor()
        executor.execute("select * from information_schema.SCHEMATA where SCHEMA_NAME = '{0}'".format(db))
        result = len(executor.fetchall()) > 0
        con.commit()
        con.close()
        return result

    def execute(self, db, sql):
        con = self.get_connection()
        executor = con.cursor()
        executor.execute('use ' + db + ';')
        for s in sql.split(';\n'):
            if s.isspace() or s.startswith('#') or s.startswith('\n#'):
                continue
            executor.execute(s)
        con.commit()

    def save_sql(self, sql, name):
        if os.path.exists(name):
            return None
        if not os.path.exists('sql'):
            os.makedirs('sql')
        with open(name, 'w', encoding='utf-8') as fp:
            fp.write(sql)

    def delete_sql(self, name):
        if not os.path.exists(name):
            return None
        os.remove(name)

    def read_sql(self, name):
        if not os.path.exists(name):
            return None
        with open(name, 'r', encoding='utf-8') as fp:
            return ''.join(fp.readlines())

    def connection_test(self):
        try:
            conn = self.get_connection()
            conn.close()
            return True
        except Exception as err:
            print(err)
            return False


def connection_test(ip, user, password):
    try:
        conn = pymysql.connect(host=ip, user=user, password=password,
                               charset='utf8mb4', connect_timeout=3)
        conn.close()
        return True
    except Exception as err:
        print(err)
        return False

# if __name__ == '__main__':
#     dbs = get_dbs()
#     tb_str = print_tables(dbs[4])
#     save_sql(tb_str, 'abc.sql')
#     tb_str = read_sql('abc.sql')
#
#     execute(dbs[4], tb_str)
