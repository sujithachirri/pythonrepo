

import numnum as np

#lists working

# list_a=[1,2,3,4]
# list_b=[5,6,7,8]
#
# print(list_a*list_b)

numpy_a=np.array([1,2,3,4])
numpy_b=np.array([5,6,7,8])
print(numpy_a * numpy_b)

print(numpy_a)

#common properties

numpyBasic_array=np.array([1,2,3,4.3,"a"])

print(numpyBasic_array.dtype)
print(numpyBasic_array.itemsize)

print(numpyBasic_array.size)

#2D arrays
array_2D=np.array([[1,2,3],[3,4,5],[6,7,8]])
print(array_2D)
print("Dimensions: {}".format(array_2D.ndim))
print("shape: {}".format(array_2D.shape))
print("Array Dtype: {}".format(array_2D.dtype))

#3D array
array_3D=np.array([[[1,2],[3,4],[5,6],[6,7],[2,3],[3,8]]])
print(array_3D)
print("Dimensions: {}".format(array_3D.ndim))
print("shape: {}".format(array_3D.shape))
print("Array Dtype: {}".format(array_3D.dtype))

array_2D=np.array([1,2,3],dtype='float64') #when we give int32 output will be in integer #if u give float32 the itemsize will be 4
print(array_2D)
print(array_2D.itemsize)
print(array_2D.dtype)

array_x=np.array([[1,2,3,4,5],[6,7,8,9,0]])
print(array_x)
print(array_x.size)

print(array_x[1,2])
print(array_x[0,2])
print(array_x[:,2])
print(array_x[:,-3])
print(array_x[:])

#step - start:end - stepsize
print(array_x[0 ,0: 4: 2])
print(array_x[: ,0: 6: 2])

array_x[0,2] =10
print(array_x)
#3D array
array_3D=np.array([[[1,2],[3,4]],[[5,6],[6,7]]])
print(array_3D[1,1,1])

array_3D[:,0,:]=100
print(array_3D)

array_3D[:,0,:]=[[10,10],[20,30]]
print(array_3D)

#common arrays
#one's two's empty

print(np.zeros(3))  #one dimentional array

print(np.ones(3))

two_d=np.zeros((3,3)) #two d array
print(two_d)

three_d=np.zeros((2,3,3))
print(three_d)

four_d=np.zeros((3,3,4,5))
print(four_d)

print(np.full((3,3),2)) #to print common element [1,2,3] in the place of 2

print(np.zeros((5,), dtype=int))

#repeat

array_r=[[1,2,3],[4,5,6]]
array_repeat=np.repeat(array_r,2,axis=0)
print(array_repeat)

array_z=np.zeros((3,3))
array_z[1,1]=8
print(array_z)

updated_array=np.zeros((5,5))
updated_array[1:-1, 1:-1]= array_z
print(updated_array)

#copying arrays
array_x=np.array([1,2,3,4])
array_y=array_x
array_y[0]=7
print(array_x)
print(array_y)


array_x=np.array([1,2,3,4])
array_y=array_x.copy()
array_y[0]=10
print(array_x)
print(array_y)

#math operations

array_math=np.array([1,2,3])
print(np.sin(np.pi/2))  #example found in sin documentation actual is (np.sin)
print("Declared array: {}".format(array_math))
print("Add 10 to array: {}".format(array_math + 10))
print("Sub 10 to array: {}".format(array_math - 4))
print("raise 10 to array: {}".format(array_math ** 2))
print("mul 10 to array: {}".format(array_math * 3))
print("div 10 to array: {}".format(array_math / 2))


