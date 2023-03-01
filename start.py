from model.view import show_window
import logging

if __name__ == '__main__':
    try:
        show_window()
    except Exception as ex:
        logging.error(ex)
