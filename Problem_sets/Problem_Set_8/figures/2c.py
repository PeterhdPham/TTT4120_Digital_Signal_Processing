from scipy.linalg import toeplitz
import numpy as np
gamma_xx = {0: 1.16, 1: -0.4, -1: -0.4}

# Function to create the Yule-Walker matrix and vector for a given order
def create_yule_walker(order):
    # Create the autocorrelation matrix (symmetric Toeplitz matrix)
    r = [gamma_xx[i] if i in gamma_xx else 0 for i in range(order)]
    R = toeplitz(r)
    # Create the autocorrelation vector (RHS of the Yule-Walker equations)
    b = np.array([gamma_xx[i + 1] if (i + 1) in gamma_xx else 0 for i in range(order)])
    return R, b

# Function to solve the Yule-Walker equations and find the prediction error variance
def solve_yule_walker(order):
    R, b = create_yule_walker(order)
    # Solve the Yule-Walker equations for the AR coefficients
    a = np.linalg.solve(R, b)
    # Calculate the prediction error variance
    prediction_error_variance = gamma_xx[0] - np.dot(a, b)
    return a, prediction_error_variance

# Calculate the coefficients and prediction error variances for orders 1, 2, and 3
coefficients_order_1, variance_order_1 = solve_yule_walker(1)
coefficients_order_2, variance_order_2 = solve_yule_walker(2)
coefficients_order_3, variance_order_3 = solve_yule_walker(3)

print(coefficients_order_1, variance_order_1)
print(coefficients_order_2, variance_order_2)
print(coefficients_order_3, variance_order_3)