# Python code for 2D random walk.
import numpy
import pylab
import random
import matplotlib.cm as cm
 
# defining the number of steps
n = random.randint(2000, 20000)
 
#creating two array for containing x and y coordinate
#of size equals to the number of size and filled up with 0's
x = numpy.zeros(n)
y = numpy.zeros(n)

r = random.random()

b = random.random()

g = random.random()

# filling the coordinates with random variables
for i in range(1, n):
    val = random.randint(1, 4)
    if val == 1:
        x[i] = x[i - 1] + 1
        y[i] = y[i - 1]
    elif val == 2:
        x[i] = x[i - 1] - 1
        y[i] = y[i - 1]
    elif val == 3:
        x[i] = x[i - 1]
        y[i] = y[i - 1] + 1
    else:
        x[i] = x[i - 1]
        y[i] = y[i - 1] - 1
     
 
# plotting stuff:
pylab.title("Random Walk ($n = " + str(n) + "$ steps)")
pylab.plot(x, y, color=(r, g, b))
pylab.axis('off')
pylab.savefig("rand_walk"+str(n)+".png",bbox_inches="tight",dpi=1000)
pylab.show()