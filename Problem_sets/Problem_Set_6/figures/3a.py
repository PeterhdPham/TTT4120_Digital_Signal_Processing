import numpy as np
import matplotlib.pyplot as plt

# Given frequencies
f1 = 7/40
f2 = 9/40


# Number of samples for our discrete-time signal
N = 100

# Discrete-time signal
n = np.arange(N)
x_n = np.sin(2 * np.pi * f1 * n) + np.sin(2 * np.pi * f2 * n)

# Compute the DFT
X_f = np.fft.fft(x_n, N)
magnitude_X_f = np.abs(X_f)[:N//2]

# Frequency values for the DFT
f_values = np.fft.fftfreq(N)[:N//2]

# Plot
plt.figure(figsize=(10, 5))
plt.stem(f_values, magnitude_X_f, 'r', markerfmt='ro', basefmt=" ", linefmt='r')
plt.xlabel('Frequency (f)')
plt.ylabel('|X(f)|')
plt.title('Discrete Magnitude Spectrum')
plt.grid(True)
plt.xlim([0, 0.5])
plt.ylim([0, N/2 + 10])
plt.show()
