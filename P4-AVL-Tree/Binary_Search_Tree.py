class Binary_Search_Tree:
    # TODO.I have provided the public method skeletons. You will need
    # to add private methods to support the recursive algorithms
    # discussed in class

    class __BST_Node:
        # TODO The Node class is private. You may add any attributes and
        # methods you need. Recall that attributes in an inner class 
        # must be public to be reachable from the the methods.
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
            self.height = 1
    def __init__(self):
        self.__root = None

    def __calculate_height(self, node):
        """
        Calculate the height of the given node.
        Performance: O(1)
        """
        if node is None:
            return 0
        return node.height
    def __update_height(self, node):
        """
        Update the height of the given node.
        Performance: O(1)
        """
        if node is not None:
            node.height = 1 + max(self.__calculate_height(node.left), self.__calculate_height(node.right))

    def insert_element(self, value):
        # Insert the value specified into the tree at the correct
        # location based on "less is left; greater is right" binary
        # search tree ordering. If the value is already contained in
        # the tree, raise a ValueError. Your solution must be recursive.
        # This will involve the introduction of additional private
        # methods to support the recursion control variable.
        # Performance: O(log n)
        # Uses private method __recursive_insert
        self.__root = self.__recursive_insert(self.__root, value)
    def __recursive_insert(self, node, value):	
        """
        Private method to recursively insert a value into the tree.
        Performance: O(log n)
        The balancing feature ensures this is the case.
        """
        if node is None: 
            return self.__BST_Node(value)		
        elif value == node.value:
            raise ValueError
        elif value < node.value:
            node.left = self.__recursive_insert(node.left, value)
        elif value > node.value:
            node.right = self.__recursive_insert(node.right, value)
        # Update Height 
        self.__update_height(node)
        return self.__balance(node)

        

    def remove_element(self, value):
        # Remove the value specified from the tree, raising a ValueError
        # if the value isn't found. When a replacement value is necessary,
        # select the minimum value to the from the right as this element'sr
        # replacement. Take note of when to move a node reference and when
        # to replace the value in a node instead. It is not necessary to
        # return the value (though it would reasonable to do so in some 
        # implementations). Your solution must be recursive. 
        # This will involve the introduction of additional private
        # methods to support the recursion control variable.
        # Uses private method __recursive_remove
        # Performance: O(log n)

        self.__root = self.__recursive_remove(self.__root, value)
    def __recursive_remove(self, node, value):
        """
        Private method to recursively remove a value from the tree.
        Performance: O(log n). The balancing feature ensures this is
        the case.
        """
        if node is None:
            raise ValueError
        elif value < node.value:
            node.left = self.__recursive_remove(node.left, value)
        elif value > node.value:
            node.right = self.__recursive_remove(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                # Find the minimum value in the right subtree
                temp = self.__find_min(node.right)
                node.value = temp.value
                node.right = self.__recursive_remove(node.right, temp.value)
        self.__update_height(node)
        return self.__balance(node)

    def __find_min(self, node):
        """
        Private method to find the minimum value in the tree.
        Performance: O(log n)
        This is because the tree is balanced.
        """
        if node is None or node.left is None:
            return node 
        return self.__find_min(node.left)
    
    def in_order(self):
        # Construct and return a string representing the in-order
        # traversal of the tree. Empty trees should be printed as [ ].
        # Trees with one value should be printed as [ 4 ]. Trees with more
        # than one value should be printed as [ 4, 7 ]. Note the spacing.
        # Your solution must be recursive. This will involve the introduction
        # of additional private methods to support the recursion control 
        # variable.
        # Performance: O(n): has to traverse every node in the tree
        # at least once
        if self.get_height() == 0:
            return "[ ]"
        return f"[ {self.__recursive_in_order(self.__root)[:-2]} ]"

    
    def __recursive_in_order(self, node):
        """
        Private method to recursively traverse the tree in-order.
        Performance: O(n): has to traverse every node in the tree
        at least once
        """
        if node is None:
            return ""
        return self.__recursive_in_order(node.left) + str(node.value) + ", " + self.__recursive_in_order(node.right)



    def pre_order(self):
        # Construct and return a string representing the pre-order
        # traversal of the tree. Empty trees should be printed as [ ].
        # Trees with one value should be printed in as [ 4 ]. Trees with
        # more than one value should be printed as [ 4, 7 ]. Note the spacing.
        # Your solution must be recursive. This will involve the introduction
        # of additional private methods to support the recursion control 
        # variable.
        # Performance: O(n): has to traverse every node in the tree
        # at least once
        if self.get_height() == 0:
            return "[ ]"
        return f"[ {self.__recursive_pre_order(self.__root)[:-2]} ]"
    
    def __recursive_pre_order(self, node):
        """
        Private method to recursively traverse the tree pre-order.
        Performance: O(n): has to traverse every node in the tree
        at least once
        """
        if node is None:
            return ""
        return str(node.value) + ", " + self.__recursive_pre_order(node.left) + self.__recursive_pre_order(node.right)

    
        
    def post_order(self):
        # Construct an return a string representing the post-order
        # traversal of the tree. Empty trees should be printed as [ ].
        # Trees with one value should be printed in as [ 4 ]. Trees with
        # more than one value should be printed as [ 4, 7 ]. Note the spacing.
        # Your solution must be recursive. This will involve the introduction
        # of additional private methods to support the recursion control 
        # variable.
        # Performance: O(n): has to traverse every node in the tree
        # at least once
        if self.get_height() == 0:
            return "[ ]"
        return f"[ {self.__recursive_post_order(self.__root)[:-2]} ]"

    def __recursive_post_order(self, node):
        """
        Private method to recursively traverse the tree post-order.
        Performance: O(n): has to traverse every node in the tree
        at least once
        """
        if node is None:
            return ""
        return self.__recursive_post_order(node.left) + self.__recursive_post_order(node.right) + str(node.value) + ", "

    def to_list(self):
        # Construct and return a Python list/array containing the in-order
        # traversal of the tree. Your solution must be recursive. This will
        # involve the introduction of additional private methods to support
        # the recursion control variable.
        return self.__recursive_to_list(self.__root)
    
    def __recursive_to_list(self, node):
        """
        Private method for recursively constructing a list containing the in-order traversal of the tree.

        Performance: O(n)
        """
        if node is None:
            return []
        return self.__recursive_to_list(node.left) + [node.value] + self.__recursive_to_list(node.right)

    def get_height(self):
        # return an integer that represents the height of the tree.
        # assume that an empty tree has height 0 and a tree with one
        # node has height 1. This method must operate in constant time.
        # Performance: O(1): Only needs to access the height attribute of the root node
        return self.__calculate_height(self.__root)
    
    def __str__(self):
        # return a string representation of the tree using the in-order
        # traversal.
        return self.in_order()
    
    def __balance_factor(self, node):
        # Relies on the __calculate_height method to calculate the balance, which 
        # is O(1) time for each, so this method is O(1) time.
        return self.__calculate_height(node.right) - self.__calculate_height(node.left)
    def __rotate_right(self, node):
        # Rotate the tree to the right at the node specified. Return the
        # new root of the subtree. This method must operate in constant time.	
        # This is in O(1) time because it only has to switch the 
        # position of a set number of nodes.
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        self.__update_height(node)
        self.__update_height(new_root)
        return new_root
    def __rotate_left(self, node):
        # Rotate the tree to the left at the node specified. Return the
        # new root of the subtree. This method must operate in constant time.
        # This is in O(1) time because it only has to switch the
        # position of a set number of nodes.
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        self.__update_height(node)
        self.__update_height(new_root)
        return new_root
    
    def __balance(self, node):
        """
        Balance the tree at the node specified. Return the new root of the subtree.
        Performance: O(1): Relies on the __balance_factor and __rotate methods, which are O(1) time.
        """
        if self.__balance_factor(node) == -2:
            if self.__balance_factor(node.left) == -1 or self.__balance_factor(node.left) == 0:
                return self.__rotate_right(node)
            if self.__balance_factor(node.left) == 1:
                node.left = self.__rotate_left(node.left)
                return self.__rotate_right(node)
        elif self.__balance_factor(node) == 2:
            if self.__balance_factor(node.right) == 1 or self.__balance_factor(node.right) == 0:
                return self.__rotate_left(node)
            if self.__balance_factor(node.right) == -1:
                node.right = self.__rotate_right(node.right)
                return self.__rotate_left(node)
        return node

if __name__ == '__main__':
    pass #unit tests make the main section unnecessary
