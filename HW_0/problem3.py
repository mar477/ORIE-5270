# ORIE 5270 
# Homework 0 Question 3
# Name: Mrinal Ramsaha
# NetID: mar477

# Copied from homework (question)
import numpy as np
import matplotlib.pyplot as plt
A = np.random.randn(100, 50)
x = np.ones(50)
b = A.dot(x) + 0.01*np.random.randn(100) 
step_size = 0.002
T = 1000

x_coord = [] #for plot
y_coord = [] #for plot

# Gradient Descent
def gradient_descent(x0,objective,gradient,step_size=0.001,\
    max_iter=100,print_frequency=10):
    x = x0 #Initialize
    for y in range(1,max_iter+1): # Range
        x = x - step_size*gradient(x) # Iteration
        y_coord.append(objective(x))
        x_coord.append(y)
        if y%print_frequency == 0: # Condition for print frequency
            print("Iteration: "+ str(y) + ", Objective " + str(objective(x)))
    plt.scatter(x_coord,y_coord,s=0.4)
    plt.show()

#Objective
def objective(x):
    i = np.linalg.norm(A.dot(x)-b) #||Ax-b||
    j = i ** 2 #squared
    k = j/2 #divide by 2
    return k # Objective Value

#Gradient
def gradient(x):
    i = A.dot(x) - b
    j = np.transpose(A)
    return (j.dot(i)) # Function statement

gradient_descent(x,objective,gradient,step_size,T) # Statement
