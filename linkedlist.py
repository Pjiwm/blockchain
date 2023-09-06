from __future__ import annotations
from enum import Enum

class LinkedList:

    def __init__(self):
        self.__head = None
        self.__tail = None

    def __str__(self):
        curr = self.__head
        if not curr:
            return "[]"

        string = "["
        while curr:
            string += str(curr.value) + ", "
            curr = curr.next

        return string[:-2] + "]"

    def clear(self):
        self.__head = None
        self.__tail = None

    def contains(self, value):
        curr = self.__head
        while curr:
            if curr.value == value:
                return True
            curr = curr.next
        return False

    def extend(self, other: LinkedList):
        self.__tail.next = other.__head
        self.__tail = other.__tail

    def find(self, value):
        idx = 0
        curr = self.__head
        while curr:
            if curr.value == value:
                return idx
            curr = curr.next
            idx += 1
        return None

    def get(self, idx):
       if not self.__head: return None
       node = self.__head.get_node(idx, 0)
       return node.value if node else None

    def head(self):
        return self.__head.value if self.__head else None

    def is_empty(self):
        return not self.__head

    def pop(self):
        # If the list is just a head, or head or tail, values gotta be set to None
        if not self.__tail:
            self.__head = None
        elif self.__head.next == self.__tail:
            self.__tail = None
            self.__head.next = None
        else:
            self.__tail.prev.next = None
            self.__tail = self.__tail.prev

    def pop_head(self):
        if not self.__tail:
            self.__head = None
        elif self.__head.next == self.__tail:
            self.__head = self.__tail
            self.__tail = None
            self.__head.prev = None
        else:
            self.__head = self.__head.next
            self.__head.prev = None

    def push(self, value):
        if not self.__head:
            self.__head = Node(value, None)
        elif not self.__tail:
            self.__tail = Node(value, self.__head)
            self.__head.next = self.__tail
        else:
            self.__tail.next = Node(value, self.__tail)
            self.__tail = self.__tail.next

    def push_first(self, value):
        if not self.__head:
            self.__head = Node(value, None)
        prev = self.__head
        self.__head = Node(value, None)
        self.__head.next = prev

    def remove(self, idx):
        node = self.__head.get_node(idx, 0)
        if not node: return
        # Removing the head is tricky, because we gotta assign a new head.
        # For tail this is no issue, since it's the last node it shares the same logic as the pop method.
        if node == self.__tail:
            self.pop()
        elif node == self.__head:
            self.pop_head()
        else:
            prev = node.prev
            prev.next = node.next
            node.next.prev = prev

    def set(self, idx, value):
        node = self.__head.get_node(idx, 0)
        if not node: return
        node.value = value

    def sort(self, sort: Sort):
        curr = self.__head
        is_sorted = True
        while True:
            if not curr.next:
                if is_sorted:
                    return
                else:
                    curr = self.__head
                    is_sorted = True

            if curr.value > curr.next.value and sort == Sort.Ascend:
                stored = curr.value
                curr.value = curr.next.value
                curr.next.value = stored
                is_sorted = False
            elif curr.value < curr.next.value and sort == Sort.Descend:
                stored = curr.value
                curr.value = curr.next.value
                curr.next.value = stored
                is_sorted = False
            curr = curr.next

    def tail(self):
        return self.__tail.value if self.__tail else None


class Node:

    def __init__(self, value, prev):
        self.value = value
        self.prev = prev
        self.next = None

    def get_node(self, idx, depth):
        if idx == depth: return self
        next = self.next
        return next.get_node(idx, depth+1) if next else None


class Sort(Enum):
    Ascend = 0
    Descend = 1