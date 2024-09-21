class RandomizedSet:

    def __init__(self):
        self.items = []
        self.storeValues = {}

    def insert(self, val: int) -> bool:
        if val in self.storeValues:
            return False
        self.items.append(val)
        self.storeValues[val] = len(self.items) - 1
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.storeValues:
            return False
        
        last_element = self.items[-1]
        index_to_remove = self.storeValues[val]
        self.items[index_to_remove] = last_element
        self.storeValues[last_element] = index_to_remove
        self.items.pop()
        del self.storeValues[val]

        return True
        

    def getRandom(self) -> int:
        if not self.items:
            return None
        return random.choice(self.items)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()