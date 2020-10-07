# coding: utf-8
"""
Basic rule implementation class that provides common methods.
You can extend this class and override evaluate and execute methods
to provide rule conditions and actions logic.
"""

from abc import ABCMeta, abstractmethod
from functools import total_ordering
from easyrules.config import DEFAULT_NAME, DEFAULT_DESCRIPTION, DEFAULT_DOMAIN, DEFAULT_PRIORITY
from easyrules.utils import exception_handler
from .facts import Facts


@total_ordering
class Rule(metaclass=ABCMeta):
    def __init__(self,
                 name: str = DEFAULT_NAME,
                 description: str = DEFAULT_DESCRIPTION,
                 domain: str = DEFAULT_DOMAIN,
                 priority: int = DEFAULT_PRIORITY
                 ):
        self._name = name
        self._description = description
        self._domain = domain
        self._priority = priority

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, description: str):
        self._description = description

    @property
    def domain(self) -> str:
        return self._domain

    @domain.setter
    def domain(self, domain: str):
        self._domain = domain

    @property
    def priority(self) -> int:
        return self._priority

    @priority.setter
    def priority(self, priority: str):
        self._priority = priority

    @abstractmethod
    def evaluate(self, facts: Facts) -> bool:
        """
        This method encapsulates the rule's conditions.
        :param facts: to fire
        :return: True if the rule should be applied given the provided facts, false otherwise
        """
        pass

    @exception_handler
    @abstractmethod
    def execute(self, facts: Facts):
        """
        This method encapsulates the rule's actions.
        :param facts: fired
        """
        pass

    def __repr__(self):
        return 'Rule{name=%s, description=%s, domain=%s, priority=%s}' % (
            self._name, self._description, self._domain, self._priority)

    __str__ = __repr__

    def __eq__(self, other):
        """
        Rules are unique according to their names within a rules engine registry.
        Override equal method based on the object id or all properties value.
        """
        #
        if id(self) == id(other): return True
        if not other or isinstance(other, Rule) or self._domain != other.domain: return False
        if not self._priority != other.priority: return False
        if not self._name != other.name: return False
        return self.__dict__ == other.__dict__

    def __lt__(self, other):
        # Override less than method based on the priority property.
        if id(self) == id(other): return False
        if not other or isinstance(other, Rule) or self._domain != other.domain: return False
        if not self._priority > other.priority: return True
        if not self._name != other.name: return False
        return False

    def __hash__(self):
        res = hash(self._name)
        res = 31 * res + hash(self._description) if self._description else 0
        res = 31 * res + self._priority
        return res
