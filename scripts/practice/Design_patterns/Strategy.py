# This is a Behavioural strategy used for when we want the class to be Open - for extenstions and closed for modifications
# this is called open-closed principle

from abc import ABC, abstractmethod

class FilterStrategy(ABC):

    @abstractmethod
    def removeValue(self, val):
        pass

class RemoveNegativeStrategy(FilterStrategy):

    def removeValue(self, val):
        return val < 0
    
class RemoveOddStrategy(FilterStrategy):

    def removeValue(self, val):
        return abs(val) % 2

class Values:

    def __init__(self, val):
        self.vals = val

    def filter(self, strategy):
        res = []
        for n in self.vals:
            if not strategy.removeValue(n):
                res.append(n)
        return res
    
values = Values([-3, -2, -1, 0, 1 , 2, 3, 4, 5, 6, 7])

print(values.filter(RemoveNegativeStrategy()))
print(values.filter(RemoveOddStrategy()))

# this way we can add additional strategies without modifying our values class