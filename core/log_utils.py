import logging

from datetime import datetime

log_file = 'log/sys_%s.log' % datetime.strftime(datetime.now(), '%Y-%m-%d')
log_level = logging.WARNING
log_format = '%(asctime)s[%(levelname)s]: %(message)s'
logging.basicConfig(filename=log_file, level=logging.WARNING, format=log_format)


def get_log():
    return logging.getLogger()
