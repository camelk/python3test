#matplotlib inline
#config InlineBackend.figure_format = 'retina'
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19680801)

N = 50
x = np.random.rand(N)
y = np.random.rand(N)

plt.scatter(x,y)
plt.show()


