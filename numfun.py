import numpy as np
def numpy_function(x,y):
    return 2*x+y
b= np.fromfunction(numpy_function, (5,5), dtype=int)
print(b)