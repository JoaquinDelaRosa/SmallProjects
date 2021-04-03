import numpy as np
import math
import random
import matplotlib.pyplot as plt
from matplotlib import animation

fig = plt.figure()
ax = plt.axes(xlim = (0,1), ylim = (0,1))
plot, = ax.plot([], [], lw = 1)


N = 10000
successes = 0 
failures = 0
probability = 0.5

def init():
    plot.set_data([], [])
    return plot,

def calculateProbability(a, b, p):
    # Where a is number of successes
    # b is number of failures
    # p is the probability of success
    const = math.comb(a + b, a)
    return  const * math.pow(p, a) * math.pow(1 - p, b)

def update(frame):
    #Generate random number
    rn = random.random()
    if(rn < probability):
        global successes
        successes += 1
    else:
        global failures
        failures += 1

    # Compute beta function
    x = np.linspace(0, 1, N)
    y = [calculateProbability(successes, failures, i) for i in x]
    plot.set_data(x, y)
    return plot, 

anim = animation.FuncAnimation(fig, update, init_func=  init, interval = 1000, blit = True)
plt.show()
