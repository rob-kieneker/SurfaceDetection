import logging
import sys


def setup_logging(level=logging.INFO):
    """
    General logging set up
    """
    root = logging.getLogger()
    root.setLevel(level)

    # Console handler
    c_handler = logging.StreamHandler(sys.stdout)
    c_handler.setLevel(logging.WARNING)

    c_format = logging.Formatter(
        "%(name)s - %(levelname)s - %(message)s"
    )
    c_handler.setFormatter(c_format)

    # File handler
    f_handler = logging.FileHandler("file.log")
    f_handler.setLevel(logging.ERROR)

    f_format = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    f_handler.setFormatter(f_format)

    root.addHandler(c_handler)
    root.addHandler(f_handler)


def get_logger(name: str) -> logging.Logger:
    """
    Assign and return default logger
    :param name: Logging name, generally passed through __name__
    :return:
    """
    return logging.getLogger(name)
