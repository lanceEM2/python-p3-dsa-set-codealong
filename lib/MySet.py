class MySet:
    def __init__(self, enumerable=None):
        if enumerable is None:
            enumerable = []
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True

    def has(self, value):
        return value in self.dictionary

    def add(self, value):
        self.dictionary[value] = True   # Add a value as a key on the dictionary
        return self

    def delete(self, value):
        self.dictionary.pop(value, None)
        return self

    def size(self):
        return len(self.dictionary)

    def clear(self):
        return self.dictionary.clear()