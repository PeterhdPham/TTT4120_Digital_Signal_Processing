import numpy as np
import matplotlib.pyplot as plt

# Define the sequence x(n)
Nx = 28
n = np.arange(Nx)
x = 0.9**n

# DFT lengths
dft_lengths = [int(Nx/4), int(Nx/2), Nx, 2*Nx]

# Compute DFT for each length and plot magnitude
plt.figure(figsize=(12, 8))
for N in dft_lengths:
    X_k = np.fft.fft(x, n=N)
    plt.subplot(2, 2, dft_lengths.index(N) + 1)
    plt.stem(np.arange(N), np.abs(X_k), use_line_collection=True)
    plt.title(f'Magnitude of DFT (N={N})')
    plt.xlabel('Frequency Index (k)')
    plt.ylabel('|X[k]|')
    plt.grid(True)
plt.tight_layout()
plt.show()
