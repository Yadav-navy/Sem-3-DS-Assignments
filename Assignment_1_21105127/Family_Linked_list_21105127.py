#Linked List Exercise 2: Doubly Linked Lists
class Node(object): 
	def __init__(self, val): 
		self.value = val 
		self.next = None 
		self.prev = None

class DoublyLinkedList(object): 
	def __init__(self): 
		self.head = None
		self.tail = None

	def add_node(self, val): 
		new_node = Node(val)
		#If no head, set new node as head
		if self.head == None: 
			self.head = new_node
			self.tail = new_node
		else: 
			current_node = self.head
			#if next not none (tail) continue traversing
			while current_node.next != None: 
				current_node = current_node.next
			#if tail, add to end
			current_node.next = new_node 
			#set prev pointer to current node
			new_node.prev = current_node
			#set new tail to new node
			self.tail = new_node

	def insert_node_after(self, val, insert_val): 
		if self.head != None: 
			#Create new node
			current_node = self.head 
			new_node = Node(insert_val)
			#If val is first item in list, insert after 
			if self.head.value == val: 
				self.head.next.prev = new_node
				new_node.prev = self.head
				new_node.next = self.head.next
				self.head.next = new_node
			#If tail is val, create new tail
			elif self.tail.value == val: 
				self.tail.next = new_node
				new_node.prev = self.tail
				self.tail = new_node
			else: 
				#If neither head nor tail, traverse through
				while current_node.value != val: 
					current_node = current_node.next 
					#If val is not in list, give error message
					if current_node.value != val: 
						print("Value not in list")
						return False
				#Set new node's next to current node's next 
				new_node.next = current_node.next
				#Insert new node next to current node
				current_node.next = new_node
				#Set new node next prev's pointer to new node
				new_node.next.prev = new_node
				#Set new node's prev pointer to current node 
				new_node.prev = current_node

	def remove_node_from_end(self): 
		if self.head != None: 
			current_node = self.head 
			while current_node.next.next != None: 
				current_node = current_node.next
			current_node.next.prev = None
			current_node.next = None
			self.tail = current_node

	def remove_node(self, val): 
		if self.head != None: 
			current_node = self.head 
			#If val is the head 
			if self.head.value == val: 
				self.head.next.prev = None
				self.head = self.head.next
			#If val is the tail
			elif self.tail.value == val: 
				self.tail.prev.next = None
				self.tail = self.tail.prev
			else: 
				while current_node.next.value != val: 
					current_node = current_node.next 
					#If val is not in list 
					if current_node.next.value != val: 
						print("Value not in list")
						return False
				#Set next next node's prev pointer to current node
				current_node.next.next.prev = current_node 
				#Set next node to current's next next pointer
				current_node.next = current_node.next.next

	def display(self): 
		#Create empty list
		value_list = []
		if self.head != None: 
			current_node = self.head 
			#Start at head and check if next is not tail
			while current_node.next != None: 
				#Add current node to list and traverse forward
				value_list.append(current_node.value)
				current_node = current_node.next 
			value_list.append(current_node.value)
			print(value_list)
		else: 
			print("No nodes")
			return False

dll = DoublyLinkedList()
dll.add_node('Navneet')
dll.display()
dll.add_node(19)
dll.display()
dll.add_node('who is the son of')
dll.display()
dll.add_node('Om Parkash')
dll.display()
dll.add_node(60)
dll.display()
dll.add_node('who is the father of')
dll.display()
dll.add_node('Amit')
dll.display()
dll.add_node(30)
dll.display()
dll.add_node('who is the Brother of ')
dll.display()
dll.add_node('Nikesh')
dll.display()
dll.add_node(20)
# dll.display()
# dll.add_node(99)
# dll.add_node(1000)
# dll.add_node("The list is linked")
dll.display()

"""
Q.Try to find a way to link the family members' doubly-linked list based on their relationship.
Ans.One way to link the family members doubly-linked list is by sorting the doubly linked list according to age in decending order.
By doing so we will get a doubly linked list in which older generation people will be close to head in double linked list and new
generation people will be close to tail in doubly linked list.
*/

"""
