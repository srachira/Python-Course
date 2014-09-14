__author__ = 'SuSh'
from treeutils import*
class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_tree(inorder,preorder):
    if inorder:
        x=inorder.index(preorder[0])
        root=TreeNode(preorder[0])
        root.left=find_tree(inorder[:x],preorder[1:x+1])
        root.right=find_tree(inorder[x+1:],preorder[x+1:])
        return root
    return None

def find_tree1(inorder,postorder):
    if inorder:
        length=len(postorder)
        y=inorder.index(postorder[length-1])
        root=TreeNode(postorder[length-1])
        root.left=find_tree1(inorder[:y],postorder[:y])
        root.right=find_tree1(inorder[y+1:],postorder[y:-1])
        return root
    return None

def find_tree2(inorder,levelorder):
    if len(levelorder):
        for i in levelorder:
            if i in inorder:
                root=TreeNode(i)
                index=inorder.index(i)
                root.left=find_tree2(levelorder[1:],inorder[:index])
                root.right=find_tree2(levelorder[1:],inorder[index+1:])
                return root

if __name__ == "__main__":
    preorder=[10,20,30,40,50,60,70]
    inorder=[20,40,30,50,10,60,70]

    print "InOrder and PreOrder"
    head=find_tree(inorder,preorder)
    pre_order(head,print_node)
    print"\n"

    inorder=[20,40,30,50,10,60,70]
    postorder=[40,50,30,20,70,60,10]
    print "InOrder and PostOrder"
    head=find_tree1(inorder,postorder)
    pre_order(head,print_node)
    print"\n"

    inorder=[20,40,30,50,10,60,70]
    levelorder=[10,20,60,30,70,40,50]
    print "InOrder and LevelOrder"
    head=find_tree2(inorder,levelorder)
    pre_order(head,print_node)
    print"\n"