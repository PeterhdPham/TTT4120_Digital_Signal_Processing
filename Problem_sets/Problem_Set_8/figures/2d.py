from scipy.linalg import toeplitz
import numpy as np
import matplotlib.pyplot as plt
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

def PDS_estimate(order, f):
    coefficients, prediction_error_variance = solve_yule_walker(order)
    sum_coefficients = 0
    for i, c in enumerate(coefficients):
        sum_coefficients += c * np.exp(-1j * 2 * np.pi * f * (i + 1))  # i+1 because coefficients start from lag 1
    denominator = (1 - sum_coefficients)
    return prediction_error_variance / np.abs(denominator)**2

def plot_theoretical_PDS_MA(frequencies):
    H_f = 1 - 0.4 * np.exp(-1j * 2 * np.pi * frequencies)
    theoretical_PDS_MA = np.abs(H_f)**2
    plt.plot(frequencies, 10 * np.log10(theoretical_PDS_MA), label='Theoretical PDS of MA process', linestyle='--')

def PDS_estimate_plot():
    frequencies = np.linspace(-0.5, 0.5, 1000)
    plt.figure(figsize=(10, 5))

    # Plot the theoretical PDS of the MA process
    plot_theoretical_PDS_MA(frequencies)

    # Calculate and plot the AR model estimates for each order
    for order in range(1, 4):
        AR_values = [PDS_estimate(order, f) for f in frequencies]
        plt.plot(frequencies, 10 * np.log10(np.abs(AR_values)), label=f'AR[{order}] Estimate')

    plt.xlabel('Frequency')
    plt.ylabel('Power (dB)')
    plt.title('Power Density Spectrum Estimates vs Theoretical PDS of MA process')
    plt.legend()
    plt.grid(True)
    plt.show()

# Call the function to plot all the estimates and the theoretical PDS on the same figure
PDS_estimate_plot()
