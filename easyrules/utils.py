# coding: utf-8

import logging
from . import logger


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
