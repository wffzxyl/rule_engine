# coding: utf-8
# flake8: noqa
from __future__ import absolute_import

VERSION = (0, 0, 1)
__version__ = VERSION
__versionstr__ = ".".join(map(str, VERSION))

import logging

logger = logging.getLogger("easyrules")
logger.addHandler(logging.NullHandler())

from .api import Action, Condition, Fact, Facts, Rule, Rules, RulesEngine, RulesEngineParameters
from .core import DefaultRule, DefaultRuleEngine, RuleBuilder
from .decorator import DRule