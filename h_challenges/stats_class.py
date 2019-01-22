# Write a class with three different methods - insert, get_mean, and get_median.
# insert should add an instance of a value.
# get_mean should return the mean of the instance.
# get_median should return the median of the instance.
# These methods have to be written with O(k) in memory.

class Stats(object):
    def __init__(self):
        self.total_sum = 0
        self.dict = {}
        self.total_instances = 0
        self.key_list = []

    def insert(self, value):
        # (1) add the value to the total sum
        self.total_sum += value
        self.total_instances += 1

        if value not in self.key_list:
            self.key_list.append(value)
            self.key_list = sorted(self.key_list)

        # (2) add value to dictionary & increase count
        if value in self.dict:
            self.dict[value] = self.dict[value] + 1
        else:
            self.dict[value] = 1

    def get_mean(self):
        return self.total_sum/self.total_instances

    def get_median(self):
        middle = self.total_instances/2
        tally = 0

        if self.total_instances % 2 == 0:
            #if even, then we have to add the two items in the middle

            for value in self.key_list:
                tally = tally + self.dict[value]

                if tally >= middle:
                    break

            value1 = value

            tally = 0

            for value in self.key_list:
                tally = tally + self.dict[value]

                if tally >= middle + 1:
                    break

            value2 = value

            return (value1 + value2)/2

        else:
            #if odd, then we have to pull the item at that instance
            for value in self.key_list:
                tally = tally + self.dict[value]

                if tally >= middle:
                    break
            return value

test1 = Stats()
test1.insert(10)
test1.insert(0)
test1.insert(5)

# print(test1.get_mean())
print(test1.get_median())
