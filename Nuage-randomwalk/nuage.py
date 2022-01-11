import numpy as np
import matplotlib.pyplot as plt 


n = 20000
X = np.random.rand(n,1)
Y = np.random.rand(n,1)

plt.scatter(X,Y, c=np.random.normal(X,Y), cmap='rainbow', s=15, alpha=0.4)
plt.show()