# NumPy
# just Python
def pythonsum(n):
    a = range(n)
    b = range(n)
    c = []
    for i in range(len(a)):
        a[i] = i ** 2
        b[i] = i ** 3
        c.append[a[i]+b[i]]
    return c
# with NumPy
import numpy as np
def numpysum(n):
    a = numpy.arange(n)**2
    b = numpy.arange(n)**3
    c = a + b
    return c

#compare calculation time
import sys
from datetime import datetime
size = 1000
start = datetime.now()
c = pythonsum(size)
delta = datetime.now() - start
print 'The last 2  elements of the sum', c[-2:]
print 'PythonSum elapsed time in ms',delta.microseconds

start = datetime.now()
c = numpysum(size)
delta = datetime.now() - start
print 'The last 2  elements of the sum', c[-2:]
print 'NumpySum elapsed time in ms',delta.microseconds

#array
import numpy as np
'''
np.array()
np.asarray()
np.arange()
np.ones()
np.ones_like()
np.zeros()
np.zeros_like()
np.empty()
np.empty_like()
np.eye()  /np.identity()
'''

a = np.arange(5)
a.dtype
a.shape
m = np.array([np.arange(2), np.arange(2)])
m.shape
m.dtype
np_ones_like(m)
np.zeros(10)
np.zeros((3,6))
np.empty((2,3,2))

# data fromat
np.float64(15)
np.float(True)
np.int8('C')
np.bool(42)
np.bool(0)
np.arange(7,dtype = np.uint16)

arr = np.array([1,2,3,4,5])
arr.dtype
float_arr = arr.astype(np.float64)
float_arr.dtype

a = np.array([[1,2],[3,4]])
a.dtype.byteorder
a.itemsize

t = np.dtype('float64')
t.char
t.str
t.type

# calculation of array
arr = np.array([[1, 2, 3],[4, 5, 6]])
arr * arr
arr - arr
1/ arr
arr ** 0.5

# sub_arrays[start:stop:step]
a = np.arange(9)
a[3:7]
a[:7:2]
a[::-1]
s=slice(none,7,2)
a[s]
s=slice(none,none,-1)
a[s]

b=np.arange(24).reshape(2,3,4)
b[1,0,1]  #b[D1,D2,D3]
b[:,0,1]
b[1][1][1]

# memento
'''
sub_arr = arr[start:stop:step:,start:stop:step:,start:stop:step]
s = slice(start,stop,step)
'''

# boolean
names = np.array(['Bob','Joe', 'Will', 'Joe', 'Joe','Bob','Will'])
data = np.arange(28).reshape(7,4)
names == 'Joe'
data[names == 'Joe']
data[names == 'BOb',2:]

data[data < 5] =0

arr = np.empty((8,4))
for i in range(8):
...     arr[i]=i

arr[[4,3,0,6]] #arr[[row_n,row_m,row_p],[col_n,col_m,col_p]]

arr.T
arr.transpose()
a = np.arange(24).reshape(3,8)
a.resize(2,12)

# matrix combination
a = np.arange(9).reshape(3,3)
b = 2 * a
np.hstack((a,b))    #horizontal stack
np.concatenate((a,b),axis=1)
np.vstack((a,b))    #vertical stack
np.concatenate((a,b),axis=0)

np.dstack((a,b))    #deep stack

one = np.arange(2)
two = one*2
np.column_stack((one,two))
np.row_stack((one,two))

a = np.arange(9).reshape(3,3)
np.hsplit(a,3)
np.split(a,3,axis=1)
np.vsplit(a,3)
np.split(a,3,axis=0)

c = np.arange(27).reshape(3,3,3)
np.dsplit(c,3)

# properties of array
b = np.arange(24).reshape(2,12)
b.ndim
b.size
b.itemsize
b.nbytes

b = np.array([1.+1.j, 3.+2.j])
b.real
b.imag

b = np.arange(27).reshape(3,3,3)
b.flat
b.flat[7]

# data format of array
b = np.array([1.+1.j, 3.+2.j])
b.astype(int)
b.astype('complex')
b.tolist()
b.tostring()

np.fromstring(b.tostring(),dtype = complex)
np.fromstring('20:42:52', sep=':',dtype = int)


