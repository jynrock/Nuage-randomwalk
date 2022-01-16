import matplotlib.pyplot as plt
import numpy as np
import random as random

n = random.randint(2000, 20000)
def points(n=n):
    x = np.random.uniform(size=n)
    y = np.random.uniform(size=n)
    return x, y
x, y = points()


fig = plt.figure(figsize=(4,4))
ax = fig.add_subplot(111, title="Test scatter")
plt.scatter(x, y, c=np.random.rand(len(x)), s=15, cmap='rainbow', alpha=0.8)
plt.axis('off')
plt.savefig("Nuage_"+str(n)+".png",bbox_inches="tight",dpi=1000)
plt.show()
