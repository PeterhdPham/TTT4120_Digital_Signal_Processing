import numpy as np
import matplotlib.pyplot as plt

# Define the sequences
Nx = 28
x = 0.9**np.arange(Nx)

Nh = 9
h = np.ones(Nh)

# Perform linear convolution
y = np.convolve(x, h)

# Plot
plt.figure(figsize=(10, 5))
plt.stem(y, use_line_collection=True)
plt.title('Output signal y(n) using time-domain convolution')
plt.xlabel('n')
plt.ylabel('y(n)')
plt.grid(True)
plt.show()

print(f"Length of y(n), Ny = {len(y)}")
