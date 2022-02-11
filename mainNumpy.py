import numpy as np

l = [1, 2, 3, 4, 5, 6]
a = np.array(l)
print(a)
print(type(a))

# Types of array ------->

# 1. 0-D array :-
a = np.array(20)
print(a)

# 2. 1-D array :-
l=[1,2,3,4,5,6,7,8,9,10]
a=np.array(l)
print(a)

# 3. 2-D array :-
l=[[1,2,5,7],[3,4,8,9],[5,6,3,4]]
a=np.array(l)
print(a)

# 4. n-D array :-
l=[1,2,3,4,5]
a=np.array(l,ndmin=5)
print("n-D Array: ",a)

# CONVERT TO ARRAY--
l=[10, 20, 30, 40, 50, 60]
a1=np.array(l)
print(a1)

# INDEXING--
print(a1[3])
print(a1[2]+a1[4])

# 2-D array indexing--
l=[[1,2,5,7],[3,4,8,9],[5,6,3,4],[3,4,5,6]]
a2=np.array(l)
print(a2)
print(a2[0][2])
print(a2[2][3])

# Slicing--
print("slicing 1-4:  ", a1[1:5])

# Element from index 1 to 5 but only of odd positions
# 1,2,3,4,5 = 1,3,5

print(a1[1:6:2])

print(a1[-1])

# To convert to array--

l=[10.0, 20.0, 30.0, 40.0, 50.0, 60.0]
a=np.array(l)
print(a)

#dtype -- To get data type of array elements (float/int etc)
print(a.dtype)

# Shape--  To print no of row and columns
print("Shape of a: ",a.shape)

b=np.array([[1,2],[3,4],[5,6]])
print(b.shape)

c=np.array([44,55,66,77,88],ndmin=15)
print("Array C: ",c)
print("Shape of C: ",c.shape)

# Reshaping an array--     Change the dimension of array automatically
b=a.reshape(3,2)
print("Reshaped aaray result: ",b)
print("Reshaped array shape(): ",b.shape)

# Size--    To print lenght of array
print("Size of a: ",a.size)

# Search for an elements--
if 20.0 in a:
    print("Element Found")
else:
    print("Elements not Found")

# ndim--   print dimensions of array

print(a.ndim)
print(c.ndim)

# Copy--   Creates copy and save in new array
d=a.copy()
print(d)

# Fill--   Replace whole array by 0 [0]
p=np.array([1,2,34,5,6])
p.fill(0)
print(p)

# Concatenate--  Joins 2 or More array
x=np.array([1,2,3,4])
y=np.array([7,8,9,10])

z=np.concatenate((x,y))
print(z)

# Sort--   Arrangement of word-wise OR number-wise
l=[60, 45, 23, 56, 89, 90,100]
a=np.array(l)
print(a)
s=np.sort(a)
print("Sorted a: ",s)

st=["bat","apple","dog","eat","cat"]
x=np.array(st)
print(x)
y=np.sort(x)
print(y)

# Boolean Filtering--
l=[60,45,23,56,89,90,100]
a=np.array(l)
print(a)
x=a>80
print(x)

y=a[a>80]      # Those number greater than 80
print(y)

z=a[a<80]      # Those number less than 80
print(z)


# Vectorization--
x=a*10
print(x)

x=a+20
print(x)

# Broadcasting--
a=np.array([[1,2],[3,4]])
b=np.array([11,22])
c=a+b
print(c)