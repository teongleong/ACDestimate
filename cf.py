import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def func(x, a, b, c):
    return a * np.exp(-b * x) + c
#Define the data to be fit with some noise:

xdata = []
ydata = []

def introduce_noise():
    global xdata, ydata
    xdata = np.linspace(0, 4, 50)
    y = func(xdata, 2.5, 1.3, 0.5)
    np.random.seed(1729)
    y_noise = 0.2 * np.random.normal(size=xdata.size)
    ydata = y + y_noise
    plt.plot(xdata, ydata, 'b-', label='data')

#Fit for the parameters a, b, c of the function func:

def fit():
    popt, pcov = curve_fit(func, xdata, ydata)
    plt.plot(xdata, func(xdata, *popt), 'r-', label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))
#Constrain the optimization to the region of 0 <= a <= 3, 0 <= b <= 1 and 0 <= c <= 0.5:

#popt, pcov = curve_fit(func, xdata, ydata, bounds=(0, [3., 1., 0.5]))
#popt
##array([ 2.43708906,  1.        ,  0.35015434])
#plt.plot(xdata, func(xdata, *popt), 'g--', label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))


#introduce_noise()
#fit()

def f2(x, a, b, c):
    return x*x*a + x*b + c

#xaxis = np.linspace(-7, 5, 10)
#yaxis = f2(xaxis, -1, -2, 1)
#plt.plot(xaxis, yaxis, "b-", label='data')

# yaxis2 = [[646.5, 0], 
#           [400.4, 124.9], 
#           [0, 176.635]]
# popt, pcov = curve_fit(f2, xaxis, yaxis2)
# print(popt)

#646.5 0 400.4 124.9 0 176.6352739403996

#print(str(type(xaxis)))

# http://chris35wills.github.io/parabola_python/
def calc_parabola_vertex(x1, y1, x2, y2, x3, y3):
		'''
		Adapted and modifed to get the unknowns for defining a parabola:
		http://stackoverflow.com/questions/717762/how-to-calculate-the-vertex-of-a-parabola-given-three-points
		'''

		denom = (x1-x2) * (x1-x3) * (x2-x3)
		A = (x3 * (y2-y1) + x2 * (y1-y3) + x1 * (y3-y2)) / denom
		B = (x3*x3 * (y1-y2) + x2*x2 * (y3-y1) + x1*x1 * (y2-y3)) / denom
		C = (x2 * x3 * (x2-x3) * y1+x3 * x1 * (x3-x1)
		     * y2+x1 * x2 * (x1-x2) * y3) / denom

		return A, B, C


#Define your three known points
x1, y1 = [646.5, 0]
x2, y2 = [400.4, 124.9]
x3, y3 = [0, 176.635]

#Calculate the unknowns of the equation y=ax^2+bx+c
a,b,c=calc_parabola_vertex(x1, y1, x2, y2, x3, y3)

#Define x range for which to calc parabola

x_pos = np.arange(-400, 700, 1)
y_pos = []

#Calculate y values
for x in range(len(x_pos)):
		x_val = x_pos[x]
		y = (a*(x_val**2))+(b*x_val)+c
		y_pos.append(y)

# Plot the parabola (+ the known points)
import matplotlib.pyplot as plt

plt.plot(x_pos, y_pos, linestyle='-.', color='black') # parabola line
plt.scatter(x_pos, y_pos, color='gray') # parabola points
plt.scatter(x1,y1,color='r',marker="D",s=50) # 1st known xy
plt.scatter(x2,y2,color='g',marker="D",s=50) # 2nd known xy
plt.scatter(x3,y3,color='k',marker="D",s=50) # 3rd known xy
plt.show()


# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend()
# plt.show()

