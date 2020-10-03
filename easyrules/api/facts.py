# coding: utf-8
"""
This class encapsulates a set of facts and represents a facts namespace.
Facts have unique names within a Facts object.
"""

from easyrules.utils import logger
from .fact import Fact


class Facts():
    def __init__(self, facts: set = None):
        self._facts = facts if facts else set()

    def put(self, name: str, value: object):
        """
        Add a fact, replacing any fact with the same name.
        :param name: name of the fact to add, must not be null
        :param value: value of the fact to add, must not be null
        :return:
        """
        if not name: raise ValueError('fact name must not be null')
        if not value: raise ValueError('fact value must not be null')
        fact = self.get_by_name(name)
        if fact:
            self._facts.remove(fact)
        self._facts.add(Fact(name, value))

    def add(self, fact: Fact):
        """
        Add a fact, replacing any fact with the same name.
        :param fact: fact to add, must not be None
        """
        if not fact: raise TypeError('fact must not be None')
        if self.get_by_name(fact.name):
            logger.warning('removed same name fact: %s' % fact)
            self._facts.remove(fact)
        self._facts.add(fact)

    def get(self, fact_name: str):
        # get a fact by name.
        return self.get_by_name(fact_name)

    def remove(self, fact: Fact):
        # Remove a fact.
        if not fact: raise TypeError('fact must not be None')
        fact = self.get_by_name(fact.name)
        if fact:
            self._facts.remove(fact)

    def get_by_name(self, fact_name: str):
        # Get a fact by name.
        if not fact_name: raise TypeError('fact name must not be None')
        for fact in self._facts:
            if fact.name == fact_name:
                return fact
        return None

    def remove_by_name(self, fact_name: str):
        # Remove a fact by name.
        if not fact_name: raise TypeError('fact name must not be None')
        fact = self.get_by_name(fact_name)
        if fact:
            self._facts.remove(fact)

    def as_dict(self):
        # Return a copy of the facts as a dict.
        return {fact.name: fact.value for fact in self._facts}

    def clear(self):
        # Clear facts
        self._facts = set()

    def __repr__(self):
        return '[' + ','.join(self._facts) + ']'

    __str__ = __repr__

    def __len__(self):
        return len(self._facts)

    def __iter__(self):
        return iter(self._facts)
