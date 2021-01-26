import matplotlib.pyplot as plt
import math
import random


def func(x: int):
    return xxx - 6xx + 2*x + 12 


def create_random_points(numPoints: int):
    x_points = []
    y_points = []
    a, b = func(-5), func(5)
    for i in range(0, numPoints):
        x_points.append(random.uniform(-5, 5))
        y_points.append(random.uniform(a, b))
    return x_points, y_points


def set_func_graph():
    x_graph = []
    y_graph = []
    x = -5
    for i in range(0, 100):
        x_graph.append(x)
        y_graph.append(func(x))
        x += 0.1
    return x_graph, y_graph


#Code starts here

x_points, y_points = create_random_points(1000)
x_graph, y_graph = set_func_graph()

plt.title("Grafico")

k=0
while k < len(x_points):
    x, y = x_points[k], y_points[k]
    k = k+1
    if y < func(x):
        plt.scatter(x,y,color='red')
    else:
        plt.scatter(x,y,color='blue')

plt.scatter(x_points[0],y_points[0],color='red')
plt.plot(x_graph, y_graph)
plt.show()