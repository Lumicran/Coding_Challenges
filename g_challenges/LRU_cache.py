# 11.04.18

# Part I - What do the following lines of code give you?
A1 = range(10)
# Gives you numbers 0 through 9

A2 = sorted([i for i in A1 if i in A1])
# List comprehension -
# will give you a sorted copy of the list in A1 (numbers 0 through 9)

A3 = [i for i in A1 if i in [4, 5, 6]]
# List comprehension -
# Will give you a list with 4, 5, 6

A4 = {i:i*i for i in A1}
# Dictionary comprehension -
# For each number in A1 (which is 0 to 9)
# Will create a dictionary where the key is
# the numbers 0 to 9, and the key for each is the
# number multiplied by itself.

A5 = [[i,i*i] for i in A1]
# list comprehension (list in a list) -
# for each number in A1 (0-9), creates a list where
# the first item is the number, and the second item
# is the number multiplied by itself.


# Given the LRU_Cache class below (with self.size in __init__ and the skeleton of the methods
# get and put, complete __init__, along with get and put.)
class LRU_Cache():
    """Size-limited associative storage that will, when full, discard the least recently used key"""

    def __init__(self, size=3):
        self.size = size
        self.keyList = []
        self.keyDict = {}

    def get(self, key):
        """Retrieves the value associated with key returns None if the key is not present"""

        # Iterate to update list
        if key in self.keyList:
            self.keyList.remove(key)
            self.keyList.append(key)

            print(self.keyList)
            #return value of item
            return self.keyDict[key]


    def put(self, key, value):
        """Associates a value with a key.  If a new key is introduced,and would result in size being exceeded, remove the value least recently assigned or retrieved."""

        # Add/update key & value to dictionary
        self.keyDict[key] = value

        if key not in self.keyList:
            self.keyList.append(key)
        else:
            self.keyList.remove(key)
            self.keyList.append(key)


        if len(self.keyDict) > self.size:
            key = self.keyList.pop(0)
            del(self.keyDict[key])

        print(self.keyList)


def unit_test():
    test_cache = LRU_Cache(2)

    test_cache.put(1, "alpha")

    test_cache.put(2, "beta")

    test_cache.put(3, "charlie")

    test_cache.put(4, "delta")

    print(test_cache.get(1))
    print(test_cache.get(4))

    test_cache.put(2, "epsilon")

    test_cache.put(5, "foxtrot")

    print(test_cache.get(2))


if _name_ == "_main_":
    unit_test()
