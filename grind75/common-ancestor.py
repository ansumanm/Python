import sys


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    path = []
    pathToP = []
    pathToQ = []

    def findTreeNode(self, root: "TreeNode", t: "TreeNode") -> "TreeNode":
        if root is None:
            return None

        # print("findTreeNode: root %d t %d" % (root.val, t.val))
        Solution.path.append(root)
        if root.val == t.val:
            # Found
            return t

        tn = self.findTreeNode(root.right, t)

        if tn is None:
            tn = self.findTreeNode(root.left, t)

        if tn is None:
            Solution.path.pop()

        return tn

    def printPath(self, path: list("TreeNode")):
        for p in path:
            print(p.val, "->")

    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        # Find Path to P
        Solution.path = []

        fNode = self.findTreeNode(root, p)
        if fNode is None:
            return None

        Solution.pathToP = Solution.path

        # Find Path to Q
        Solution.path = []
        fNode = self.findTreeNode(root, q)
        if fNode is None:
            return None

        # Now compare both the paths and find the first element that does not match. The previous element is the common ancestor
        print("##############")
        self.printPath(Solution.pathToP)
        print("--------------")
        self.printPath(Solution.path)

        idx = 0
        while Solution.pathToP[idx].val == Solution.path[idx].val:
            idx += 1
            if idx >= len(Solution.pathToP) or idx >= len(Solution.path):
                break

        idx -= 1
        return Solution.pathToP[idx]


def create_tree(level_order_list):
    if not level_order_list:
        return None

    root = TreeNode(level_order_list[0])
    queue = [root]
    i = 1

    while i < len(level_order_list):
        current_node = queue.pop(0)

        # Assign left child
        if i < len(level_order_list) and level_order_list[i] is not None:
            current_node.left = TreeNode(level_order_list[i])
            queue.append(current_node.left)
        i += 1

        # Assign right child
        if i < len(level_order_list) and level_order_list[i] is not None:
            current_node.right = TreeNode(level_order_list[i])
            queue.append(current_node.right)
        i += 1

    return root


def print_tree(node, level=0):
    if node is not None:
        print_tree(node.right, level + 1)
        print(" " * 4 * level + "->", node.val)
        print_tree(node.left, level + 1)


def main_lca():
    input_list = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
    root = create_tree(input_list)
    print_tree(root)

    s = Solution()
    lca = s.lowestCommonAncestor(root, TreeNode(2), TreeNode(4))
    print("The lca of 2 and 4 is ", lca.val)


def main():
    input_list = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
    # input_list = [6, 2, 8]

    root = create_tree(input_list)
    print_tree(root)

    print("Enter number to find the path:")
    input_data_str = sys.stdin.read()
    input_data = int(input_data_str)

    s = Solution()
    # lca = s.lowestCommonAncestor(root, TreeNode(2), TreeNode(8))
    # print("The lca of 2 and 8 is ", lca.val)
    print("==================================")
    path = s.findTreeNode(root, TreeNode(input_data))
    print("==================================")
    [print(p.val) for p in s.path]


# main()
main_lca()
