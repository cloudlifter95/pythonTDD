BLANK = object()
class HashTable:
    def __init__(self, capacity) -> 'HashTable':
        self.capacity = capacity
        self.values = self.capacity * [BLANK]
    def __len__(self):
        return len(self.values)
    def __setitem__(self, key, value):
        # self.values.append(value)
        index = hash(key) % len(self)
        self.values[index] = value
    def __getitem__(self, key):
        index = hash(key) % len(self)
        value = self.values[index]
        if value is BLANK:
            raise KeyError(key)
        return value