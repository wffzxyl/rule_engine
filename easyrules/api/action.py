# coding: utf-8
"""
This interface represents a rule's action.
"""

from abc import ABCMeta, abstractmethod
from .facts import Facts


class Action(metaclass=ABCMeta):
    # TODO, A exception decoration.
    @abstractmethod
    def execute(self, facts: Facts):
        """
        Execute the action when the rule's condition evaluates to true.
        :param facts: facts known at the time of execution of the action
        :return:
        """
        pass


