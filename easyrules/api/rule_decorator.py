# coding: utf-8

from functools import wraps
from easyrules import config


class RuleDecorator(object):
    def __init__(self,
                 name: str = config.DEFAULT_NAME,
                 description: str = config.DEFAULT_DESCRIPTION,
                 domain: str = config.DEFAULT_DOMAIN,
                 priority: int = config.DEFAULT_PRIORITY
                 ):
        self._name = name
        self._description = description
        self._domain = domain
        self._priority = priority

    def __call__(self, cls, *args, **kwargs):
        # Here, Change a class to a function.
        @wraps(cls)
        def wrap(*args, **kwargs):
            obj = cls(*args, **kwargs)
            obj.name = self._name
            obj.description = self._description
            obj.domain = self._domain
            obj.priority = self._priority
            # Here, Change the function to a class instance.
            return obj

        return wrap
