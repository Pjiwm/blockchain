from linkedlist import LinkedList

list1 = LinkedList()
list2 = LinkedList()
for i in range(11):
    list1.push(i+1)
    list2.push(i+20)
print("o:", list1)
print("o:", list2)

list1.extend(list2)
print(list1)