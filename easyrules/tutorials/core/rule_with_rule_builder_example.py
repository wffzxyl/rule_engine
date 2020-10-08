# coding: utf-8

from easyrules import Action, Condition, Facts, Rules, DefaultRuleEngine, RuleBuilder

# s1: Get facts.
facts = Facts()


# s2: Define some Conditions.
class HelloWorldCondition(Condition):
    def evaluate(self, facts: Facts):
        return True


# s3: Define some Actions.
class HelloWorldAction(Action):
    def execute(self, facts: Facts):
        print('hello word')


# s4: Build some DefaultRule instances with RuleBuilder.
rule = RuleBuilder() \
    .name('hello word') \
    .description('desc') \
    .priority(1) \
    .domain('example') \
    .when(HelloWorldCondition()) \
    .then(HelloWorldAction()) \
    .build()

# s5: Add rules to Rules instance.
rules = Rules()
rules.add(rule)

# s6: Define DefaultRuleEngine object and fire rules for target facts.
engine = DefaultRuleEngine()
engine.fire(rules, facts)
