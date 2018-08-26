# encoding: utf-8


class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

    # 迭代读值
    def get_post_order_tranverse(self, list):
        if self.data is not None:
            if self.left is not None:
                self.left.get_post_order_tranverse(list)

            if self.right is not None:
                self.right.get_post_order_tranverse(list)
            # print(self.data)
            list.append(self.data)

    # Lowest Common Ancestor of a Binary Tree
    def LowestParent(self, root, p, q):
        stack = [root]
        par_child = {root.data: None}
        while stack:
            node = stack.pop()
            if node.left:
                par_child[node.left.data] = node.data
                stack.append(node.left)
            if node.right:
                par_child[node.right.data] = node.data
                stack.append(node.right)
        res = set()
        while p:
            res.add(p)
            p = par_child[p]
        while q not in res:
            q = par_child[q]
        return q


def construct_tree(pre_order, mid_order):
    # 忽略参数合法性判断
    if len(pre_order) == 0:
        return None
    # 前序遍历的第一个结点一定是根结点
    root_data = pre_order[0]
    for i in range(0, len(mid_order)):
        if mid_order[i] == root_data:
            break
    # 递归构造左子树和右子树
    left = construct_tree(pre_order[1: 1 + i], mid_order[:i])
    right = construct_tree(pre_order[1 + i:], mid_order[i + 1:])
    return Node(root_data, left, right)


def get_closest_parent(node1, node2):
    return


if __name__ == '__main__':
    preOrderTraverse = [1, 2, 4, 7, 3, 5, 8, 9, 6]
    midOrderTraverse = [4, 7, 2, 1, 8, 5, 9, 3, 6]
    tree_a = construct_tree(preOrderTraverse, midOrderTraverse)
    postOrderTraverse = []
    tree_a.get_post_order_tranverse(postOrderTraverse)
    print(postOrderTraverse)
    tree_a = tree_a.LowestParent(tree_a, 6, 8)

    print(tree_a)

