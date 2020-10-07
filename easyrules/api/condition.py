# coding: utf-8
"""
This interface represents a rule's condition.
"""

from abc import ABCMeta, abstractmethod
from .facts import Facts


class Condition(metaclass=ABCMeta):
    @abstractmethod
    def evaluate(self, facts: Facts) -> bool:
        """
        Evaluate the condition according to the known facts.
        :param facts: facts known when evaluating the rule
        :return: true if the rule should be triggered, false otherwise
        """
        return True
