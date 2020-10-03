# coding: utf-8

from easyrules import RuleDecorator, Fact, Rule, Facts, Rules, DefaultRuleEngine, ConditionalRuleGroup
from typing import List


@RuleDecorator(name='rule1', domain='example', priority=2)
class Rule1(Rule):
    def evaluate(self, facts: List[Fact]):
        return True

    def execute(self, facts: List[Fact]):
        print('do rule1')


@RuleDecorator(name='rule2', domain='example', priority=1)
class Rule2(Rule):
    def evaluate(self, facts: List[Fact]):
        return True

    def execute(self, facts: List[Fact]):
        print('do rule2')


facts = Facts()

unit_rule_group = ConditionalRuleGroup(name='a_conditional_rule_group', domain='example', priority=1)
unit_rule_group.add_rule(Rule1())
unit_rule_group.add_rule(Rule2())

rules = Rules()
rules.add(unit_rule_group)

engine = DefaultRuleEngine()
engine.fire(rules, facts)
