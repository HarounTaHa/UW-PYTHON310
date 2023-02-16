print("Hello")

age = 42
weight = 2.6

x = 1
print(dir(x))
print(x.bit_length())
print(x.conjugate())

y = -2

print(y.__abs__())

z = x
print(x == z)
print(x is z)

z = y
print(z)

print(y == z)
print(y is z)

print(id(y))
print(id(z))

# del y
# print(y)

print('z', z)

print('-------------------------')

list1 = [[1, 2, 3], ["a", "b"]]

list2 = list1[:]
print(list1)
print(list2)
print(list2 is list1)

list1[0] = [5, 6, 7]

list1[1].append('x')

print(list1)
print(list2)

print(list1[1] is list2[1])
print(id(list1[1]))
print(id(list2[1]))

print('****************')

import copy
list3 = copy.copy(list2)
print(list3)
list2.append(['r', "f"])
list2[0].append(4)
print(list3)
list3 = copy.deepcopy(list2)
print(list3)

