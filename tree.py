from typing import Union


class Node(object):
    def __init__(self, data) -> None:
        self.data = data
        self.left: Union[Node, None] = None
        self.right: Union[Node, None] = None

    def __str__(self) -> str:
        return str(self.data)


class Tree(object):
    def __init__(self) -> None:
        self.root = None

    def add(self, data):
        node = Node(data)
        # 如果二叉树为空，那么添加的点将插入 root 节点处
        if self.root is None:
            self.root = node
        else:
            # 在 q 列表中，添加二叉树的根节点
            q = [self.root]
            while True:
                pop_node = q.pop(0)
                # 左子树为空则将点添加到左子树
                if pop_node.left is None:
                    pop_node.left = node
                    return
                # 右子树为空则将点添加到右子树
                elif pop_node.right is None:
                    pop_node.right = node
                    return
                # 把左右后继节点进队列，随后取出“左”后继节点
                else:
                    q.append(pop_node.left)
                    q.append(pop_node.right)

    def get_parent(self, data) -> Union[Node, None]:
        if self.root.data == data:
            # 根节点没有父节点
            return None
        # 在 tmp 列表中，添加二叉树的根节点
        tmp = [self.root]
        while tmp:
            pop_node = tmp.pop(0)
            # 如果点的左子树为要寻找的点
            if pop_node.left and pop_node.left.data == data:
                # 返回这个点，即为寻找点的父节点
                return pop_node
            # 如果点的右子树为要寻找的点
            if pop_node.right and pop_node.right.data == data:
                # 返回这个点，即为寻找点的父节点
                return pop_node
            # 添加 tmp 列表里的元素
            if pop_node.left is not None:
                tmp.append(pop_node.left)
            if pop_node.right is not None:
                tmp.append(pop_node.right)
        return None

    def delete(self, data) -> bool:
        # 如果根为空，就什么也不做
        if self.root is None:
            return False

        parent = self.get_parent(data)
        if parent:
            # 确定待删除节点
            del_node = parent.left if parent.left.data == data else parent.right
            # 待删除节点的左子树为空时
            if del_node.left is None:
                # 如果待删除节点是父节点的左孩子
                if parent.left.data == data:
                    parent.left = del_node.right
                # 如果待删除节点是父节点的右孩子
                else:
                    parent.right = del_node.right
                # 删除变量 del_node
                del del_node
                return True
            # 待删除节点的右子树为空时
            elif del_node.right is None:
                # 如果待删除节点是父节点的左孩子
                if parent.left.data == data:
                    parent.left = del_node.left
                # 如果待删除节点是父节点的右孩子
                else:
                    parent.right = del_node.left
                # 删除变量 del_node
                del del_node
                return True
            # 左右子树都不为空时
            else:
                tmp_pre = del_node
                # 待删除节点的右子树
                tmp_next = del_node.right
                # 寻找待删除节点右子树中的最左叶子节点并完成替代
                if tmp_next.left is None:
                    # 替代
                    tmp_pre.right = tmp_next.right
                    tmp_next.left = del_node.left
                    tmp_next.right = del_node.right
                else:
                    # 让 tmp_next 指向右子树的最左叶子节点
                    while tmp_next.left:
                        tmp_pre = tmp_next
                        tmp_next = tmp_next.left
                    # 替代
                    tmp_pre.left = tmp_next.right
                    tmp_next.left = del_node.left
                    tmp_next.right = del_node.right
                # 如果待删除节点是父节点的左孩子
                if parent.left.data == data:
                    parent.left = tmp_next
                # 如果待删除节点是父节点的右孩子
                else:
                    parent.right = tmp_next
                del del_node
                return True
        else:
            return False

    def inorder(self, node: Node) -> list:
        """
        中序遍历
        左中右
        """
        if node is None:
            return []
        result = [node.data]
        left_data = self.inorder(node.left)
        right_data = self.inorder(node.right)
        return left_data + result + right_data

    def preorder(self, node: Node) -> list:
        """
        前序遍历
        中左右
        """
        if node is None:
            return []
        result = [node.data]
        left_data = self.preorder(node.left)
        right_data = self.preorder(node.right)
        return result + left_data + right_data

    def postorder(self, node: Node) -> list:
        """
        后序遍历
        左右中
        """
        if node is None:
            return []
        result = [node.data]
        left_data = self.postorder(node.left)
        right_data = self.postorder(node.right)
        return left_data + right_data + result


if __name__ == '__main__':
    t = Tree()
    for i in range(1, 11):
        t.add(i)
    print('中序遍历:', t.inorder(t.root))
    print('前序遍历:', t.preorder(t.root))
    print('后序遍历:', t.postorder(t.root))
