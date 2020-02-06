import numpy as np


array = np.arange(3, 12).reshape(3, 3)
print(array)
print()
second_array = array ** 2
print(second_array)

print()
third_array = np.vstack([array, second_array])
print(third_array)
print()

print(third_array @ array)
print()
print(third_array.reshape(3,3,2))
