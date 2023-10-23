import numpy as np
import matplotlib.pyplot as plt

def compute_dtft(x, f):
    n = np.arange(len(x))
    e_term = np.exp(-1j * 2 * np.pi * f[:, np.newaxis] * n)
    X_f = np.sum(x * e_term, axis=1)
    return X_f

# Define the sequence x(n)
Nx = 28
n = np.arange(Nx)
x = 0.9**n

# Compute DTFT over a dense set of frequency points for visualization
f_dense = np.linspace(0, 1, 1000, endpoint=False)
X_f_dense = compute_dtft(x, f_dense)

# DFT lengths
dft_lengths = [int(Nx/4), int(Nx/2), Nx, 2*Nx]

# Plot DTFT and DFTs
plt.figure(figsize=(15, 10))
for N in dft_lengths:
    # Compute DFT
    X_k = np.fft.fft(x, n=N)
    f_dft = np.arange(N) / N
    
    # Plotting
    plt.subplot(2, 2, dft_lengths.index(N) + 1)
    plt.plot(f_dense, np.abs(X_f_dense), label='DTFT', color='blue')
    plt.stem(f_dft, np.abs(X_k), linefmt='r-', markerfmt='ro', basefmt=" ", use_line_collection=True, label=f'DFT (N={N})')
    plt.title(f'Magnitude of DFT (N={N}) and DTFT')
    plt.xlabel('Normalized Frequency (f)')
    plt.ylabel('Magnitude')
    plt.grid(True)
    plt.legend()
plt.tight_layout()
plt.show()
