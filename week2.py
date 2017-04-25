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


VEDIO week02d 04:10