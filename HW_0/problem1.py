# ORIE 5270
# Homework 0 Question 1
# Name: Mrinal Ramsaha
# NetID: mar477

n = 0.5 #step size (learning rate)
x = 0 # x_zero
delta_f_x = 2*x - 1 #Gradient 
f_x = x*x - x #Objective

for y in range(1,101):
	x = x - n*(2*x-1)
	if y%10 == 0: #every 10 iterations
		print("Iteration " + str(y) + ", Objective Value " +
	 str(x*x - x) + ", Iterate " + str(x))	 

