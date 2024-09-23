##1 mutliple sorted lists into one sorted list

import heapq
##empty list, created heap, for each array add tuple to heap, last transform for heap
def sort(lists):
	sorted_list = []
	heap = [(array[0], array) for array in lists]
	heapq.heapify(heap)
##create loop, pop smallest number from each heap, returns tuple put ito two variables
	while heap:
		smallest_number, new_array = heapq.heappop(heap)
##with append add smallest number to sorted list
		sorted_list.append(smallest_number)
##remove first element
		new_array.pop(0)
##if numbers left, add new first number to heap
		if new_array:
			heapq.heappush(heap, (new_array[0], new_array))
##return ew sorted list
	return sorted_list
##test cases
print(sort([[1]]))  # returns [1]
print(sort([[2], [1]]))  # returns [1, 2]
print(sort([[2, 3, 3, 4], [1, 5], [1, 2, 4]]))  # returns [1, 1, 2, 2, 3, 3, 4, 4, 5]
print(sort([[10, 100], [1, 1, 1], [1, 1000]]))  # returns [1, 1, 1, 1, 10, 100, 1000]
print(sort([[1,5,6], [2,2,999], [5,7,7,10]]))   # returns [1,2,2,5,5,6,7,7,10,999]

##2 returning kthlargest element in all lists

import heapq
##define a and k, flatten lists into one,
def k_largest(A, k):
	combined_lists = [num for sublist in A for num in sublist]
##create a heap with first item
	heap = combined_lists[:k]
	heapq.heapify(heap)
##replace each item in the heap if larger tahn smallest replace
	for num in heap:
		if num > heap[0]:
			heapq.heapreplace(heap, num)

	return heap[0]
##test cases
print(k_largest([[1]], 1)) # returns 1
print(k_largest([[2], [1]], 2)) # returns 1
print(k_largest([[2, 3, 3, 4], [1, 5], [1, 2, 4]], 4)) # returns 3
print(k_largest([[10, 100], [1, 1, 1], [1, 1000]], 7)) # returns 1



##3 kth largest in binary search tree

class Node:
	def __init__(self, key: int):
		self.left = None
		self.right = None
		self.value = key

def k_largest_bst(root: Node, k: int):
##create empty stack, set current node to root
	stack = []
	curr = root
##remember create loop, inner loop goes through tree starting from the root to right child
##since right child larger in bst, add back to the stack
	while True:
		while curr is not None:
			stack.append(curr)
			curr = curr.right
##no more right children then pop top node from stack
		else:
			curr = stack.pop()
			k = k - 1
##once k is 0 found kth largest, return value
		if k == 0:
			return curr.value
##then set current node to compare ot left child and subtree
		curr = curr.left
##test case
##remember create tree left ot right
n1 = Node(41)
n2 = Node(20)
n3 = Node(65)
n4 = Node(11)
n5 = Node(29)
n6 = Node(50)
n7 = Node(91)
n8 = Node(32)
n9 = Node(72)
n10 = Node(99)

##make children
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
n5.right = n8
n7.left = n9
n7.right = n10
##call function
print(k_largest_bst(n1,4)) #should return 65