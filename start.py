from core.log_utils import get_log
from model.view import show_window

if __name__ == '__main__':
    try:
        show_window()
    except Exception as ex:
        log = get_log()
        log.error(ex)
