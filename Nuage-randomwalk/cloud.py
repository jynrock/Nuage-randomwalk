import matplotlib.pyplot as plt
import numpy as np
import random as random

i = 0

while i < 15:
	n = random.randint(2000, 50000)
	m = random.randint(5, 100)
	def points(n=n):
	    x = np.random.uniform(size=n)
	    y = np.random.uniform(size=n)
	
	    return x, y
	x, y = points()
	
	
	fig = plt.figure(figsize=(10,10))
	
	plt.scatter(x, y, c=np.random.rand(len(x)), s=m, cmap='rainbow', alpha=0.6)
	plt.axis('off')
	plt.savefig("Clouds/Cloud_"+str(n)+"-"+str(m)+".png")
	i = i+1
