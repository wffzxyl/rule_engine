# coding: utf-8

import logging
import os
from .config import ROOT, LOG_LEVEL


def create_logger():
    logger = logging.getLogger("easyrules_logger")
    logger.setLevel(LOG_LEVEL)

    fh = logging.FileHandler(os.path.join(ROOT, 'easyrules.log'))

    fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt)
    fh.setFormatter(formatter)

    logger.addHandler(fh)
    return logger


logger = create_logger()


def exception_handler(logger: logging.Logger = logger):
    """
    A decorator that wraps the passed in function and logs exceptions should one occur
    """

    def decorator(func):

        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                err = "Exception occured in %s，%s " % (func.__name__, e)
                logger.exception(err)
            raise

        return wrapper

    return decorator
