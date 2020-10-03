# coding: utf-8
"""
This interface represents a rule's action.
"""

from abc import ABCMeta, abstractmethod
from easyrules.utils import exception_handler
from .facts import Facts


class Action(metaclass=ABCMeta):
    @exception_handler
    @abstractmethod
    def execute(self, facts: Facts):
        """
        Execute the action when the rule's condition evaluates to true.
        :param facts: facts known at the time of execution of the action
        :return:
        """
        pass
