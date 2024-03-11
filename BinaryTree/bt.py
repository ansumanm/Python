"""
Binary tree.
"""

from typing import Tuple, List

"""
For Tree to List problem
"""
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        newNode = ListNode(value)

        # Insert into list
        if self.head is None:
            self.head = newNode
        else:
            # Insert at front
            newNode.next = self.head
            self.head = newNode

    def walk(self) -> List[ListNode]:
        result = []
        node = self.head
        while node:
            result.append(node.value)
            node = node.next

        return result


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        newNode = TreeNode(value)
        if self.root is None:
            self.root = newNode
        else:
            self._insert_recursive(self.root, newNode)

    def delete(self, value):
        # Find the node containing value and delete it.
        # Logic is complex.
        pass

    def _insert_recursive(self, node: TreeNode, newNode):
        if newNode.value < node.value:
            if node.left is None:
                node.left = newNode
                newNode.parent = node
            else:
                self._insert_recursive(node.left, newNode)
        elif newNode.value > node.value:
            if node.right is None:
                node.right = newNode
                newNode.parent = node
            else:
                self._insert_recursive(node.right, newNode)
        else:
            # value already exists
            pass

    def inorder_traversal(self, node, result=None):
        if result is None:
            result = []

        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.value)
            self.inorder_traversal(node.right, result)

        return result

    def preorder_traversal(self, node, result=None):
        if result is None:
            result = []

        if node:
            result.append(node.value)
            self.preorder_traversal(node.left, result)
            self.preorder_traversal(node.right, result)

        return result

    def postorder_traversal(self, node, result=None):
        if result is None:
            result = []

        if node:
            self.postorder_traversal(node.left, result)
            self.postorder_traversal(node.right, result)
            result.append(node.value)

        return result
    
    def level_order_traversal(self, node, result=None):
        queue = list()
        if result is None:
            result = []

        queue.append(node)

        while(queue):
            node = queue.pop(0)
            result.append(node.value)

            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)

        return result


    def copy_binary_tree(self, node: TreeNode) -> TreeNode:
        if node is None:
            return None

        copyNode = TreeNode(node.value)

        copyNode.left = self.copy_binary_tree(node.left)
        copyNode.right = self.copy_binary_tree(node.right)

        return copyNode

    def is_tree_equal(
        self, rootNode1: TreeNode, rootNode2: TreeNode, result=True
    ) -> bool:
        if rootNode1 is None and rootNode2 is None:
            return True

        if rootNode1 is not None and rootNode2 is None:
            return False

        if rootNode1 is None and rootNode2 is not None:
            return False

        if rootNode1.value != rootNode2.value:
            return False

        result = result and self.is_tree_equal(rootNode1.left, rootNode2.left, result)
        result = result and self.is_tree_equal(rootNode1.right, rootNode2.right, result)

        return result

    def mirror_tree(self, node: TreeNode) -> TreeNode:
        if node is None:
            return None

        newNode = TreeNode(node.value)
        newNode.left = self.mirror_tree(node.right)
        newNode.right = self.mirror_tree(node.left)

        return newNode

    def find_path_between_two_nodes(
        self, fromNode: TreeNode, toNode: TreeNode
    ) -> List[TreeNode]:
        """
        Use BFS to find the path.
        """
        # Simulate a FIFO using list
        queue = [[fromNode]]

        while queue:
            # print("**************")
            # for path in queue:
            #     for node in path:
            #         print(node.value)

            # Evaluate one path at a time until we reach the destination Node.
            path = queue.pop(0)

            curNode = path[-1]  # Last Node.

            if curNode.value == toNode.value:
                # We got our path. Stop processing and return it.
                return path
            else:
                if curNode.right and curNode.right not in path:
                    rightPath = list(path)
                    rightPath.append(curNode.right)
                    queue.append(rightPath)

                if curNode.left and curNode.left not in path:
                    leftPath = list(path)
                    leftPath.append(curNode.left)
                    queue.append(leftPath)

                if curNode.parent and curNode.parent not in path:
                    parentPath = list(path)
                    parentPath.append(curNode.parent)
                    queue.append(parentPath)

    def find_node(self, node: TreeNode, val: int) -> TreeNode:
        if node is None:
            return None
        elif node.value == val:
            return node
        elif node.value > val:
            return self.find_node(node.left, val)
        elif node.value < val:
            return self.find_node(node.right, val)

    def find_path(self, fromVal: int, toVal: int) -> List[TreeNode]:
        # Find the fromNode
        fromNode = self.find_node(self.root, fromVal)
        toNode = self.find_node(self.root, toVal)

        print(f"fromNode: {fromNode.value} toNode: {toNode.value}")

        if fromNode is None or toNode is None:
            return None

        path = self.find_path_between_two_nodes(fromNode, toNode)

        return path
    
    def find_depth(self, node: TreeNode, depth=0, path=None) -> Tuple[int, List[TreeNode]]:
        if path is None:
            # If path is uninitialized, initialize it with the current node
            path = [node]
        
        # print(f"Node val: {node.value} depth: {depth} path: {[node.value for node in path]}")

        if node.right is None and node.left is None:
            return depth, path
        
        depthLeft = 0
        depthRight = 0
        pathRight = list(path)
        pathLeft = list(path)

        if node.right:
            pathRight.append(node.right)
            depthRight, pathRight = self.find_depth(node.right, depth + 1, pathRight)

        if node.left:
            pathLeft.append(node.left)
            depthLeft, pathLeft = self.find_depth(node.left, depth + 1, pathLeft)

        if depthRight >= depthLeft:
            return depthRight, pathRight
        else:
            return depthLeft, pathLeft
        
    def tree_to_list(self, list: LinkedList) -> None:
        self._tree_to_list_recursive(self.root, list)

    def _tree_to_list_recursive(self, treeNode: TreeNode, list: LinkedList):
        if treeNode is None:
            return
        
        list.insert(treeNode.value)
        self._tree_to_list_recursive(treeNode.left, list)
        self._tree_to_list_recursive(treeNode.right, list)
        del treeNode


if __name__ == "__main__":
    bt = BinaryTree()

    bt.insert(5)
    bt.insert(4)
    bt.insert(6)
    bt.insert(2)
    bt.insert(1)
    bt.insert(3)
    bt.insert(7)
    bt.insert(6)
    bt.insert(8)
    bt.insert(9)

    print("========== Tree traversal =============")
    print("Inorder: ", bt.inorder_traversal(bt.root))
    print("Preorder: ", bt.preorder_traversal(bt.root))
    print("Postorder: ", bt.postorder_traversal(bt.root))
    print("=========== Tree copying =============")
    copyTree = bt.copy_binary_tree(bt.root)
    print("copyTree Inorder: ", bt.inorder_traversal(copyTree))
    print("copyTree Preorder: ", bt.preorder_traversal(copyTree))
    print("copyTree Postorder: ", bt.postorder_traversal(copyTree))
    print("========= Check if two trees are equal ============")
    result = bt.is_tree_equal(bt.root, copyTree)
    if result:
        print("Two Trees are equal.")
    else:
        print("Two trees are not equal.")

    mirrorTree = bt.mirror_tree(bt.root)
    print("========== Mirror Tree ==============")
    print("Inorder traversal: ", bt.inorder_traversal(mirrorTree))
    print("Preorder traversal: ", bt.preorder_traversal(mirrorTree))
    print("Postorder traversal: ", bt.postorder_traversal(mirrorTree))

    print("===== Find path =====")
    print("Path between 4 and 8:", [node.value for node in  bt.find_path(4, 8)])
    print("Path between 6 and 8:", [node.value for node in  bt.find_path(6, 8)])
    print("Path between 6 and 8:", [node.value for node in  bt.find_path(6, 8)])
    print("Path between 8 and 1:", [node.value for node in  bt.find_path(8, 1)])
    print("Path between 3 and 1:", [node.value for node in  bt.find_path(3, 1)])
    print("Path between 1 and 3:", [node.value for node in  bt.find_path(1, 3)])

    print("====== Level order traversal =====")
    print(bt.level_order_traversal(bt.root))

    print("====== Depth =====================")
    depth, path = bt.find_depth(bt.find_node(bt.root, 2))
    print("Depth of node 2: ", depth, [node.value for node in path])
    depth, path = bt.find_depth(bt.root)
    print("Depth of node 5: ", depth, [node.value for node in path])

    ll = LinkedList()
    bt.tree_to_list(ll)
    print(ll.walk())


#     print(
#         """
# Diameter of a tree: The diameter (or sometimes called the width) of a tree
# is the length of the longest path between any two nodes in the tree.
# This path may or may not pass through the root.
#         """
#    )
