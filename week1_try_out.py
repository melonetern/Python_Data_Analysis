#     Wiederholung Python Basis
# frequently used modules
# numpy,scipy, pandas, matplotlib.pyplot

print 'hello Python!'

long_string = 'long_string1 ' +\
               'long_string2 '+\
                'long_string3'

paragraph = '''this is a long paragraph,
                use this way in multiple lines'''

a = [1, 2, 3, 4, 5, 6,
     7, 8, 9,10]

#This is a comment

'''more lines comment
in this way'''

x = raw_input('input your value')

x = 1; y = 2; z = 3

'''
if expression:
    suite
elif expression:
    suite
else:
    suite
'''
import sys
help(sys.stdout.write)

#variable
counter = 100 #integer
miles = 1000.0 #float
name = 'John' #string

a = b = c = 1
a,b,c = 1, 2, 'John'

#data types: Numbers, String, List, Tuple, Dictionary
#Number: int, long, float, complex
var_a = 0.1
var_b = 3e2
del var_b

s = 'lovepython'
s[1:5]
s[0:-1]
s_twice = s*2
s_more = 'I' + s + 'you?'

#list
list = [ 'abcd', 786, 2.24, 'John', 70.2]
list[:2]
list[2:]
tinylist = [123,'John']
print tinylist*2
print list + tinylist

#tuple
tuple = ( 'abcd', 786, 2.24, 'John', 70.2)

#dict
dict ={}
dict['one'] = 'This is one'
dict[2] = 'This is two'
print dict
dict.keys()
dict.values()

a = 9 % 5
b =9 // 4
c =3**2

# Operators
#compare: ==, !=, >, <, =<, =>
# =, +=, //=, %=, **=, ...
#bit operators
a = 60      #0011 1100 == 60
b = 13      #0000 1101 == 13
#---------------------------------
~a          #1100 0011 == -61
a << 2      #1111 0000 == 240
a >> 2      #0000 1111 == 15
a & b       #0000 1100 == 12
a | b       #0011 1101 == 61
a ^ b       #0011 0001 == 49

#logic: and, or, not
a = True
b = False
a and b
not a

#member: in, not in
#ID: is, is not
