# coding: utf-8

from abc import ABCMeta


class Fact(metaclass=ABCMeta):
    def __init__(self, name: str, value: object):
        if not name or not value:
            raise ValueError('name or value must not be None')
        self._name = name
        self._value = value

    @property
    def name(self):
        return self._name

    @property
    def value(self):
        return self._value

    def equal(self, other):
        if id(self) == id(other): return True
        if not other or type(self) != type(other): return False
        return self._name == other.name and self._value == other.value

    def __repr__(self):
        return 'Fact{name=%s, value=%s}' % (self._name, self._value)

    __str__ = __repr__