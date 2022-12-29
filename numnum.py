import numpy as np
data_from_text=np.genfromtxt('numpy.txt.txt',delimiter=',')
print(data_from_text)

data_from_text=data_from_text.astype('int32')
print(data_from_text)

print(data_from_text > 10)
#advanced indexing

print(data_from_text[data_from_text > 0])
print(data_from_text[data_from_text < 0])

#fill values
fill_values=np.genfromtxt('numpy.txt.txt',delimiter=',',dtype=np.int32)
print(fill_values)

fill_values=np.genfromtxt('numpy.txt.txt',delimiter=',',dtype=np.int32,filling_values=100)
print(fill_values)

