"""
In this lesson we are going to learn how to validate and protect the quality of the data we process.
An “exception” is an indication that something out of the ordinary (exceptional) happened.
Exceptions are handled with a “try - except” block.
try:
    with open('missing.txt') as data_file:
        process(data_file)   # never called if file missing
except FileNotFoundError:
    print("Couldn't find missing.txt")

try:
    do_something()
    f = open('missing.txt','w')
except IOError:
    print("couldn't open missing.txt")
else:
    process(f)  # only called if there was no exception

"""

import unittest


class MyTests(unittest.TestCase):

    def test_tautology(self):
        self.assertEqual(1, 1)


# in test.py
if __name__ == '__main__':
    unittest.main()
