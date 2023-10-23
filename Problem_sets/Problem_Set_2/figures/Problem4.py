import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd

def plot_spectrum(Fs, title):
    plt.figure()
    f_values = np.array([-Fs/2, 0, Fs/2])
    X_values = np.array([0.5, 1, 0.5])
    
    plt.stem(f_values, X_values, basefmt=" ", use_line_collection=True)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.title(title)
    plt.grid(True)

# For x1[n] with Fs1 = 4000 Hz
plot_spectrum(4000, 'Spectrum of x1[n]')

# For x2[n] with Fs2 = 1500 Hz
plot_spectrum(1500, 'Spectrum of x2[n] (Aliased)')

plt.tight_layout()
plt.show()


# Time duration
T = 1.0  # seconds

# Sampling frequencies
Fs1 = 4000  # Hz for x1[n]
Fs2 = 1500  # Hz for x2[n]

# Generate time vectors
t1 = np.linspace(0, T, int(T * Fs1), endpoint=False)
t2 = np.linspace(0, T, int(T * Fs2), endpoint=False)

# Generate the signals
x1 = np.cos(2000 * np.pi * t1)
x2 = np.cos(2000 * np.pi * t2)

# Play the signals
print("Playing signal with Fs1 = 4000 Hz")
sd.play(x1, Fs1)
sd.wait()
print("Playing signal with Fs2 = 1500 Hz")
sd.play(x2, Fs2)
sd.wait()