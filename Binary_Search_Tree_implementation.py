class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
    # for adding child to Tree Structure
    def add_children(self, data):
        if data == self.data:
            return

        if data < self.data:
            #Add to left side
            if self.left:
                self.left.add_children(data)
            else:
                self.left = BinarySearchTreeNode(data)

        else:
            #Add to right side
            if self.right:
                self.right.add_children(data)
            else:
                self.right = BinarySearchTreeNode(data)


    # In order traversal of Tree Structure
    def in_order_traversal(self):
        elements = []
        # visit left node
        if self.left:
            elements += self.left.in_order_traversal()

        #Visit base node

        elements.append(self.data)

        #visit right node
        if self.right:
            elements+= self.right.in_order_traversal()

        return elements
    # Searching the node vlue in Tree Structure
    def search(self, val):

        if self.data == val:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                  return False


        if val > self.data:
            #Value might be in right subtree
            if self.right:
                return self.right.search(val)
            else:
                return False




def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_children(elements[i])
    return root

if __name__ == '__main__':
    number = [4,4, 1,20,9,23,18,34, 4]
    numbers_tree = build_tree(number)
    #print(numbers_tree.in_order_traversal())
    print(numbers_tree.search(34))

