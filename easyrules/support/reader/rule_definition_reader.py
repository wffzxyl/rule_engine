# coding: utf-8
"""
Rules engine interface.
"""

from abc import ABCMeta, abstractmethod
from typing import List
from easyrules.utils import exception_handler


class RuleDefinitionReader(metaclass=ABCMeta):
    @exception_handler
    @abstractmethod
    def read(self, file_path: str) -> List:
        """
        Read a list of rule definitions from a structured file.
        The file is expected to contain a collection of rule definitions even for a single rule.
        :return: a list of rule definitions
        """
        pass
