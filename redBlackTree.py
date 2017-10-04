'''
This file demonstrates the construction and use of a red-black tree. Recall that a red-black
tree is a type of balanced binary search tree that uses coloring of nodes in order to facilitate in
the balancing process of a binary search tree.

Recall that the properties of a red black tree are as follows:

- Root property - root node should be black
- Leaf property - every leaf node should be black
- Red property - The children of a red node should be black
- Depth property - All paths to a leaf node should have the same black node depth

In this file we set up two demo red black trees and then show what the tree looks like during left and right rotations.

'''

from print_tree import print_tree_from_breadth_first_stack

class RedBlackNode(object):
    color = None
    value = None
    left_node = None
    right_node = None
    parent = None
    nil = False
    visited = False

    #setter methods to be referenced by property methods below
    def setParent(self, parent):
        self._parent = parent

    def setLeft(self, left):
        self._left = left

    def setRight(self, right):
        self._right = right

    def setValue(self, value):
        self._value = value

    def setNil(self, nil):
        self._nil = nil

    def setColor(self, color):
        self._color = color

    def setVisited(self, visited):
        self._visited = visited


    #property methods
    parent = property(fget=lambda self: self._parent if self._parent!=None else RedBlackNode(None, True),fset=setParent)
    left = property(fget=lambda self: self._left if self._left!=None else RedBlackNode(None, True), fset = setLeft)
    right= property(fget=lambda self: self._right if self._right!=None else RedBlackNode(None, True), fset = setRight)
    value = property(fget=lambda self: self._value ,fset=setValue)
    nil = property(fget=lambda self: self._nil, fset=setNil)
    color = property(fget=lambda self: self._color ,fset=setColor)
    visited = property(fget=lambda self: self._visited ,fset=setVisited)

    def __init__(self, value=None, nil=False):
         self._color = "black"
         self._value = value
         self._left = None
         self._right = None
         self._parent = None
         self._nil=nil
         self._visited = False

#red black tree to represent tree to hold red black nodes
class RedBlackTree(object):
    _root = None
    def set_root(self, newroot):
        self._root = newroot

    root = property(fget=lambda self: self._root, fset=set_root)

    def reset_nodes(self, number_of_nodes):
        '''
        Set up demo nodes with values 1 to 15
        '''
        self.nodes_array = []
        for i in range(0, number_of_nodes+1):
            self.nodes_array.append(RedBlackNode(value=i))
        self.root = None


    def insert_node(self, current, newnode):
        '''
        Insert a node the same way that you would in a standard binary search tree.
        This is to be later rotated to be in line with properties of a red black tree.
        '''
        if self.root == None:
            self.root = newnode
            return
        #if both are null return
        if current.left.nil == True and current.right.nil==True:
           if newnode.value < current.value:
               current.left = newnode
               newnode.parent = current
               return
           else:
               current.right = newnode
               newnode.parent = current
               return

        if newnode.value < current.value:
            if current.left.nil == True:
                current.left = newnode
                newnode.parent = current
            else:
                self.insert_node(current.left, newnode)
        else:
            if current.right.nil == True:
                current.right = newnode
                newnode.parent = current
            else:
                self.insert_node(current.right, newnode)

    def traverse_tree(self, current):

        print "value: " + str(current.value) + " color: " + str(current.color)
        #base case when you have reached a leaf node
        if current.left.nil == True and current.right.nil == True:
            return

        if  current.left.nil==False:
            print "going left from " + str(current.value) + " color: " + str(current.color)
            self.traverse_tree(current.left)

        if current.right.nil == False:
            print "going right from " + str(current.value) + " color: " + str(current.color)
            self.traverse_tree(current.right)

    def print_tree(self):
        stack =  self.traverse_tree_by_levels()
        print_tree_from_breadth_first_stack(stack, print_method="red_black_node")

    def traverse_tree_by_levels(self):
        stack = self.tree_level_visit(self.root)
        if stack == None:
            return None
        for node in stack:
            node.visited = False
        #print [node.value for node in stack]
        return [node for node in stack]

    def tree_level_visit(self, current):
        stack = []
        if current == None:
            return
        current.visited = True
        stack.append(current)
        stack.append(current.left)
        stack.append(current.right)

        for i in range(0 , len(stack)):
            if stack[i].visited == False:
                stack.append(stack[i].left)
                stack.append(stack[i].right)
                stack[i].visited = True

        return stack


    def rotate_left(self, xnode):
        '''
        Performs a left rotate around the xnode
        '''

        ############get Y node, get y node left, set x right as y left, set ynode parent to x parent#################
        ynode = xnode.right
        xnode.right = ynode.left

        if ynode.left.nil != True:
           ynode.left.parent = xnode

        #set y parent to x parent
        ynode.parent = xnode.parent
        #######################################

        #######################################
        #below if else block to set right or left of parent to ynode or set as root if no parent
        #  or set y as root
        #check to see if at root first
        if xnode.parent.nil == True:
            self.root = ynode
        elif xnode == xnode.parent.left:
               xnode.parent.left = ynode
        else: #x must have been on right
              xnode.parent.right = ynode
        #######################################

        #finally put y above x and set x as its left node
        ynode.left = xnode
        xnode.parent = ynode

    def rotate_right(self,ynode):
        '''
        #performs a right rotate around the ynode
        '''

        ############get x node, get x node right, set y left as x right, set parent of xnode to y parent#################
        xnode = ynode.left
        ynode.left = xnode.right

        if xnode.right.nil!= True:
           xnode.right.parent = ynode

        #set x parent to y parent
        xnode.parent = ynode.parent
        #######################################

        #######################################
        #below if block to set ynode new parent to xnode as right or left, or set x as theroot
        #check to see if at root first
        if (ynode.parent.nil == True):
            self.root = xnode
        elif ynode == ynode.parent.right:
             ynode.parent.right = xnode
        else: #y must have been on right
             ynode.parent.left = xnode
        #######################################
        #finally put x above y and set y as its right node
        xnode.right = ynode
        ynode.parent = xnode


    def insert_red_black(self, newnode):
        '''
        Insert a node into a red black tree using standard binary search tree insertion and then
         update nodes to be congruent with properties of a red black tree.
        '''
        newnode.color = "red"
        #insert node in the standard binary search tree way
        self.insert_node(self.root, newnode)

        while newnode.parent.color == "red":

            #newnode parent on left of its parent
            if newnode.parent == newnode.parent.parent.left:
              #case 1: if newnodes right uncle is red
              if newnode.parent.parent.right.color == "red":
                  newnode.parent.color = "black"
                  newnode.parent.parent.right.color = "black"
                  newnode.parent.parent.color = "red"
                  newnode = newnode.parent.parent

              else: #else newnodes uncle must be black or nonexist
                   #case 2: newnode right uncle black and a right child
                   if newnode ==  newnode.parent.right:
                        newnode = newnode.parent
                        self.rotate_left(newnode)
                   #newnode right uncle black and newnode is left child
                   newnode.parent.color = "black"
                   newnode.parent.parent.color = "red"
                   self.rotate_right(newnode.parent.parent)
            #begin symmetric for cases 4-6

            elif newnode.parent == newnode.parent.parent.right:
                #case 4 if left uncle is red
                if newnode.parent.parent.left.color =="red":
                   newnode.parent.color = "black"
                   newnode.parent.parent.left.color = "black"
                   newnode.parent.parent.color = "red"
                   newnode = newnode.parent.parent

                else:  #left uncle is nonexistent or black
                 #case 5 newnode left uncle black, new node left child
                  if newnode == newnode.parent.left:
                     newnode = newnode.parent
                     self.rotate_right(newnode)
                  #case 6 newnode left uncle black, newnode right child
                  newnode.parent.color = "black"
                  newnode.parent.parent.color = "red"
                  self.rotate_left(newnode.parent.parent)
        self.root.color = "black"
        return newnode

    def setup_nodes_demo(self, node_insertion_list):
        for num in node_insertion_list:
            self.insert_red_black(self.nodes_array[num])

    def node_insert_demo(self, node_insertion_list):
        for num in node_insertion_list:
            print ":::::: before insertion of: " + str(num) + " ::::::"
            self.print_tree()
            self.insert_red_black(self.nodes_array[num])
            print ":::::: after insertion of: " + str(num) + "::::::"
            self.print_tree()


redandblack = RedBlackTree()
node_list1 = [4, 3, 5, 2, 7, 6, 8, 9, 10 ,11]
node_list2 = [11, 2, 14, 1, 7, 15, 5, 8, 4]
node_list3 = [5, 3, 7, 1, 9, 4, 6]


print "------  Red Black Tree Demo 1  ------"
print "inserting the following nodes in order: "
print str(node_list1)
redandblack.reset_nodes(15)
redandblack.setup_nodes_demo(node_list1)
print "--- Red Black Tree 1 is ---"
redandblack.print_tree()

print ""
print ""
print "--------- Red Black Tree Demo 2 ---------"
print "inserting the following nodes in order:"
print str(node_list2)
redandblack.reset_nodes(15)
redandblack.setup_nodes_demo(node_list2)
print "--------- Red Black Tree 2 is  ---------"
redandblack.print_tree()
print ""
print ""

print "--------- Red Black Tree print after each insertion ---------"
print "inserting the following nodes in order: "
print str(node_list3)
redandblack.reset_nodes(15)
redandblack.node_insert_demo(node_list3)
