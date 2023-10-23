import numpy as np
import matplotlib.pyplot as plt

# Given frequencies
f1 = 7/40
f2 = 9/40

# Generate the signal segment of length 100
N_100 = 100
n_100 = np.arange(N_100)
x_n_100 = np.sin(2 * np.pi * f1 * n_100) + np.sin(2 * np.pi * f2 * n_100)

# Plot the generated signal
# plt.figure(figsize=(10, 5))
# plt.stem(n_100, x_n_100, 'b', markerfmt='bo', basefmt=" ", linefmt='b')
# plt.xlabel('Sample Number (n)')
# plt.ylabel('x(n)')
# plt.title('Signal Segment of Length 100')
# plt.grid(True)
# plt.show()


# Compute DFT of length 1024 for the signal segment
DFT_length_1024 = 1024
X_f_1024 = np.fft.fft(x_n_100, DFT_length_1024)
magnitude_X_f_1024 = np.abs(X_f_1024)[:DFT_length_1024//2]

# Frequency values for the DFT
f_values_1024 = np.fft.fftfreq(DFT_length_1024)[:DFT_length_1024//2]

# # Plot the magnitude spectrum
# plt.figure(figsize=(10, 5))
# plt.plot(f_values_1024, magnitude_X_f_1024, 'g')
# plt.xlabel('Frequency (f)')
# plt.ylabel('|X(f)|')
# plt.title('Estimated Magnitude Spectrum (DFT length = 1024)')
# plt.grid(True)
# plt.xlim([0, 0.5])
# plt.ylim([0, max(magnitude_X_f_1024) + 10])
# plt.show()

# Define segment lengths and DFT length
segment_lengths = [1000, 30, 10]
DFT_length = 1024

# Compute DFT for each segment length and store the magnitude spectra
magnitude_spectra = {}

for length in segment_lengths:
    n_segment = np.arange(length)
    x_n_segment = np.sin(2 * np.pi * f1 * n_segment) + np.sin(2 * np.pi * f2 * n_segment)
    X_f_segment = np.fft.fft(x_n_segment, DFT_length)
    magnitude_spectra[length] = np.abs(X_f_segment)[:DFT_length//2]

# Plot magnitude spectra for each segment length
plt.figure(figsize=(15, 10))
for i, length in enumerate(segment_lengths, 1):
    plt.subplot(2, 2, i)
    plt.plot(f_values_1024, magnitude_spectra[length], label=f'Segment Length = {length}')
    plt.xlabel('Frequency (f)')
    plt.ylabel('|X(f)|')
    plt.title(f'Estimated Magnitude Spectrum (Segment Length = {length})')
    plt.grid(True)
    plt.xlim([0, 0.5])
    plt.ylim([0, max(magnitude_spectra[length]) + 10])
    plt.legend()

plt.tight_layout()
plt.show()


# Define DFT lengths for part (c)
DFT_lengths_c = [256, 128]

# Compute DFT for each length and store the magnitude spectra
magnitude_spectra_c = {}

for dft_length in DFT_lengths_c:
    X_f_c = np.fft.fft(x_n_100, dft_length)
    magnitude_spectra_c[dft_length] = np.abs(X_f_c)[:dft_length//2]

# Frequency values for the DFTs in part (c)
f_values_256 = np.fft.fftfreq(DFT_lengths_c[0])[:DFT_lengths_c[0]//2]
f_values_128 = np.fft.fftfreq(DFT_lengths_c[1])[:DFT_lengths_c[1]//2]

# Plot magnitude spectra for each DFT length in part (c)
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(f_values_256, magnitude_spectra_c[DFT_lengths_c[0]], label=f'DFT Length = {DFT_lengths_c[0]}')
plt.xlabel('Frequency (f)')
plt.ylabel('|X(f)|')
plt.title(f'Estimated Magnitude Spectrum (DFT length = {DFT_lengths_c[0]})')
plt.grid(True)
plt.xlim([0, 0.5])
plt.ylim([0, max(magnitude_spectra_c[DFT_lengths_c[0]]) + 10])
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(f_values_128, magnitude_spectra_c[DFT_lengths_c[1]], label=f'DFT Length = {DFT_lengths_c[1]}')
plt.xlabel('Frequency (f)')
plt.ylabel('|X(f)|')
plt.title(f'Estimated Magnitude Spectrum (DFT length = {DFT_lengths_c[1]})')
plt.grid(True)
plt.xlim([0, 0.5])
plt.ylim([0, max(magnitude_spectra_c[DFT_lengths_c[1]]) + 10])
plt.legend()

plt.tight_layout()
plt.show()
