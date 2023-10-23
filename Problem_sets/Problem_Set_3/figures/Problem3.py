import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz

# Frequency response for the first system: y[n] = x[n] + 2x[n-1] + x[n-2]
def system1():
    b = np.array([1, 2, 1])  # Coefficients for x[n]
    a = np.array([1])        # Coefficients for y[n]

    w, h = freqz(b, a, worN=1024)

    plt.figure()
    plt.subplot(2, 1, 1)
    plt.plot(w, np.abs(h))
    plt.xlabel('Frequency (rad/sample)')
    plt.ylabel('Magnitude')
    plt.title('Magnitude Response of System 1')
    plt.grid()

    plt.subplot(2, 1, 2)
    plt.plot(w, np.angle(h))
    plt.xlabel('Frequency (rad/sample)')
    plt.ylabel('Phase (radians)')
    plt.title('Phase Response of System 1')
    plt.grid()

    plt.tight_layout()
    plt.show()

# Frequency response for the second system: y[n] = -0.9y[n-1] + x[n]
def system2():
    b = np.array([1])        # Coefficients for x[n]
    a = np.array([1, 0.9])   # Coefficients for y[n]

    w, h = freqz(b, a, worN=1024)

    plt.figure()
    plt.subplot(2, 1, 1)
    plt.plot(w, np.abs(h))
    plt.xlabel('Frequency (rad/sample)')
    plt.ylabel('Magnitude')
    plt.title('Magnitude Response of System 2')
    plt.grid()

    plt.subplot(2, 1, 2)
    plt.plot(w, np.angle(h))
    plt.xlabel('Frequency (rad/sample)')
    plt.ylabel('Phase (radians)')
    plt.title('Phase Response of System 2')
    plt.grid()

    plt.tight_layout()
    plt.show()

# Plot both systems
system1()
system2()
