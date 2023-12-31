#!/usr/bin/env python3
"""Linked Lists -> Linked List Implementation: Tutorial 2

The goal of this tutorial is to learn how to create a custom singly linked list data structure.
This data structure consists of a collection of nodes which together represent a sequence.
The LinkedList class should contain methods that can be performed on a linked lists:
Those methods include insertion, deletion and traversal.
In this tutorial we will implement only a selection of those methods such as:
insertion, length and traversal

Your task is to:
    * locate the TODOs in this file
    * complete the missing part from the code
    * run the test of this tutorial located in same folder.

To test run LinkedList_t.py in your command line'

Notes:
    * do not change class structure or method signature to not break unit tests
    * visit this url for more information on linked list:
    https://realpython.com/linked-lists-python/
"""
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, data):
        self.data = data

    def setNext(self,next):
        self.next = next

class LinkedList:

    def __init__(self):
        self.first = None
        self.last = None
        self.count = 0

    def __str__(self):
        curr = self.first
        if not curr:
            return "[]"

        string = "["
        while curr:
            string += str(curr.data) + ", "
            curr = curr.next

        return string[:-2] + "]"

    def append(self, item):
        if not self.first:
            self.first = item
        elif not self.last:
            self.last = item
            self.first.next = self.last
        else:
            self.last.next = item
            self.last = self.last.next
        self.count += 1

    def getLen(self):
        return self.count

    def printAll(self):
        print(self)