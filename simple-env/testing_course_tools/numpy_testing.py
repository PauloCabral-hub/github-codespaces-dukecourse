import numpy as np

data = [[1, 2, 3], [4, 5, 6], [7, 8,9]]

# to create numpy arrays you can use lists
data_array = np.array(data)

# or special methods
data_array = np.ones(12)
data_array = np.zeros(5)
data_array = np.arange(1,10)

# to inspect array atributes
data_array.shape
data_array.ndim
data_array.size
data_array.dtype
data_array.nbytes

# to modify
data_array.reshape(2,2) 

# numpy methods for linear algebra
data_array.transpose()
data_array.diagonal()

# matrix product is done in a weird way
# A1 @  A2  


# remember that ndarrays can take any dimension you want