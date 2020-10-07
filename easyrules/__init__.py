# coding: utf-8
# flake8: noqa
from __future__ import absolute_import

VERSION = (0, 0, 2)
__version__ = VERSION
__versionstr__ = ".".join(map(str, VERSION))

import logging

logger = logging.getLogger("easyrules")
logger.addHandler(logging.NullHandler())

from . import config
from .utils import logger, exception_handler

from .api import Action, Rule, Condition, RuleDecorator, Fact, Facts, Rule, Rules, RulesEngine, RulesEngineParameters
from .core import DefaultRule, DefaultRuleEngine, RuleBuilder
from .support import ActivationRuleGroup, CompositeRule, ConditionalRuleGroup, UnitRuleGroup, YamlRuleDefinitionReader, YamlRuleFactory