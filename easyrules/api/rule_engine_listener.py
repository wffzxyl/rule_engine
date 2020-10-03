# coding: utf-8
"""
A listener for rules engine execution events.
"""

from abc import ABCMeta, abstractmethod
from .facts import Facts
from .rules import Rules


class RulesEngineListener(metaclass=ABCMeta):

    @abstractmethod
    def before_evaluate(self, rules: Rules, fact: Facts):
        """
        Triggered before evaluating the rule set.
        When this listener is used with a InferenceRulesEngine object,
        this method will be triggered before the evaluation of each candidate rule set in each iteration.
        :param rules: to fire
        :param fact: present before firing rules
        """
        pass

    @abstractmethod
    def after_evaluate(self, rules: Rules, fact: Facts):
        """
        Triggered after executing the rule set.
        When this listener is used with a InferenceRulesEngine object,
        this method will be triggered after the execution of each candidate rule set in each iteration.
        :param rules: fired
        :param fact: present before firing rules
        """
        pass
