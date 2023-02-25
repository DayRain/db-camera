import json
from datetime import datetime, date
from core.local_constants import standard_date_format


def time_to_str(date_time: datetime, format):
    return date_time.strftime(format)
    pass


def str_to_time(date_str: str, format):
    return datetime.strptime(date_str, format)


def datetime_parser(dct):
    for k, v in dct.items():
        if validate(v):
            try:
                dct[k] = str_to_time(v, standard_date_format)
            except:
                pass
    return dct


def validate(date_text):
    try:
        datetime.fromisoformat(str(date_text))
        return True
    except ValueError:
        return False
