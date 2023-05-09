import numpy as np
import matplotlib.pyplot as plt
import time
from matplotlib.animation import FuncAnimation
from mpl_toolkits import mplot3d



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

def function(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))

def plot4():
#	10 - (-10) + 1 = 21; (elements in list)
#	21 devide in 41 elements => 0.5; (step)
#
#	10 - (-10) + 1 = 21; (elements in list)
#	21 / 2001 = 0.525; (step)
	x = np.linspace(-10, 10, 2001)
	y = np.linspace(-10, 10, 2001)

	X, Y = np.meshgrid(x, y)
	Z = function(X, Y)

	fig = plt.figure(figsize=(10, 8))
	ax = plt.axes(projection='3d')

	ax.plot_surface(X, Y, Z, cmap='cool', alpha=0.8)

	ax.set_title('3D Contour Plot of function(x, y) =\
					sin(sqrt(x^2 + y^2))', fontsize=14)
	ax.set_xlabel('x', fontsize=12)
	ax.set_ylabel('y', fontsize=12)
	ax.set_zlabel('z', fontsize=12)

	plt.show()

X_LEFT = 100
Y_TOP = 100
X_RIGHT = 1100
Y_BOTTOM = 1100
BORDER = np.array(((X_LEFT, Y_TOP),(X_RIGHT, Y_BOTTOM)))
DELTA_BORDER = 150

def min_delta_border(point, border):
	return np.min(np.abs(border - point))

def F1(point):
		db = min_delta_border(point, BORDER)
		print("point: {0}, db: {1}".format(point, db))
		if db < DELTA_BORDER:
			return -1.0 / (db + 1)
		else:
			return 0

def evaluate():
	print("DELTA_BORDER: {0}".format(DELTA_BORDER))
	point = np.array( [[1050, 600],[1050, 600]] )

	print(np.apply_along_axis(F1, 1, arr=point))

#	print("F1: {0}".format(F1(point)))


evaluate()
