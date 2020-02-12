# ORIE 5270 
# Homework 0 Question 2
# Name: Mrinal Ramsaha
# NetID: mar477

def gradient_descent(x0,objective,gradient,step_size=0.001,\
    max_iter=100,print_frequency=10):
    x = x0 #Initialize
    for y in range(1,max_iter+1): # Range
        x = x - step_size*gradient(x) #Iteration
        if y%print_frequency == 0: #Condition for print frequency
            print("Iteration: "+ str(y) + ", Objective " + str(objective(x)))

def objective(x):
    return # Objective Value

def gradient(x):
    return # Function statement

