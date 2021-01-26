import matplotlib.pyplot as plt
import math
import random
import numpy as np

# GRADED FUNCTION: initialize_with_zeros

def func(x):
    return x*x*x - 6*x*x + 2*x + 12 


def initialize_parameters(n_x, n_y, n_h = 1):
    """
    Argument:
    n_x -- size of the input layer
    n_h -- size of the hidden layer
    n_y -- size of the output layer
    
    Returns:
    parameters -- python dictionary containing your parameters:
                    W1 -- weight matrix of shape (n_h, n_x)
                    b1 -- bias vector of shape (n_h, 1)
                    W2 -- weight matrix of shape (n_y, n_h)
                    b2 -- bias vector of shape (n_y, 1)
    """
    
    np.random.seed(1)
    
    ### START CODE HERE ### (≈ 4 lines of code)
    W1 = np.random.randn(n_h, n_x)*0.01
    b1 = np.zeros((n_h, 1))
    ### END CODE HERE ###
    
    assert(W1.shape == (n_h, n_x))
    assert(b1.shape == (n_h, 1))
    
    parameters = {"W1": W1,
                  "b1": b1,
                }
    
    return parameters    


def initialize_X_and_Y(numPoints):
    x_points = []
    y_points = []
    for i in range(0, numPoints):
        x = random.uniform(-5, 5)
        x_points.append(x)
        y_points.append(func(x))
    return x_points, y_points



# def create_random_points(numPoints: int):
#     x_points = []
#     y_points = []
#     a, b = func(-5), func(5)
#     for i in range(0, numPoints):
#         x_points.append(random.uniform(-5, 5))
#         y_points.append(random.uniform(a, b))
#     return x_points, y_points


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

x_points, y_points = create_random_points(800)
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