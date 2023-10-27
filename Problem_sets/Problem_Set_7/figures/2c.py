import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter
import math
# Number of samples
N = 20000
sigma_w2 = 3/4
b = [1]  # numerator coefficients of the filter
a = [1, 0.5]  # denominator coefficients of the filter

# White Gaussian Noise
wg_noise = np.random.normal(0, np.sqrt(sigma_w2), N)

x = lfilter(b, a, wg_noise)

# plt.figure(figsize=(10,4))
# plt.stem(wg_noise, use_line_collection=True)
# plt.title('Amplitude Distribution of White Gaussian Noise')
# plt.xlabel('Amplitude')
# plt.ylabel('Probability Density')
# plt.show()

# plt.figure(figsize=(10,4))
# plt.stem(x, use_line_collection=True)
# plt.title('Random signal $x[n]$')
# plt.xlabel('Amplitude')
# plt.ylabel('n')
# plt.show()

def mean_estimator(x):
    N=len(x)
    sum_x=0
    for n in range(N):
        sum_x+=x[n]
    return sum_x/N

print(f'Mean estimator: ', mean_estimator(x))

def autocorrelation_function_estimator(x, l):
    N=len(x)
    sum_x_plus_lag=0
    for n in range(N-np.abs(l)-1):
        sum_x_plus_lag+=x[n]*x[n+np.abs(l)]
    return (sum_x_plus_lag)/(N-np.abs(l))

def plot_autocorelation_function_estimator(x, min_lag, max_lag):
    lags = range(min_lag, max_lag + 1)  # Including max_lag
    autocorr_values = [autocorrelation_function_estimator(x, l) for l in lags]
    n = np.arange(-10, 11)
    y = (1/2)**(-n)
    # Plotting
    plt.figure(figsize=(10, 5))
    plt.stem(lags, autocorr_values, use_line_collection=True)
    plt.stem(n, y, use_line_collection=True)
    plt.xlabel('Lag')
    plt.ylabel('Autocorrelation')
    plt.title('Estimated Autocorrelation Function')
    plt.grid(True)
    plt.show()

plot_autocorelation_function_estimator(x, -10, 10)

def compute_autocorrelation(x, max_lag=1000):
    """Compute the autocorrelation for all lags up to max_lag."""
    return [autocorrelation_function_estimator(x, l) for l in range(-max_lag, max_lag + 1)]

def optimized_power_density_spectrum_estimator(autocorr_values, f, max_lag=1000):
    lags = np.arange(-max_lag, max_lag + 1)
    return np.sum(autocorr_values * np.exp(-1j * 2 * np.pi * f * lags))

def optimized_plot_power_density_spectrum_estimator(x, f_min, f_max, num_points=1000, max_lag=1000):
    frequencies = np.linspace(f_min, f_max, num_points)
    autocorr_values = compute_autocorrelation(x, max_lag)
    
    # Compute power density spectrum for each frequency using the precomputed autocorrelation values
    Pxx_values = [optimized_power_density_spectrum_estimator(autocorr_values, f, max_lag) for f in frequencies]
    
    # Plotting
    plt.figure(figsize=(10, 5))
    plt.plot()
    plt.plot(frequencies, np.abs(Pxx_values))
    plt.xlabel('Frequency')
    plt.ylabel('Power')
    plt.title('Estimated Power Density Spectrum (Optimized)')
    plt.grid(True)
    plt.show()

# Testing the optimized function for frequencies from -0.5 to 0.5
# optimized_plot_power_density_spectrum_estimator(x, -0.5, 0.5)
P_hat_computed = np.mean(np.abs(x)**2)
print(P_hat_computed)