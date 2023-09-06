from linkedlist import LinkedList, Sort

ll = LinkedList()

ll.push(10)
ll.push(8)
ll.push(0)
ll.push(12)
ll.push(5)
ll.push(30)
ll.push(31)
ll.push(15)
print(ll)
ll.sort(Sort.Ascend)
print(ll)

ll.sort(Sort.Descend)
print(ll)
