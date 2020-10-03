# coding: utf-8
"""
A class representing a named fact. Facts have unique names within a Fact instance.
"""

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

    def __repr__(self):
        return 'Fact{name=%s, value=%s}' % (self._name, self._value)

    __str__ = __repr__

    def __eq__(self, other):
        """
        The Facts API represents a namespace for facts where each fact has a unique name.
        Hence, equals/hashcode are deliberately calculated only on the fact name.
        """
        if id(self) == id(other): return True
        if not other or isinstance(other, Fact): return NotImplemented
        return self._name == other.name and self._value == other.value

    def __hash__(self):
        res = hash(self._name)
        res = 31 * res + hash(self._value)
        return res
