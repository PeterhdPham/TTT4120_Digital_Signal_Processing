import numpy as np
import matplotlib.pyplot as plt

# Problem 5:
def x_n(n):
    if 0<= n<= 2:
        return n+1
    else:
        return 0
    
n_values = np.arange(-5, 15)  # A range of n values
x_values = [x_n(n) for n in n_values]
plt.figure()

def unit_impulse(n):
    if n==0:
        return 1
    else:
        return 0

def h_1_n(n):
    return unit_impulse(n) + unit_impulse(n-1) + unit_impulse(n-2)

def h_2_n(n):
    if 0<=n<=10:
        return 0.9**n
    else:
        return 0
1
h_1values = [h_1_n(n) for n in n_values]
h_2values = [h_2_n(n) for n in n_values]

y_1values = np.convolve(x_values,h_1values)
y_2values = np.convolve(y_1values, h_2values)
n_values_y1 = np.arange(len(y_1values)) 

n_values_y2 = np.arange(len(y_2values)) 

y_1values_interchanged = np.convolve(x_values,h_2values)
y_2values_interchanged = np.convolve(y_1values_interchanged, h_1values)
n_values_y1_interchanged = np.arange(len(y_1values_interchanged)) 
n_values_y2_interchanged = np.arange(len(y_2values_interchanged)) 

# (a) Compute and sketch x[n]
def problem_5a():
    plt.stem(n_values, x_values, label="x[n]")
    plt.xlabel('n')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.title('Problem 5a')
    plt.grid(True)
    plt.show()
# problem_5a()

def problem_5ay():
    plt.stem(n_values_y1, y_1values, label="y_1[n]")
    plt.xlabel('n')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.title('Problem 5a')
    plt.grid(True)
    plt.show()
problem_5ay()

# (b) Compute and plot the signal y2[n]. 
def problem_5b():
    plt.stem(n_values_y2, y_2values, label="y_2[n]")
    plt.xlabel('n')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.title('Problem 5b')
    plt.grid(True)
    plt.show()
# problem_5b()

# (d) Compute and plot the signal y1[n] and y2[n] when the order of the two systems is interchanged

def problem_5d1():
    plt.stem(n_values_y1_interchanged, y_1values_interchanged, label="y_1[n]")
    plt.xlabel('n')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.title('Problem 5d')
    plt.grid(True)
    plt.show()
problem_5d1()

def problem_5d2():
    plt.stem(n_values_y2_interchanged, y_2values_interchanged, label="y_2[n]")
    plt.xlabel('n')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.title('Problem 5d')
    plt.grid(True)
    plt.show()
problem_5d1()