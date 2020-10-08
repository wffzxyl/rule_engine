# coding: utf-8

import sys
from enum import Enum

DEFAULT_NAME: str = 'rule'
DEFAULT_DESCRIPTION: str = 'description'
DEFAULT_DOMAIN: str = 'example'
DEFAULT_PRIORITY: int = sys.maxsize - 1


class CompositeRuleType(Enum):
    ACTIVATION_RULE_GROUP = 'ActivationRuleGroup'
    CONDITIONAL_RULE_GROUP = 'ConditionalRuleGroup'
    UNIT_RULE_GROUP = 'UnitRuleGroup'
