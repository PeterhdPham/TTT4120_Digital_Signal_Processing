import numpy as np
import matplotlib.pyplot as plt

# Define the sequences
Nx = 28
x = 0.9**np.arange(Nx)

Nh = 9
h = np.ones(Nh)

# Perform linear convolution
y = np.convolve(x, h)

# Frequency-domain convolution function
def freq_domain_convolution(x, h, N):
    X = np.fft.fft(x, n=N)
    H = np.fft.fft(h, n=N)
    Y = X * H
    return np.fft.ifft(Y)

# Choose DFT/IDFT lengths
N_lengths = [int(len(y)/4), int(len(y)/2), len(y), 2*len(y)]

for N in N_lengths:
    y_freq = freq_domain_convolution(x, h, N)
    
    plt.figure(figsize=(10, 5))
    plt.stem(y, use_line_collection=True, linefmt='C0-', markerfmt='C0o', label='Time-domain convolution')
    plt.stem(np.real(y_freq), use_line_collection=True, linefmt=f'C1-', markerfmt=f'C1o', label=f'Frequency-domain convolution (N={N})')
    
    plt.title(f'Comparison for DFT Length = {N}')
    plt.xlabel('n')
    plt.ylabel('y(n)')
    plt.legend()
    plt.grid(True)
    plt.show()
 