#!/usr/bin/env python3
"""Linked List -> Extended Linked List Implementation: Homework

The goal of this homework is to implement a singly linked list data structure with additional functionalities.
In previous tutorials you have learned how a node and a linked list data structure in its basic form can be created.
However, a LinkedList class can have more methods to perform additional operations on a linked list,
such as: insertion (begin, end, or after a specific element), deletion, traversal, and sorting.

Your task is to:
    * locate the TODOs in this file
    * complete the missing part from the code
    * run the test of this homework located in same folder.

To test run LinkedList_t.py in your command line'

Notes:
    * do not change class structure or method signature to not break unit tests
    * visit this url for more information on linked list:
    https://realpython.com/linked-lists-python/
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        curr = self.head
        string = ""
        while curr:
            string += str(curr.data) + "\n"
            curr = curr.next

        return string[:-1]

    #TODO 1: Insert at the beginning of the list
    def insertBeg(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    #TODO 2: Insert at the end
    def insertEnd(self, new_data):
        if not self.head:
            self.head = Node(new_data)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = Node(new_data)

    #TODO 3: Insert after a specific node
    def insertAfter(self, data, new_data):
        curr = self.head
        while curr:
            if curr.data == data:
                next = curr.next
                curr.next = Node(new_data)
                curr.next.next = next
                return
            curr = curr.next

    #TODO 4: Deleting a node at a specific index
    def deleteIndex(self, index):
        idx = 0
        curr = self.head
        last = None
        while curr:
            if idx == index:
                last.next = curr.next
                return

            last = curr
            curr = curr.next
            idx += 1
        raise ValueError("Index out of bounds")

    #TODO 5: Search an element
    def find(self, key):
        idx = 0
        curr = self.head
        while curr:
            if curr.data == key:
                return idx
            curr = curr.next
            idx += 1
        return -1

    #TODO 6: Sort the linked list
    def sort(self, head):
        # Bubble sort
        curr = self.head
        is_sorted = True
        while True:
            if not curr.next:
                if is_sorted:
                    return
                else:
                    curr = self.head
                    is_sorted = True
            if curr.data > curr.next.data:
                stored = curr.data
                curr.data = curr.next.data
                curr.next.data = stored
                is_sorted = False
            curr = curr.next

    #TODO 7: Print the linked list
    def printList(self):
        print(self)