# -*- coding: UTF-8 -*-


class TreeNode:
    a = 0  # 变量是一个类变量，它的值将在这个类的所有实例之间共享。你可以在内部类或外部类使用 TreeNode.empCount 访问。

    def __init__(self, val):  # 第一种方法__init__()方法是一种特殊的方法，被称为类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法
        self.val = val        # self 代表类的实例，self 在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数。
        self.left = None      # 类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。
        self.right = None

    def display(self):
        print("val : ", self.val)
        if self.left is not None:
            self.left.display()


def insert(root, val):
    if root is None:
        root = TreeNode(val)
    else:
        if val < root.val:
            root.left = insert(root.left, val)   #递归地插入元素
        elif val > root.val:
            root.right = insert(root.right, val)
    return root


def query(root, val):   # 找得到返回1 罢了
    if root is None:
        return
    if root.val is val:
        return 1
    if root.val < val:
        return query(root.right, val)  #递归地查询
    else:
        return query(root.left, val)


def findmin(root):
    if root.left:
        return findmin(root.left)
    else:
        return root


def delnum(root, val):
    if root is None:
        return
    if val < root.val:
        return delnum(root.left, val)
    elif val > root.val:
        return delnum(root.right, val)
    else:                                         # 删除要区分左右孩子是否为空的情况
        if root.left and root.right:

            tmp = findmin(root.right)              # 找到后继结点
            root.val = tmp.val
            root.right = delnum(root.right, val)  # 实际删除的是这个后继结点

        else:
            if root.left is None:
                root = root.right
            elif root.right is None:
                root = root.left
    return root


def abc(a):
    return -a
# 測试代码
root = TreeNode(3)
root = insert(root, 2)
root = insert(root, 1)
root = insert(root, 4)
root.display()
print(root.val)
print(root.val)

print(query(root, 3))
print(query(root, 1))
root = delnum(root, 1)
print(query(root, 1))
