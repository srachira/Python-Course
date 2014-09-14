__author__ = 'SuSh'
from treeutils import *

#BST PROBLEM

class bst(object):

    def __init__(self):
        self.value = None
        self.flag = True
    def bst1(self,root):
        if(root.value >= self.value):
            self.value = root.value
        else:
            self.flag=False

#Max Child Count

def degree(root):
    if root is None:
        return 0
    elif root.right is not None and root.left is not None:
        return 2
    elif root.right or root.left:
        return 1

def max_count(root):
    if root is not None:
        count=degree(root)
        if count < 2:
            count2 = degree(root.left)
            if count2 > count:
                count=count2
            count2 = degree(root.right)
            if count2 > count:
                count=count2
    return count

def height(root):
    if(root.left is None and root.right is None):
        root.value=0
        return
    left_value=0
    right_value=0
    if root.left:
        left_value=root.left.value
    if root.right:
        right_value=root.right.value
    root.value=max(left_value,right_value)+1


def balance(root):
    left_value=0
    right_value=0
    if(root.left):
        left_value=root.left.value
    if(root.right):
        right_value=root.right.value
    root.value=left_value-right_value
    print root.value

class depth(object):
    def __init__(self):
        self.first_node = None
    def find_depth(self, node):
        if self.first_node is None:
            self.first_node = node.value
            node.value = 0
        if node.left is not None:
            node.left.value = node.value + 1
        if node.right is not None:
            node.right.value = node.value + 1

if __name__ == "__main__":
    print "BST CHECK"
    input = (10, (3,None,8),(15,13,None))
    root = create_tree(input)
    c = bst()
    in_order(root,c.bst1)
    if c.flag == False:
        print "Not a BST"
    else:
        print "BST"

    print "Max Child Check"
    input = (10, (20,None,40),(30,50,None))
    root = create_tree(input)
    a=max_count(root)
    print "Max is",a

    input = (7, (10, 18, 20), 12)
    root = create_tree(input)
    a=max_count(root)
    print "Max is",a

    print "Finding Weight"
    input = (5, (10, 18, 20), 12)
    root = create_tree(input)
    c=Counter()
    pre_order(root,c.increment)
    print "Pre_order",c.count

    input = (5, (10, 18, 20), 12)
    root = create_tree(input)
    c=Counter()
    post_order(root,c.increment)
    print "PostOrder",c.count

    input = (5, (10, 18, 20), 12)
    root = create_tree(input)
    c=Counter()
    in_order(root,c.increment)
    print "Inorder", c.count

    print "Finding Balance"
    input = (5, (10, 18, 20), 12)
    root = create_tree(input)
    post_order(root,height)
    pre_order(root,balance)

    print "Depth"
    input = (5, (10, 18, 20), 12)
    root = create_tree(input)
    b=depth()
    pre_order(root,b.find_depth)
    in_order(root,print_node)