import matplotlib.pyplot as plt
import pylab
import numpy as np
import math


x = np.linspace(-30, 30, 1000)  # 100 linearly spaced numbers
y = np.sin(x)/x  # computing the values of sin(x)/x

# x^2 / a^2 + y^2 / b^2 = 1
# y = sqrt (b^2 * (1 - x^2 / a^2))

a = 4
b = 2

#z = np.sqrt( np.square(b) * (1 - (np.square(x) / np.square(a))) ) - 1
#print(type(y))

def drawline(x1, y1, x2, y2):
    pylab.plot([x1, x2], [y1, y2])

#pylab.plot([-4, 4], [0, 0])
drawline(-4, 0, 4, 0)
#pylab.plot([0, 0], [0, 2])
drawline(0, 0, 0, b * 0.5)

# compose plot
#pylab.plot(x, z)  # sin(x)/x
#pylab.plot(x, y, 'co')  # same function with cyan dots
#pylab.plot(x, 2*y, x, 3*y)  # 2*sin(x)/x and 3*sin(x)/x

multiplier = 8.18476236105044

rawdata = [
    [62.45,	371,	646.5, 2404.8326345091],
    [67,	256.9,	699, 3149.7049068127],
    [130.6,	370.7,	723.5, 3146.26461061367],
    [48.5,	332.7,	691, 2333.21237781733],
    [91,	469.3,	746.5, 2748.90014369383],
    [73.5,	405.4,	703, 2286.403507695],
    [76.6,	332.6,	816, 2633.60836116534],
    [45,	251.7,	748, 2692.17328565603],
    [85.2,	402.7,	665.5, 2472.19133563727],
    [67,	294.8,	748, 3194.03506555579],
    [69.6,	367.3,	726, 2340.78149343333],
    [153.2,	481.1,	890, 2922.85220290044],
    [48.9,	193.5,	677, 3004.94475822767]
]

rawdata2 = [
    {"a": 62.45, "b": 371,    "c": 646.5, "x": 2404.8326345091, "cm":5717.11389164145},
    {"a": 67,	"b": 256.9, "c": 699, "x": 3149.7049068127, "cm": 6147.20475094165},
    {"a": 130.6, "b": 370.7, "c": 723.5, "x": 3146.26461061367, "cm": 6137.15440982215},
    {"a": 48.5,	"b": 332.7, "c": 691, "x": 2333.21237781733, "cm": 6063.88802667065},
    {"a": 91,	"b": 469.3,	"c": 746.5, "x": 2748.90014369383, "cm": 5822.0430477625},
    {"a": 73.5,	"b": 405.4,	"c": 703, "x": 2286.403507695, "cm": 5449.33282613565},
    {"a": 76.6,	"b": 332.6,	"c": 816, "x": 2633.60836116534, "cm": 6019.77003298295},
    {"a": 45,	"b": 251.7,	"c": 748, "x": 2692.17328565603, "cm": 5870.2390283531},
    {"a": 85.2,	"b": 402.7,	"c": 665.5, "x": 2472.19133563727, "cm": 5840.9859826916},
    {"a": 67,	"b": 294.8,	"c": 748, "x": 3194.03506555579, "cm": 6236.8928963066},
    {"a": 69.6,	"b": 367.3,	"c": 726, "x": 2340.78149343333, "cm": 5889.89274095885},
    {"a": 153.2, "b": 481.1, "c": 890, "x": 2922.85220290044, "cm": 6007.32107515485},
    {"a": 48.9,	"b": 193.5,	"c": 677, "x": 3004.94475822767, "cm": 5925.8225167482}
]

#32
rawdata3a = [
    {"a": 47.7, "b": 198, "c": 1360},
    {"a": 93.8, "b": 381, "c": 1323.5},
    {"a": 60.3, "b": 263, "c": 1285.5},
    {"a": 113.6, "b": 456.5, "c": 1275.5},
    {"a": 153.2, "b": 481.1, "c": 890}
]

#33
rawdata3b = [
    {"a": 62.6, "b": 227.4, "c": 1360},
    {"a": 64.2, "b": 260.6, "c": 1300},
    {"a": 56.4, "b": 263, "c": 1285.5},
    {"a": 127.4, "b": 487.9, "c": 1275.5},
    {"a": 48.9, "b": 193.5, "c": 677}
]

rawdata32 = [
    {"a": 58.56, "b": 143.56, "c": 781.7},
    {"a": 119.89, "b": 280.79, "c": 959.16},
    {"a": 278.05, "b": 558.65, "c": 1009.075},
    {"a": 432.79, "b": 845.29, "c": 1105.46}
]

rawdata33 = [
    {"a": 125.88, "b": 217.99, "c": 649.17},
    {"a": 248.13, "b": 393.74, "c": 629.43},
    {"a": 111.27, "b": 187.52, "c": 657.14},
    {"a": 99.6, "b": 176.33, "c": 637.53}
]

# x[0] a
# x[1] b
# x[2] c

for x in rawdata:
#    x[0] = x[0] * math.sin(45) # should be pi / 4
    x[0] *= 2
    x.append(x[2] - x[1] + x[0])

for x in rawdata2:
    x["a"] *= 2
    x["c-b+a"] = x["c"] - x["b"] + x["a"]





#for x in rawdata:
#    drawline(x[2], 0, x[4], x[0])
#    drawline(x[4], x[0], 0, x[3]/multiplier)

def drawset(index):
    x = rawdata[index]
    drawline(x[2], 0, x[4], x[0])
    drawline(x[4], x[0], 0, x[3]/multiplier)


def max_value(a, b, c):
    # 2ax + b = 0
    # x = -b/2a
    x = (-b/(2*a))
    y = a*x*x + b*x + c
    return x, y


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


# x = np.array([0.0, 1.0, 2.0, 3.0,  4.0,  5.0])
# y = np.array([0.0, 0.8, 0.9, 0.1, -0.8, -1.0])
# z = np.polyfit(x, y, 3)
# z


# curve fit and draw
def sketch_curve(x1, y1, x2, y2, x3, y3):
    #Define your three known points
    #x1, y1 = [646.5, 0]
    #x2, y2 = [400.4, 124.9]
    #x3, y3 = [0, 176.635]

    #Calculate the unknowns of the equation y=ax^2+bx+c
    a, b, c = calc_parabola_vertex(x1, y1, x2, y2, x3, y3)

    #Define x range for which to calc parabola

    x_pos = np.arange(-400, 700, 1)
    y_pos = []

    #Calculate y values
    for x in range(len(x_pos)):
            x_val = x_pos[x]
            y = (a*(x_val**2))+(b*x_val)+c
            y_pos.append(y)

    # Plot the parabola (+ the known points)

    plt.plot(x_pos, y_pos, linestyle='-.', color='black')  # parabola line
    plt.scatter(x_pos, y_pos, color='gray')  # parabola points
    plt.scatter(x1, y1, color='r', marker="D", s=50)  # 1st known xy
    plt.scatter(x2, y2, color='g', marker="D", s=50)  # 2nd known xy
    plt.scatter(x3, y3, color='k', marker="D", s=50)  # 3rd known xy
    plt.show()


def drawset2(index):
    x = rawdata2[index]
    #x["ans"] = x["x"]/mult
    x["ans"] = x["a"] * math.sqrt(2)
    
    mult = x["cm"]/x["c"]
    print("test " + str(x["ans"] * mult * 2) )
    x1 = x["c"]
    y1 = 0

    x2 = x["c-b+a"]
    y2 = x["a"]

    x3 = 0
    y3 = x["ans"]

    a, b, c = calc_parabola_vertex(x1, y1, x2, y2, x3, y3)
    max_x, max_y = max_value(a, b, c)
    print(str(x1) + " " + str(y1) + " " + str(x2) +
          " " + str(y2) + " " + str(x3) + " " + str(y3) + " " + str(max_x)+ " " + str(max_y))
    sketch_curve(x1, y1, x2, y2, x3, y3)

    drawline(x1, y1, x2, y2)
    drawline(x2, y2, x3, y3)


def calc_and_normalize(first_c, data):
    for x in data:
        x["c-b+a"] = x["c"] - x["b"] + x["a"]
        multiplier = first_c / x["c"]
        x["c-b+a"] *= multiplier
        x["a"] *= multiplier
        x["b"] *= multiplier
        x["c"] *= multiplier


def my_curve_fit(points):
    x = []
    y = []
    for p in points:
        x.append(p[0])
        y.append(p[1])
    z = np.polyfit(x, y, 2)
    print("polynomial fit")
    print(z)
    return z

def drawset3(data):
    if len(data) == 0: 
        return
    
    first_c = data[0]["c"]
    calc_and_normalize(first_c, data);

    points = [[first_c, 0]]
    for d in data:
        x = d["c-b+a"]
        y = d["a"]
        points.append([x, y])

    coefficient = my_curve_fit(points)
    
    a = coefficient[0]
    b = coefficient[1]
    c = coefficient[2]

    points.append([0, c])
    print("ans "+str(c))

    x_pos = np.arange(-200, first_c, 1)
    y_pos = []

    #Calculate y values
    for x in range(len(x_pos)):
            x_val = x_pos[x]
            y = (a*(x_val**2))+(b*x_val)+c
            y_pos.append(y)
    
    # Plot the parabola (+ the known points)

    plt.plot(x_pos, y_pos, linestyle='-.', color='black')  # parabola line
    #plt.scatter(x_pos, y_pos, color='gray')  # parabola points
    for p in points:
        print(str(p[0]) + " " + str(p[1]))
        plt.scatter(p[0], p[1], color='r', marker="D", s=10)  # 1st known xy
    #plt.scatter(x2, y2, color='g', marker="D", s=50)  # 2nd known xy
    #plt.scatter(x3, y3, color='k', marker="D", s=50)  # 3rd known xy
    plt.show()

        #x3 = 0
        #y3 = x["ans"]

    #for p in points:
        # a, b, c = calc_parabola_vertex(x1, y1, x2, y2, x3, y3)
        # max_x, max_y = max_value(a, b, c)
        # print(str(x1) + " " + str(y1) + " " + str(x2) +
        #     " " + str(y2) + " " + str(x3) + " " + str(y3) + " " + str(max_x) + " " + str(max_y))
        # sketch_curve(x1, y1, x2, y2, x3, y3)

        # drawline(x1, y1, x2, y2)
        # drawline(x2, y2, x3, y3)

# for x in range(0, 12):
#     drawset2(x)


drawset3(rawdata3a)
drawset3(rawdata3b)
drawset3(rawdata33)
drawset3(rawdata32)

# print(rawdata)

# snell
# nisin(ti) = nrsin(tr)
#  sin(tr) = (ni/nr)sin(ti)
# ti =
# tr = sinh((ni/nr)sin(ti))


#plot generic graph
# x_pos = np.arange(-2 * math.pi, 2 * math.pi, 0.1)
# y_pos = []


# def func2plot(x):
#     return x*x

# def angle_refraction(angle_incident):
#     refract_index = 1/1.33
#     return math.degrees(math.asin(refract_index * math.sin(angle_incident)))


# def plot_func(f):
#     #Calculate y values
#     for x in range(len(x_pos)):
#         x_val = x_pos[x]
#         #y = (a*(x_val**2))+(b*x_val)+c
#         y = f(x_val)
#         y_pos.append(y)
    
#     plt.plot(x_pos, y_pos, linestyle='-.', color='black')
#     plt.show()


# plot_func(angle_refraction)

