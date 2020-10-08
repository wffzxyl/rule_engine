# coding: utf-8
# flake8: noqa
from __future__ import absolute_import

VERSION = (0, 2, 0)
__version__ = VERSION
__versionstr__ = ".".join(map(str, VERSION))

import logging

logger = logging.getLogger("easyrules")
logger.addHandler(logging.NullHandler())

from . import config
from .api import Action
from .api import Condition
from .api import Fact
from .api import Facts
from .api import Rule
from .api import RuleDecorator
from .api import RulesEngineListener
from .api import RuleListener
from .api import Rules
from .api import RulesEngine
from .api import RulesEngineParameters
from .core import DefaultRule
from .core import DefaultRuleEngine
from .core import RuleBuilder
from .support import ActivationRuleGroup
from .support import CompositeRule
from .support import ConditionalRuleGroup
from .support import UnitRuleGroup
from .support import YamlRuleDefinitionReader
from .support import YamlRuleFactory
from .utils import logger, exception_handler
