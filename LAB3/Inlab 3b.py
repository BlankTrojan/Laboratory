class Node:

    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def getfullCount(y):
    # Base Case
    if y is None:
        return 0


    queue = []


    queue.append(y)

    count = 0
    while (len(queue) > 0):
        node = queue.pop(0)


        if node.left is not None and node.right is not None:
            count = count + 1


        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)

    return count

y = Node(3)
y.left = Node(2)
y.right = Node(6)
y.left.right = Node(5)
y.left.right.left = Node(1)
y.left.right.right = Node(6)
y.right.right = Node(9)
y.right.right.left = Node(4)

print(getfullCount(y))