import numpy as np

# Generate a NumPy array
array = np.arange(1, 17).reshape(4, 4)

# Slicing: Get the first two rows and columns
sliced_array = array[:2, :2]

# Reshaping: Reshape to 2x8
reshaped_array = array.reshape(2, 8)

# Splitting: Split into two arrays along columns
split_arrays = np.hsplit(array, 2)

print("Original Array:\n", array)
print("Sliced Array:\n", sliced_array)
print("Reshaped Array:\n", reshaped_array)
print("Split Arrays:\n", split_arrays)
