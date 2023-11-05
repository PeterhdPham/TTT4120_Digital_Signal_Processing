import numpy as np
import matplotlib.pyplot as plt

# Number of samples for the white noise and the FFT
N = 10000
# Generate white Gaussian noise
w = np.random.normal(0, 1, N)

# Apply the MA process to the white noise
x = w - 0.4 * np.roll(w, 1)
x[0] = w[0]  # Since np.roll wraps around, set the first value manually

# Calculate the autocorrelation function of the MA process
r_xx = np.correlate(x, x, mode='full') / N
r_xx = r_xx[N-1:]  # Take the second half of the result

# Calculate the PDS using the FFT of the autocorrelation function
pds_x = np.fft.fft(r_xx, 2*N)  # Zero-padding for better frequency resolution
freq = np.fft.fftfreq(2*N, 1)  # Frequency vector

# Plot the Power Density Spectrum
plt.figure(figsize=(10, 6))
plt.plot(freq, 10 * np.log10(np.abs(pds_x)), label='Estimated PDS of x(n)')
plt.title('Power Density Spectrum of the MA Process')
plt.xlabel('Frequency')
plt.ylabel('Power/Frequency (dB/Hz)')
plt.grid()
plt.legend()
plt.show()
