import matplotlib.pyplot as plt
import numpy as np

def points(n=1000):
    x = np.random.uniform(size=n)
    y = np.random.uniform(size=n)
    return x, y
x1, y1 = points()
x2, y2 = points()
fig = plt.figure(figsize=(4,4))
ax = fig.add_subplot(111, title="Test scatter")
ax.scatter(x1, y1, c=np.random.normal(x1,y1), s=15, cmap='rainbow', alpha=0.5)
ax.scatter(x2, y2, c=np.random.normal(x2,y2), s=15, cmap='rainbow', alpha=0.5)
plt.show()
