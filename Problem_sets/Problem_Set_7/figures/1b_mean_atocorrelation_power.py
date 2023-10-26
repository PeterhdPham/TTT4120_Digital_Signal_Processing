import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch

# Number of samples and noise length
N = 20000

# Function to compute and print stats
def compute_stats(noise, title):
    # Mean
    # mean_value = np.mean(noise)
    # print(f"Mean Value of {title}: {mean_value}")

    # Autocorrelation
    autocorr = np.correlate(noise, noise, mode='full')
    autocorr = autocorr[autocorr.size // 2:]

    mid_point = autocorr.size // 2
    plt.figure(figsize=(10,4))
    plt.plot(range(-10, 11), autocorr[mid_point-10:mid_point+11])
    plt.title(f"Autocorrelation of {title}")
    plt.xlabel('Lag')
    plt.ylabel('Autocorrelation')
    plt.show()

    # Power Density Spectrum using Welch's method
    frequencies, psd = welch(noise, fs=1.0, nperseg=1024)

    plt.figure(figsize=(10,4))
    plt.semilogy(frequencies, psd)
    plt.title(f"Power Density Spectrum of {title}")
    plt.xlabel("Frequency")
    plt.ylabel("Power/Frequency")
    plt.show()

# 1. Binary White Noise
bw_noise = np.random.choice([1.0, -1.0], size=N)
compute_stats(bw_noise, "Binary White Noise")

# 2. White Gaussian Noise
wg_noise = np.random.normal(0, 1, N)
compute_stats(wg_noise, "White Gaussian Noise")

# 3. White Uniform Noise
wu_noise = np.random.uniform(-1, 1, N)
compute_stats(wu_noise, "White Uniform Noise")
