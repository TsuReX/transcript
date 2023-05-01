import numpy as np
import matplotlib.pyplot as plt
import time
from matplotlib.animation import FuncAnimation

def plot1():
	x = np.arange(-2*np.pi, 2*np.pi, 0.1)
	y = np.cos(x)

	plt.ion()
	
	for delay in np.arange(-2*np.pi, 2*np.pi, 0.1):
		y = np.cos(x+delay)

		plt.clf()
		plt.plot(x, y)
		plt.draw()
		plt.gcf().canvas.flush_events()

		time.sleep(0.004)

	plt.ioff()
	plt.show()

def plot2():

	plt.ion()	
	fig, ax = plt.subplots()
	x = np.arange(-2*np.pi, 2*np.pi, 0.1)
	y = np.cos(x)
 
	line, = ax.plot(x, y)

	for delay in np.arange(0, 4*np.pi, 0.1):
		y = np.cos(x+delay)

		line.set_ydata(y)

		plt.draw()
		plt.gcf().canvas.flush_events()

		time.sleep(0.02)
	plt.ioff()
	plt.show()


def update_cos(frame, line, x):
	line.set_ydata( np.cos(x+frame) )
	return [line]

def plot3():

	fig, ax = plt.subplots()
	x = np.arange(-2*np.pi, 2*np.pi, 0.1)
	y = np.cos(x)
 
	line, = ax.plot(x, y)
	
	phasa = np.arange(0, 4*np.pi, 0.1)
	
	animation = FuncAnimation(
								fig,
								func=update_cos,
								frames=phasa,
								fargs=(line, x),
								interval=40,
								blit=True,
								repeat=False)
	
	plt.show()

plot3()
