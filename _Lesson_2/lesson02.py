"""
    In this lesson we are going to start by covering two more types: strings and Booleans.
"""

csv = "a comma,separated,values"
print(csv.split(','))

new_csv = " ".join(csv.split(','))
print(new_csv)

sample = 'A long string of words'

print(sample.upper())
print(sample.lower())
print(sample.swapcase())
print(sample.title())

number = "12345"
print(number.isnumeric())
print(number.isalnum())
print(number.isalpha())
fancy = "Th!$ $tr!ng h@$ $ymb0l$"
print(fancy.isalnum())

# Common Escape Sequences::
#     \\  Backslash (\)
#     \a  ASCII Bell (BEL)
#     \b  ASCII Backspace (BS)
#     \n  ASCII Linefeed (LF)
#     \r  ASCII Carriage Return (CR)
#     \t  ASCII Horizontal Tab (TAB)
#     \ooo  Character with octal value ooo
#     \xhh  Character with hex value hh
#     \uxxxx Character with Unicode code point value xxxx
#     \N{char-name} Character with Unicdoe name char_name

s = "these\tare\tseparated\tby\ttabs"
print(s)

print("this\nthat")

print(r"this\nthat")
print("this" "that")
print("This is the first line\n"
      "And here is another line\n"
      "If I don't put in a newline "
      "I can get a very long line in, without making the"
      "line of code too long.")

print(ord('h'))
print(ord('s'))
print(chr(104))
print(chr(115))

# -------------------------------------------------
name = 'Chris'
format_name = 'Hello {}!'.format(name)
print(format_name)
# -------------------------------------------

"""
The Basics of If
 -if
 -elif
 -else
 
while a_condition:
   some_code
   iterating
"""

"""
      Function
"""


def giveTwoValues():
    return 1, "two"


first, second = giveTwoValues()
print(first)
print(second)

my_tuple = giveTwoValues()
print(my_tuple)
# ----------------------------------

"""
    Your mission today is to find three different ways to print the number 0 thru 10 using Python.
"""

# First way use for
for i in range(0, 11):
    print(i)

# Second way use while
number = 0
while number <= 10:
    print(number)
    number += 1


# Third way use function

def print_zero_to_ten(number=0):
    print(number)
    number += 1
    if number == 11:
        exit()
    print_zero_to_ten(number)


print_zero_to_ten()
