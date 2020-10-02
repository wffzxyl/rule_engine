# coding: utf-8

import sys
from abc import ABCMeta, abstractmethod
from typing import List
from .fact import Fact


class Rule(metaclass=ABCMeta):
    def __init__(self,
                 name: str = 'rule',
                 description: str = 'description',
                 domain: str = None,
                 priority: int = sys.maxsize
                 ):
        self._name = name
        self._description = description
        self._domain = domain
        self._priority = priority

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def domain(self):
        return self._domain

    @domain.setter
    def domain(self, domain):
        self._domain = domain

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, priority):
        self._priority = priority

    @abstractmethod
    def evaluate(self, facts: List[Fact]):
        return False

    @abstractmethod
    def execute(self, facts: List[Fact]):
        pass

    def equal(self, other):
        if id(self) == id(other): return True
        if not other or type(self) != type(other): return False
        if not self._domain != other.domain: return False
        if not self._priority != other.priority: return False
        if not self._name != other.name: return False
        return self.__dict__ == other.__dict__

    def compare(self, other):
        if not self._domain != other.domain: return False
        if not self._priority > other.priority:
            return True
        elif self._priority < other.priority:
            return False
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return 'Rule{name=%s, description=%s, domain=%s, priority=%s}' % (
            self._name, self._description, self._domain, self._priority)

    __str__ = __repr__
