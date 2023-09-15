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

# a)
def problem1a():
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
# problem1a()
# b)

def Y_omega(omega, M):
    return (np.sin(omega*(M+(1/2)))/np.sin(omega/2))
def problem1b():
    plt.figure()
    plt.subplot(2, 1, 1)
    plt.stem(n_values, y_values)
    plt.xlabel('n')
    plt.ylabel('y[n]')
    plt.title('y[n]')
    plt.grid(True)
    M=10
    Y_values = [Y_omega(om, M) for om in omega]
    plt.subplot(2, 1, 2)
    plt.plot(omega, Y_values)
    plt.xlabel('omega')
    plt.ylabel('Y(omega)')
    plt.title('Y(omega)')
    plt.grid(True)

    plt.tight_layout()
    plt.show()
# problem1b()

def z_n(n, N):
    n_mod = n % N
    if n_mod == 0:
        return 2
    elif n_mod == 1 or n_mod == N-1:
        return 1
    else:
        return 0

def c_k(k, N):
    return 2/N * (1 + np.cos(2 * np.pi * k / N))

def problem1d():
    N = 10
    n_values = np.arange(-30, 30)  # For example, from -30 to 30
    z_values = [z_n(n, N) for n in n_values]
    
    plt.figure()
    plt.subplot(2, 1, 1)
    plt.stem(n_values, z_values)
    plt.xlabel('n')
    plt.ylabel('z[n]')
    plt.title('z[n]')
    plt.grid(True)
    
    k_values = np.arange(-5, 6)  # From -N/2 to N/2
    omega_values = 2 * np.pi * k_values / N  # omega = 2*pi*k/N
    ck_values = [c_k(k, N) for k in k_values]
    
    plt.subplot(2, 1, 2)
    plt.stem(omega_values, ck_values)
    plt.xlabel('omega')
    plt.ylabel('c_k')
    plt.title('Fourier Coefficients c_k')
    plt.grid(True)

    plt.tight_layout()
    plt.show()

problem1d()