class Node:
    def __init__(self, key: int, p = None, l = None, r = None, h = 1):
        self.left = l
        self.right = r
        self.parent = p
        self.value = key
        self.height = h

class Tree:
    def __init__(self, key):
        self.root = Node(key)
def left_rotate(T: Tree, x: Node):
    y = x.right
    x.right = y.left
    if y.left:
        y.left.parent = x
    y.parent = x.parent
    if not x.parent:
        T.root = y
    elif x == x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y
    y.left = x
    x.parent = y
def right_rotate(T: Tree, y: Node):
    x = y.left
    y.left = x.right
    if x.right:
        x.right.parent = y
    x.parent = y.parent
    if not y.parent:
        T.root = x
    elif y == y.parent.left:
        y.parent.left = x
    else:
        y.parent.right = x
    x.right = y
    y.parent = x
def avl_insert(T: Tree, key: int):
    cur, cur_p = T.root, None
    while cur:
        cur_p = cur
        if key == cur.value:
            print("The given key already exists:", key)
            return
        elif key < cur.value:
            cur = cur.left
        else:
            cur = cur.right
    new_node = Node(key, cur_p)
    if not cur_p:
        T.root = new_node
    elif key < cur_p.value:
        cur_p.left = new_node
    else:
        cur_p.right = new_node
    avl_fixup(T, new_node)

def avl_fixup(T: Tree, z: Node):
    if z is None:
        return
    original_height = z.height
    while z and z.height != original_height:
        original_height = z.height

        update_height(z)
        balance_factor = get_balance_factor(z)
        if balance_factor > 1:
            if get_balance_factor(z.left) < 0:
                left_rotate(T, z.left)
            right_rotate(T, z)
        elif balance_factor < -1:
            if get_balance_factor(z.right) > 0:
                right_rotate(T, z.right)
            left_rotate(T, z)
        z = z.parent
    update_height(T.root)

    ## You may add more helper functions ##
def update_height(node: Node):
    if node:
        node.height = 1 + max(node.left.height if node.left else 0, node.right.height if node.right else 0)
def get_balance_factor(node: Node):
    return find_height(node.left) - find_height(node.right)
def find_height(node: Node):
    if node:
        return node.height
    return 0
def avl_delete(T: Tree, key: int):
    node_to_delete = find_node(T.root, key)
    if node_to_delete is None:
        print("Key not found:", key)
        return
    parent_of_deleted_node = node_to_delete.parent
    if node_to_delete.left is None or node_to_delete.right is None:
        delete_node_simple(T, node_to_delete)
        node = parent_of_deleted_node
    else:
        successor = find_successor(node_to_delete)
        node_to_delete.value = successor.value
        delete_node_simple(T, successor)
        node = successor.parent
    if node:
        avl_fixup(T, node)

def find_node(root: Node, key: int) -> Node:
    if root is None or root.value == key:
        return root
    if key < root.value:
        return find_node(root.left, key)
    return find_node(root.right, key)

def find_successor(node: Node) -> Node:
    successor = node.right
    while successor and successor.left:
        successor = successor.left
    return successor

def delete_node_simple(T: Tree, node: Node):
    if node.left is None and node.right is None:
        if node.parent is None:
            T.root = None
        elif node == node.parent.left:
            node.parent.left = None
        else:
            node.parent.right = None
    elif node.left is None:
        if node.parent is None:
            T.root = node.right
        elif node == node.parent.left:
            node.parent.left = node.right
        else:
            node.parent.right = node.right
        if node.right:
            node.right.parent = node.parent
    elif node.right is None:
        if node.parent is None:
            T.root = node.left
        elif node == node.parent.left:
            node.parent.left = node.left
        else:
            node.parent.right = node.left
        if node.left:
            node.left.parent = node.parent
    if node.parent:
        avl_fixup(T, node.parent)


###################################
### Below are sample functions for testing.
### You may add more test cases.
###################################
def printBST(tree: Tree):
    print_helper(tree.root, 1)
def print_helper(root: Node, depth: int):
    tab = " "*(depth*5)
    if not root:
        print(tab, "None")
        return
    print_helper(root.right, depth + 1)
    print(tab + str(root.value) + "(" + str(root.height) + ")")
    print_helper(root.left, depth + 1)
def arrayToBST(nums: list[int]):
    tree = Tree(nums[0])
    for n in nums[1:]:
        avl_insert(tree, n)
        printBST(tree)
        print("-----------------------------------------------")
    return tree
tree = arrayToBST([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
avl_delete(tree, 3)
printBST(tree)
print("-----------------------------------------------")
avl_delete(tree, 1)
printBST(tree)
print("-----------------------------------------------")
avl_delete(tree, 10)
printBST(tree)




tree = arrayToBST([20, 15, 25, 10, 18, 22, 30, 5, 12, 17, 19, 28, 35])

print("Initial AVL Tree:")
printBST(tree)
print("-----------------------------------------------")

avl_delete(tree, 15)
print("AVL Tree after deleting node with key 15:")
printBST(tree)
print("-----------------------------------------------")

avl_delete(tree, 20)
print("AVL Tree after deleting node with key 20:")
printBST(tree)
print("-----------------------------------------------")

avl_delete(tree, 25)
print("AVL Tree after deleting node with key 25:")
printBST(tree)




def minimumRemoval(activities):
    def greedy_activity_selector(s, f, n):
        A = [0]
        k = 0
        for m in range(1, n):
            if s[m] >= f[k]:
                A.append(m)
                k = m
        return A
    activities.sort(key=lambda x: x[1])
    start_times = [activity[0] for activity in activities]
    finish_times = [activity[1] for activity in activities]
    selected_activities = greedy_activity_selector(start_times, finish_times, len(activities))
    removals = len(activities) - len(selected_activities)
    return removals


# Test cases
print(minimumRemoval(
    [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]))  # Output: 7
print(minimumRemoval([(1, 2), (2, 3), (3, 4), (1, 3)]))  # Output: 1
print(minimumRemoval([(1, 2), (1, 2), (1, 2)]))  # Output: 2
print(minimumRemoval([(1, 2), (2, 3)]))  # Output: 0
print(minimumRemoval([(0, 1), (0, 1), (0, 1)]))  # Output: 2
print(minimumRemoval([(0, 1), (1, 2)]))  # Output: 0




