# nNumPy, short for "Numerical Python", is a fundamental Python library for scientific computing.
# It provides support for large, multi-dimensional arrays and matrices, 
# along with a collection of mathematical functions to efficiently operate on these data structures

# array = is a collection of homoginus types of data.

# numpy syntax
import numpy

array1 = numpy.array([1, 3, 4, 45, 5])
print(type(array1))

array2 = numpy.array(['vaibhav', 'vaibhavi', 'akash', 'vishvali'])
print(array2)


name = ['a','c','d','v','d']
print(type(name))
A1 =numpy.array(name)
print(A1)
print(type(A1))


set1 = {1,2,3,4,5,5,6}
a2 = numpy.array(set1)
print(a2)
print(type(a2))

# one dymensionall = nd array showing
array = numpy.array([[12,3,4,],[12,3,5]])
print(array)


#multidimensional array  / 2D list dosent matter size of all
list2 = [[1,2,3,4],[5,6,7,8,9,0]]
print(list2)
print(type(list2))

# 2D array = matter value in element / show value error editor
arr = numpy.array([[1,2],[2,4],[3,4]])
print(arr)
print(type(arr))



# Create a 2x2 array
array_2x2 = numpy.array([[1, 2], [3, 4]])
print(array_2x2)



# giving range and print array
new = numpy.arange(1,50)
print("\n",new )

# using the step of in array
new1 = numpy.arange(1,50,3)
print( "\n",new1 )

# zeros array
ary = numpy.array([[0,0],[0,0]])
print(ary)

zero = numpy.zeros((3,3))
print(zero)    # by default float value

ze0 = numpy.zeros((4,4),dtype = int)  #return integer in value
print("\n",ze0)

#ones array create 
one2 = numpy.ones((3,3),dtype = int)
print("\n",one2)


# identity array
id = numpy.eye(4,dtype=int)
print("\n",id)

#random array = random value return  bydefault float value
ran = numpy.random.rand(2,3)
print("\n",ran)

# random value  in integer format>?
dom = numpy.random.randint(10,20,(2,3))
print(dom)

#linespace array
sp = numpy.linspace(0, 1, 5)
print(sp)