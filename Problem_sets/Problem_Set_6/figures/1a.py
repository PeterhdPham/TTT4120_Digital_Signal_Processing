import numpy as np
import matplotlib.pyplot as plt

def X(f):
    numerator = 1 - (0.9 * np.exp(-1j*2*np.pi*f))**28
    denominator = 1 - 0.9 * np.exp(-1j*2*np.pi*f)
    return numerator / denominator

# Define the frequency range
f = np.linspace(0, 1, 1000, endpoint=False)

# Compute the magnitude of X(f)
magnitude = np.abs(X(f))

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(f, magnitude)
plt.title('Magnitude of X(f)')
plt.xlabel('Frequency (f)')
plt.ylabel('|X(f)|')
plt.grid(True)
plt.show()
