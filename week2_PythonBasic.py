# Python Wiederholung 2
'''
if condition:
    syntax_1
else:
    syntax_2
'''

flag = False
name = 'luren'
if name == 'python':
    flag = True
    print 'welcome'
else:
    print name

n = 9
if (n>=0 and n<=5) or (n>=10 and n<=15):
    print 'hello' \
else:
    print 'undefined'


'''
while
'''
# Example 1
count = 0
while(count<3):
    print 'Th count is:', count
    count +=1

print 'while finished'

#Example 2
i = 1
while i < 10:
    i += 1
    if i%2 > 0:
        continue
    print i

i = 1
while 1:
    print i
    i+=1
    pass        # pass  do nothing
    if i> 10:
        break

'''
Ctrl + C to stop endless loop
'''

'''
for iterating_var in sequence:
    statement(s)
'''
# Examples
for letter in 'Python':
    print letter

fruits =['banana','apple', 'mango']
for fruit in fruits:
    print fruit

for index in range(len(fruits)):
    print fruits[index]

range(10,20)



# mathamatical functions
abs(-3)
cmp(2,3) #return 0 1 -1
list = [3, 5, 6, 7, 8,9]
max(list)
min(list)
pow(2,3) #2**3
round(3.1415926,4)
import math
math.ceil(4.1)
math.exp(3)
math.fabs(-10) #return float 10.0
math.log(100,10)    #log(x[,base])
math.e #constant
math.log(math.e)
math.log10(100)
math.modf(1.23)
math.sqrt(2)
#triangle functions
x = math.pi
math.sin(x)
math.cos(x)
math.tan(x)
math.cot(x)
math.acos(x)
math.asin(x)
math.atan(x)
math.atan2(x,y)
hypot(x,y)
math.degrees(math.pi/2)
math.radians(x)

# random functions
import random as rdm
list =[1, 2, 3, 554,6464,45,4]
rdm.choice(list)
rdm.randrange(50,100,1) #randrange([start,] stop [,step])
'''
rdm.seed([x])
'''
rdm.shuffle(list)
rdm.uniform(1,100)

#Escape character
\
print '\\'+\
    '\' '+\
    '\" '
\a      #ring the bell
\b      #backspace
\e      #escape
\000    #empty
\n      #new line
\v      #vertical   table
\t      #row table
\r      #return
\f      #new page
\oyy    \o12    #see ASCII table
\xyy    \x0a
\other

>> print 'my name is %s and is %d years old' % ('John', 25)

%c  char
%s  string
%d  decimal
%u  unsign int
%o  oktave
%x  hex %#x
%X  HEX
%f  float
%e  science
%E
%g  4<5>
%G
%p


import time
import calendar

see week02d

#function

def functionname(parameter1,paremeter2,...):
    'introdution'
    function_suite
    return expression

def printme(str):
    'print  some string'
    print str
    return

def printinfo(name = 'Default',age = 35):
    print 'name',name
    print 'Age',age
    return

printinfo(age = 35, name = 'John')
printinfo()

# number of parameter unsure function
def printinfo(arg1,*vartuple):
    'print sth.'
    print arg1
    for var in vartuple:
        print var
    return

#lambda function
mySum = lambda arg1,arg2: arg1 + arg2
mySum(10,20)

# FILE
Expr = input('U can input expression with input()')
'''
>>> expr = input('expression')
expression 2+3
>>> expr
5
'''

val =raw_input('raw_input don't accept expression')
'''
>>> val =raw_input('hh')
hh 2+3
>>> val
'2+3'
'''

myFile = open (file_name [,access_mode][,buffering])
myFile.name
myFile.closed
myFile.mode
myFile.softspace
myFile.write(strin)
myFile.read([count])

'''
access_mode:
r
rb read binar
r+  read/write
rb+
w
wb
w+
wb+
a
ab
a+
ab+
'''

>>>my = open("Bsp.txt", 'r+')
>>> my.write('hello, my file')
>>> my.close()

current_position = my.tell()
position = my.seek(0,0)
str = my.read(10)

# os: Opeartion System
import os

os.rename('source.txt','destination.txt')
os.remove('source.txt')

# Exception Handling
try:
    fh = open('testfile','r')
    fh.write('This is my test file for exception handling')
except IOError:
    print 'Error: can\'t find file or read data'
else:
    print 'Written content in the file sucessfully'
finally:
    print 'Do this anyway'

def temp_convert(var):
    try:
        return int(var)
    except ValueError, Argument:
        print 'The argument does not contain numbers\n', Argument

temp_convert('xyz')

# customer exception
class Networkerror(RuntimeError):
    def __init__(self,arg):
        self.args = arg
try:
    raise Networkerror('Bad hostname')
except Networkerror,e:
    print e.args
