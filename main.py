import numpy as np

# p_list = [1, 3, 4, 5, 7, 7]
# print(p_list)
#
# n_list=np.array(p_list)
# print(n_list)

#one-d-array
# p_list = [1, 3, 4, 5, 7, 7]
#two-d array
# array_2d=np.array([[1,2,3],
#                    [4,5,6],
#                    [7,8,9]])
# print(array_2d)


# creation of array with default value
# print(np.zeros(shape=3))
# print(np.ones((2,3)))
# print(np.full((3,3),7))
# crating sequence of numbers in numpy
# print(np.arange(1,10,2))
# creating identity matrices
# print(np.eye(3))


#how to get shape size and type
array_2=np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]],
    [[9, 10], [11, 12]]
])
# print(array_2.shape)
# print(array_2.size)
# print(array_2.ndim)
# print(array_2.dtype)
# print(array_2.astype(float))

# operations
print(array_2+2)
print(array_2*2)
print(array_2**2)

# aggregation function (to get summary)
# print(np.sum(array_2))
# print(np.min(array_2))
# print(np.max(array_2))
# print(np.std(array_2))
# print(np.var(array_2))

# indexing and slicing indexing is selecting only one element and slicing get a whole group
# fancy indexing and boolean masking
# fancy indexing  lets you grab multiple values from arrays using lists or arrays of indices, instead of just one at a time.
# boolean masking only show what we need

# reshaping and manipulating array
# reshaping an array without modifying the array means change in dimenstion only
# reshaped_arr=array_2.reshape(2,6)
# print(reshaped_arr)
# flattening array Flattening an array means turning a multi-dimensional array into a 1D list of values
# we can use 2 meathods revel() view and flatten() copy
# print(array_2.ravel())
# print(array_2.flatten())


# insertfunction
# new_array=np.insert(array_2,2,100,axis=0)
# print(new_array)
# append an array
# arr=np.array([
#     [[1, 2], [3, 4]],
#     [[5, 6], [7, 8]],
#     [[9, 10], [11, 12]]
# ])
# print(arr)
#concatating a array
# ar=np.concatenate((array_2,arr))
# print(ar)
# deleting an array
# arr=np.delete(array_2,0,axis=0)
# print(arr)
# stacking an array
# np.hstack(),np.vstack()
#splitnig an array
# np.hsplit(),np.vsplit()
# broadcasting
# prices=np.array([100,200,300])
# discount=10
# final_price=prices-(prices*discount/100)
# print(final_price)
# how numpy handle differnt type of shapes
# vectorisation
#  is used for  performing operations on entire arrays in one go.


# handling missing value
# np.isnan
# np.nan_to_num()
# np.isinf()


