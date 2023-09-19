from linkedlist import LinkedList, Sort

# ll = LinkedList()

# ll.push(10)
# ll.push(8)
# ll.push(0)
# ll.push(12)
# ll.push(5)
# ll.push(30)
# ll.push(31)
# ll.push(15)
# print(ll)
# ll.sort(Sort.Ascend)
# print(ll)

# ll.sort(Sort.Descend)
# print(ll)


class Test:
    age = 0
    name = ''

    def __init__(self, age, name):
        self.age = age
        self.name = name

    def bytes(self):
        return bytes(self)


one = Test(10, 'one')
two = Test(20, 'two')

print(one.bytes())
print(two.bytes())