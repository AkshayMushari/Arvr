class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Add node at the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Print the linked list
    def display(self):
        current = self.head
        if not current:
            print("Linked list is empty.")
            return

        print("Linked List:")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Take dynamic input
linked_list = LinkedList()

print("Enter elements for the linked list (type 'done' to finish):")
while True:
    user_input = input("Enter data: ")
    if user_input.lower() == 'done':
        break
    linked_list.append(user_input)

# Display the final linked list
linked_list.display()


=============================================================
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class BST:
    def __init__(self):
        self.root = None

    # Insert a node into the BST
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, current_node, key):
        if key < current_node.val:
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert(current_node.left, key)
        elif key > current_node.val:
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert(current_node.right, key)
        # If key == current_node.val, do nothing (no duplicates)

    # In-order traversal (left, root, right)
    def inorder(self):
        print("In-order Traversal:")
        self._inorder(self.root)
        print()

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.val, end=' ')
            self._inorder(node.right)

    # Pre-order traversal (root, left, right)
    def preorder(self):
        print("Pre-order Traversal:")
        self._preorder(self.root)
        print()

    def _preorder(self, node):
        if node:
            print(node.val, end=' ')
            self._preorder(node.left)
            self._preorder(node.right)

    # Post-order traversal (left, right, root)
    def postorder(self):
        print("Post-order Traversal:")
        self._postorder(self.root)
        print()

    def _postorder(self, node):
        if node:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.val, end=' ')


# ---- Dynamic Input ----
bst = BST()
print("Enter elements for the Binary Search Tree (type 'done' to finish):")
while True:
    inp = input("Enter number: ")
    if inp.lower() == 'done':
        break
    try:
        num = int(inp)
        bst.insert(num)
    except ValueError:
        print("Please enter a valid integer or 'done' to stop.")

# ---- Traversals ----
bst.inorder()
bst.preorder()
bst.postorder()

=========================================================================
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid  # Target found at index mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Target not found


# ---- Dynamic Input ----
print("Enter sorted integers for the list (type 'done' to finish):")
nums = []
while True:
    inp = input("Enter number: ")
    if inp.lower() == 'done':
        break
    try:
        nums.append(int(inp))
    except ValueError:
        print("Please enter a valid integer or 'done'.")

# Ensure list is sorted (optional if user enters sorted input)
nums.sort()

# Input target to search
try:
    target = int(input("Enter the number to search for: "))
    result = binary_search(nums, target)

    if result != -1:
        print(f"{target} found at index {result}")
    else:
        print(f"{target} not found in the list.")
except ValueError:
    print("Invalid target input.")

======================================================

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        if not self.is_empty():
            item = self.stack.pop()
            print(f"Popped: {item}")
            return item
        else:
            print("Stack is empty.")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty.")
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        print("Stack:", self.stack[::-1])


# Dynamic Input for Stack
stack = Stack()
print("\n=== Stack ===")
print("Commands: push <value>, pop, peek, display, exit")

while True:
    cmd = input(">> ").strip().lower()
    if cmd == 'exit':
        break
    elif cmd.startswith("push "):
        _, val = cmd.split(maxsplit=1)
        stack.push(val)
    elif cmd == "pop":
        stack.pop()
    elif cmd == "peek":
        top = stack.peek()
        if top is not None:
            print("Top element:", top)
    elif cmd == "display":
        stack.display()
    else:
        print("Invalid command.")

======================================

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        if not self.is_empty():
            item = self.queue.pop(0)
            print(f"Dequeued: {item}")
            return item
        else:
            print("Queue is empty.")

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            print("Queue is empty.")
            return None

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        print("Queue:", self.queue)


# Dynamic Input for Queue
queue = Queue()
print("\n=== Queue ===")
print("Commands: enqueue <value>, dequeue, front, display, exit")

while True:
    cmd = input(">> ").strip().lower()
    if cmd == 'exit':
        break
    elif cmd.startswith("enqueue "):
        _, val = cmd.split(maxsplit=1)
        queue.enqueue(val)
    elif cmd == "dequeue":
        queue.dequeue()
    elif cmd == "front":
        front = queue.front()
        if front is not None:
            print("Front element:", front)
    elif cmd == "display":
        queue.display()
    else:
        print("Invalid command.")

============================================

# Longest increasing subseqence 
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for n in nums:
            ind = bisect.bisect_left(dp, n)
            if ind == len(dp):
                dp.append(n)
            else:
                dp[ind] = n
        return len(dp)
