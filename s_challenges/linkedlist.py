# Write the extend method for a singly linked list.
# Takes a list of values and adds them to the end of a given LinkedList.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def append(self, val):
        n = Node(val)
        current = self.head

        if current is None:
            self.head = n
            return

        while current.next:
            current = current.next

        current.next = n


    def extend(self, lst):

        if len(lst) == 0:
            return []

        if self.head is None:
            self.head = Node(lst[0])
            current = self.head

            for i in range(1, len(lst)):
                current.next = Node(lst[i])
                current = current.next           

            return


        current = self.head

        while current.next is not None:
            current = current.next

        for i in range(len(lst)):
            current.next = Node(lst[i])
            current = current.next

        # return_file = []

        # current = self.head

        # while current:
        #     return_file.append(current.value)
        #     current = current.next

        # return return_file

    def extend2(self, lst):
        current = self.head

        while current and current.next:
            current = current.next

        for item in lst:
            n = Node(item)
            if self.head is None:
                self.head = n
                current = n
            else:
                current.next = n
                current = current.next


individual = Linkedlist()
lst = ["2", "3", "4", "5"]
print(individual.extend(lst))

test2 = Linkedlist()
test2.append("a")
test2.append("b")
test2.append("c")
lst2 = ["d", "e", "f", "g"]
print(test2.extend(lst2))

test3 = Linkedlist()
lst3 = []
print(test3.extend(lst3))









