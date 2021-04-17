from matchers import All, Not, And, Or, HasAtLeast, HasFewerThan, PlaysIn

class QueryBuilder:

    def __init__(self, old_matcher = All(), new_matcher = All()):
        self._matcher = And(old_matcher, new_matcher)

    def build(self):
        return self._matcher

    def playsIn(self, value):
        #self._matchers.append(PlaysIn(value))
        return QueryBuilder(self._matcher, PlaysIn(value))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(self._matcher, HasAtLeast(value, attr))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(self._matcher, HasFewerThan(value, attr))

    def oneOf(self, matcher1, matcher2):
        return QueryBuilder(self._matcher, Or(matcher1, matcher2))
