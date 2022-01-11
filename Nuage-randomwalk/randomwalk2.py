import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#setting up steps for simulating 2Ddims = 2
step_n = 200
step_set = [-1, 0, 1]
origin = np.zeros((1,dims))#Simulate steps in 2D
step_shape = (step_n,dims)
steps = np.random.choice(a=step_set, size=step_shape)
path = np.concatenate([origin, steps]).cumsum(0)
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2, c=”green”)
ax.set_ylim(-10, 10)
ax.set_xlim(-5, 10)
plt.title(‘2D Random Walk’)xdata, ydata = [], []
del xdata[:]
del ydata[:]
line.set_data(xdata, ydata)