d = {'name': 'Brian', 'score': 42}
d['pi'] = 3.14
d[(1, 2, 3)] = 'a tuple key'

print(d)

d = {'one': 1, 'two': 2, 'three': 3}

print(str(d))

print(d.keys())
d.popitem()
print(d)
"""
and dict.popitem() will remove the "last" item in the dict.
"""

d = {'name': 'Brian', 'score': 42}

for x in d:
    print(x)

d = {'name': 'Brian', 'score': 42}

for k, v in d.items():
    print("%s: %s" % (k, v))

for item in d.items():
    print(item)

d.setdefault('something', 'a different value')

print(d)

item_view = d
item_view.update({'d': 453})

s = set()
s.update(['this', 'that'])
print(s)


def sort_key():
    return []


sorted_dict = dict(sorted(item_view.items(), key=sort_key))

# Set Constructors

"""
    set()
    set([1, 2, 3])
    {1, 2, 3}

    s = set()

    s.update([1, 2, 3])
    print(s)
    {1, 2, 3}

"""
