import pathlib

all_letters = "thequickbrownfoxjumpedoverthelazydog"
print(min(all_letters))
print(max(all_letters))

all_letters = "thequickbrownfoxjumpedoverthelazydog"
print(all_letters.count('o'))
print(all_letters.count('the'))
print(all_letters.count('A'))
all_number = [0, 0, 0, 12, 14, 1452]
print(all_number.count(145))

_list = list(range(10))
print(_list)
for x in range(10):
    print(x)
l = [x for x in range(10)]
print(l)


def add_one(x):
    return x + 1


a = list(map(add_one, range(10)))

print(a)


def filter_ods(x):
    return x % 2


for x in range(10):
    if filter_ods(x):
        print(x)

b = [x for x in range(10) if filter_ods(x)]
print(b)

b = list(filter(filter_ods, range(10)))
print(b)
print(sum(b))

s = "this is a string"
print(s[0] == 't')
print(s[5] == 'i')

a = "a bunch of words"
s = "a bunch of words"
print(a is s)

"""
    Tuples
"""
#
# name = 'Brian'
# other = name
# a = (1, 2, name)
# b = (3, 4, other)
# for i in range(3):
#     print(a[i] is b[i], end=' ')

"""
Lists Are Mutable
"""
food = ['spam', 'eggs', 'ham']
print(food)
food[1] = 'raspberries'
print(food)

original = [1, 2, 3]
altered = original
for i in range(len(original)):
    if True:
        altered[i] += 1

print(altered)
print(original)

bins = [[]] * 5
print(bins)

words = ['one', 'three', 'rough', 'sad', 'goof']
# loop five times
for i in range(5):
    # add a word to the corresponding bin
    print(i)
    bins[i].append(words[i])

print(bins)

bins = []
for i in range(5):
    bins.append([])

# loop five times
for i in range(5):
    bins[i].append(words[i])

print(bins)

"""
    Bad way
"""


def accumulator(count, ac_list=[]):
    for i in range(count):
        ac_list.append(i)
    return ac_list


"""
    Good way
"""


def accumulator(count, ac_list=None):
    if ac_list is None:
        ac_list = []
    for i in range(count):
        ac_list.append(i)
    return ac_list


print(accumulator(5))
print(accumulator(7))

"""
Growing the List
.append(), .insert(), .extend()
"""
food = ['spam', 'eggs', 'ham']
food.append('sushi')
print(food)

food.insert(0, 'beans')
print(food)

food.extend(['bread', 'water'])
print(food)

food.extend('spaghetti')
print(food)

"""
Shrinking a List
.pop(), .remove()

"""

food = ['spam', 'eggs', 'ham', 'toast']
food.pop()
print(food)

food.pop(0)
print(food)

food.remove('ham')
print(food)

nums = range(10)
print(nums)
# del nums[1:6:2]

food = ['spam', 'eggs', 'ham', 'toast']
food2 = food[:]
print(food2)
print(food is food2)
food2[1] = 'haroun'
print(food2)
print(food)

l = list(range(10))
for item in l:
    print(l)
    l.remove(item)
print(l)

l = list(range(10))
for item in l[:]:
    l.remove(item)
print(l)

"""
Miscellaneous List Methods
.reverse()
.sort()
"""
food = ['spam', 'eggs', 'ham']
food.reverse()
print(food)
food.sort()
print(food)


def third_letter(string):
    return string[2]


"""
You end up with the list sorted by the third letter in each element.

"""
food.sort(key=third_letter)
print(food)

"""
Other Considerations
Do you need to do the same operation to each element?
list
Is there a small collection of values which make a single logical item?
tuple
Do you want to document that these values won't change?
tuple
Do you want to build it iteratively?
list
Do you need to transform, filter, etc?
list
"""

"""
Collections Module: Counter
"""
from random import SystemRandom

from string import ascii_letters as letters

big_string = ''.join(SystemRandom().choice(letters) for _ in range(9999))

from collections import Counter

counter = Counter(big_string)
print(counter.most_common(3))
print(counter.keys())
print(counter["a"])

print(sorted(counter))

"""
Collections module - Named Tuples

"""

from collections import namedtuple

Contact = namedtuple('Contact', 'name, phone, email, city')
print(Contact.name)

Joe = Contact('Joe', phone='5551212', email='j@j.sa', city='Seattle')
print(Joe.name)
print(Joe.city)
print(Joe.count('Seattle'))
print(Joe.count('See'))

Fred = Contact('Fred', '123456', 'f@f.sa', 'florida')
print(dir(Fred))
print(Fred.name)
print(Fred.city)
print(Fred.email)
print(Fred.phone)

"""
Collections module - Deque

"""

from collections import deque

my__q = deque(range(9))

print(my__q.pop())
print(my__q)
print(my__q.popleft())
print(my__q)
print(my__q.popleft())

"""
    Iteration (for)
    Mutating Objects While Looping
"""
# List
names = ['haroun', 'Ismail', 'Mohammed']
for name in names:
    print(name)
# Index
for position, letter in enumerate('Python'):
    print(position, letter)

#  range
for number in range(5):
    print(number)

# Unused for variable
for _ in range(5):
    print("*")

"""
No Namespace
A loop does not create a local namespace:


"""
x = 10
for x in range(3):
    y = x * 2

print(x)

"""
    Text Files
"""

# f = open('secrets.txt')
# secret_data = f.read()
# f.close()

"""
    Binary Files
"""
# f = open('secrets.bin', 'rb')
# secret_data = f.read()
# f.close()

"""
    File Reading
    Reading part of a file:
"""
# header_size = 4096
# f = open('secrets.txt')
# secret_header = f.read(header_size)
# secret_rest = f.read()
# f.close()
"""
Common Idioms
The file object is an iterable that iterates through the lines in a text file..
for line in open('secrets.txt'): 
        print(line)

f = open('secrets.txt') 
while True: 
    line = f.readline() 
    if not line: 
        break 
    do_something_with_line()


with open('workfile', 'r') as f: 
     read_data = f.read() 
 f.closed 
"""

"""
File Writing

outfile = open('output.txt', 'w') 
for i in range(10): 
    outfile.write("this is line: %i\n"%i) 
outfile.close()

with open('output.txt', 'w') as f: 
    for i in range(10): 
       f.write("this is line: %i\n"%i)


"""

outfile = open('output.txt', 'w')
for i in range(10):
    outfile.write("this is line: %i\n" % i)
outfile.close()

"""
os module
# ----------------
os.getcwd() 
os.chdir(path)
# ----------------
os.path module
# ----------------
os.path.split() 
os.path.splitext() 
os.path.basename() 
os.path.dirname() 
os.path.join() 
os.path.abspath() 
os.path.relpath()

"""

"""
pathlib
pathlib is a package for handling paths in an object oriented way. See http://pathlib.readthedocs.org/en/pep428/

All the stuff in os.path and more:

import pathlib
pth = pathlib.Path('./')
pth.is_dir() 
pth.absolute() 

.absolute() returns the full path: PosixPath('/Users/andy/projects/uw')

.iterdir() allows iteration over directories. ry this:

for f in pth.iterdir(): 
    print(f) 


p = pathlib.Path.home()  # create a path to the user home dir.
p = pathlib.Path()  # create a path to the user home dir.
print(p.absolute())

"""

"""
CSV : Comma Separated Values
"""

