# -*- coding: UTF-8 -*-
# created by Long on 2021/12/9 8:49
# @Software : PyCharm
class TreeNode:  # 定义树
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetrical(self, root: TreeNode) -> bool:
        if not root:  # 空值
            return True
        else:
            return self.auxiliary(root.left, root.right)  # 使用辅助方法检测是否对称
    def auxiliary(self, left_node: TreeNode, right_node: TreeNode):
        if not left_node and not right_node:  # 如果没有左右两枝，返回True
            return True
        elif left_node and right_node:  # 同时存在左右两枝，进一步判断
            if left_node.value == right_node.value:  # 如果两枝值相等，进一步判断子节点是否相等
                return self.auxiliary(left_node.left, right_node.right) and self.auxiliary(left_node.right, right_node.left)
            else:  # 两枝值不相等
                return False
        else:  # 一枝不存在，则不对称
            return False
