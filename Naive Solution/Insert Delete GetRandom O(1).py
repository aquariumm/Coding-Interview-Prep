'''
    Rumtime:
        time: insert(), remove() take O(1) due to set() properties. getRandom() takes O(n) due to random.sample()
        space: O(1) since no extra space
    Analysis: 
        Given: instructions regarding operations
        Ask: perform operations
        To accomplish this: set data structure is selected because add() and remove() on a set take O(1).
        since we are using a set not a list, random.choice(list) can't be used, which will take O(1). Options
        left is random.sample()
'''
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = set()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.set:
            return False
        else:
            self.set.add(val)
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.set:
            self.set.remove(val)
            return True
        return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        if len(self.set) == 0:
            return None
        tem = random.sample(self.set, 1)[0]
        
        return tem


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
