import matplotlib.pyplot as plt
import numpy as np

# Function to plot pole-zero
def plot_pole_zero(a, subplot):
    zeros = np.array([0])  # zero is always at z=0
    poles = np.array([a])  # pole is at z=a
    
    # Creating the subplot
    plt.subplot(1, 2, subplot)
    
    # Plotting the unit circle
    unit_circle = plt.Circle((0,0), 1, color='gray', fill=False)
    plt.gca().add_patch(unit_circle)

    # Plotting poles and zeros
    plt.scatter(poles.real, poles.imag, color='r', marker='x', label='Pole')
    plt.scatter(zeros.real, zeros.imag, color='b', marker='o', label='Zero')
    # for zero in zeros:
    #     plt.text(zero.real, zero.imag, ' 0', verticalalignment='bottom', horizontalalignment='right', color='blue')
    # for pole in poles:
    #     plt.text(pole.real, pole.imag, ' x', verticalalignment='bottom', horizontalalignment='left', color='red')
    
    # Axis settings
    plt.axhline(0, color='black', lw=1)
    plt.axvline(0, color='black', lw=1)
    plt.xlim([-1.5, 1.5])
    plt.ylim([-1.5, 1.5])
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True)
    plt.title(f"Pole-zero plot (a={a})")
    plt.xlabel('Real')
    plt.ylabel('Imaginary')
    plt.legend()

# Setting up the figure
plt.figure(figsize=(12, 6))

# Plot for a=0.9
plot_pole_zero(0.9, 1)

# Plot for a=-0.9
plot_pole_zero(-0.9, 2)

# Displaying the plot
plt.tight_layout()
plt.show()
