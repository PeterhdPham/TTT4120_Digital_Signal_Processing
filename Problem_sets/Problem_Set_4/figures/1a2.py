import matplotlib.pyplot as plt
import numpy as np

def plot_transfer_function(a, subplot_idx):
    # Defining a range of omega from 0 to pi (i.e., 0 to Nyquist rate)
    omega = np.linspace(0, np.pi, 400)
    
    # Getting the z values along the unit circle for different omega
    z = np.exp(1j * omega)
    
    # Calculating the H(z) for given a
    H_z = z / (z - a)
    
    # Plotting the magnitude response of H(z)
    plt.subplot(1, 2, subplot_idx)
    plt.plot(omega, np.abs(H_z))
    plt.title(f'Magnitude Response (a={a})')
    plt.xlabel(r'$\omega$')
    plt.ylabel(r'$|H(e^{j\omega})|$')
    plt.grid(True)

# Creating a figure
plt.figure(figsize=(12, 6))

# Plot for a=0.9
plot_transfer_function(0.9, 1)

# Plot for a=-0.9
plot_transfer_function(-0.9, 2)

# Adjusting layout and displaying the plot
plt.tight_layout()
plt.show()
