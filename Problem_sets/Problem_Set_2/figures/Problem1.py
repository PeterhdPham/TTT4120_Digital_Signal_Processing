import matplotlib.pyplot as plt
import numpy as np

# Function definitions
def x_n(n): 
    if n == -1 or n == 1:
        return 1
    if n == 0:
        return 2 
    else:
        return 0

def y_n(n, M):
    if -M <= n <= M:
        return 1
    else:
        return 0

def X_omega(omega):
    return 2 + 2 * np.cos(omega)

# Variables
omega = np.arange(-np.pi, np.pi, 0.1)
n_values = np.arange(-5, 5)
x_values = [x_n(n) for n in n_values]
y_values = [y_n(n, 1) for n in n_values]
X_values = [X_omega(om) for om in omega]

# Problem 1

# a: Plotting
plt.figure()
plt.subplot(2, 1, 1)
plt.stem(n_values, x_values)
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('x[n]')
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(omega, X_values)
plt.xlabel('omega')
plt.ylabel('X(omega)')
plt.title('X(omega)')
plt.grid(True)

plt.tight_layout()
plt.show()


# (b) Sketch x[n-k] for k=3 and k=-3
# def problem_1b1():
#     plt.stem(n_values-3, x_values, label="x[n]")
#     plt.xlabel('n')
#     plt.ylabel('Amplitude')
#     plt.legend()
#     plt.title('Problem 1b')
#     plt.grid(True)
#     plt.show() 
# problem_1b1()
# def problem_1b2():
#     plt.stem(n_values+3, x_values, label="x[n]")
#     plt.xlabel('n')
#     plt.ylabel('Amplitude')
#     plt.legend()
#     plt.title('Problem 1b')
#     plt.grid(True)
#     plt.show()
# problem_1b2()

# # (c) Sketch x[-n]
# def problem_1c():
#     plt.stem(-1*n_values, x_values, label="x[n]")
#     plt.xlabel('n')
#     plt.ylabel('Amplitude')
#     plt.legend()
#     plt.title('Problem 1c')
#     plt.grid(True)
#     plt.show()
# problem_1c()

# # (d) Sketch x[5-n]
# def problem_1d():
#     plt.stem(-1*n_values+5, x_values, label="x[n]")
#     plt.xlabel('n')
#     plt.ylabel('Amplitude')
#     plt.legend()
#     plt.title('Problem 1d')
#     plt.grid(True)
#     plt.show()
# problem_1d()

# # (e) Sketch x[n] * y[n]
# def problem_1e():
#     def x_n_y_n(n):
#         return x_n(n)*y_n(n)
#     xy_values = [x_n_y_n(n) for n in n_values]

#     plt.stem(n_values, xy_values, label="x[n]*y[n]")
#     plt.xlabel('n')
#     plt.ylabel('Amplitude')
#     plt.legend()
#     plt.title('Problem 1e')
#     plt.grid(True)
#     plt.show()
# problem_1e()



# # (h) Compute the energy of the signal x[n]

# def problem_1h():
#     e=0 
#     for n in n_values:
#         e+=x_n(n)*x_n(n)
    
#     print("The energy og the signal x[n] = ",e)
# problem_1h()

# # Energy = sum of (x[n])^2 for all n

