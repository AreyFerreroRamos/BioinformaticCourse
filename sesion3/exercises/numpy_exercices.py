import numpy as np
import matplotlib.pyplot as plt

ar1 = np.array([3, 4, 5, 6])
ar2 = np.array([4, 5, 6, 7])
ar3 = np.array([3, 4, 5, 6])
ar4 = np.array([3, 3, 5, 6])

# Comparaison whether two arays are the same position by position.
print(np.equal(ar1, ar2))
print(np.equal(ar1, ar3))
print(np.all(np.equal(ar1, ar3)))
print(np.all(np.equal(ar1, ar4)))

# Multiply two arrays position by position.
mult_result = ar1 * ar2
print(mult_result)

# Dot product between two arrays.
dot_result = np.dot(ar1, ar2)
print(dot_result)

# Standard normalization on 15 elements.
np.random.normal(0, 1, 15)
np.random.standard_normal(15)

# Inverse matrix.
m = np.array([[1, 2], [3, 4]])
print(m)
print(np.linalg.inv(np.array(m)))

# Acumulate the elements in a matrix to an array by colapsing rows.
row_colpasing_result = m.sum(axis=0)
print(row_colpasing_result)

# Acumulate the elements in a matrix to an array by colapsing columns.
column_colpasing_result = m.sum(axis=1)
print(column_colpasing_result)

# Concatenate the elements of two matrices row wise
row_wise_result = np.concatenate((m, m), axis=0)
print(row_wise_result)


# Concatenate the elements of two matrices row wise
column_wise_result = np.concatenate((m, m), axis=1)
print(column_wise_result)

# Generate the histogram from a set of data.
data = np.random.standard_normal(40)
bins = 5
hist = np.histogram(data, bins=bins, density=True)
print(hist)

# Show the data in a plot.
# plt.hist(data, bins=bins)
# plt.show()

# 

# Caluclate the mean by column.
print(m.mean(axis=1))
