class Node:
    def __init__(self, data, children = None):
        self.data = data
        if children:
            self.children = children
        else:
            self.children = []


def remove_node(self, x):
    """Method on a Node that takes an integer/number and removes all nodes
    with a value equal to that number, along with all descendants."""

    # Base case if the very first item has x value as its data
    if self.data == x:
        self.data == None
        self.children = []
        return

    to_visit = [self]

    while to_visit:
        current = to_visit.pop()
        for child in current.children:
            if child.data == x:
                current.children.remove(child)
            to_visit.extend(current.children)

testTree = Node([
    Node(4, [3, 7]),
    Node(3, [2]),
    Node(2, [None]),
    Node(7, [9, 7, 0]),
    Node(9, [None]),
    Node(7, [None]),
    Node(0, [None])])

if __name__ == "__main__":
    remove_node(testTree, 7)
    print(Node.children)
