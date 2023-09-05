import numpy as np
import matplotlib.pyplot as plt
# import sounddevice as sd

# Task (b)
def generate_sequence(A, f1, Fs, T):
    """
    A: amplitude
    f1: normalized frequency
    Fs: sampling rate in Hz
    T: total time in seconds
    """
    n = np.arange(0, T * Fs)  # Time index
    x_n = A * np.cos(2 * np.pi * f1 * n)
    return x_n
def physical_frequencies(Fs, f1):
    return Fs*f1
# Task (c)
def play_sound(f1, Fs_list):
    for Fs in Fs_list:
        x_n = generate_sequence(1, f1, Fs, 4)
        # sd.play(x_n, samplerate=Fs)
        # sd.wait()

# Task (d)
def play_and_comment(F1_list, Fs):
    for F1 in F1_list:
        f1 = F1 / Fs  # Compute normalized frequency
        x_n = generate_sequence(1, f1, Fs, 4)
        # sd.play(x_n, samplerate=Fs)
        # sd.wait()
        print(f"Played sound with physical frequency {F1} Hz and normalized frequency {f1}")

if __name__ == "__main__":
    # Task (a)
    Fs = 6000
    f1 = 3
    F1 = physical_frequencies(Fs, f1)
    print(f"Physical frequency corresponding to f1 = {f1} is F1 = {F1} Hz")
    
    # Task (b)
    x_n = generate_sequence(1, 0.1, 6000, 4)
    plt.plot(x_n[:100])
    plt.title("First 100 samples of x[n]")
    plt.show()
    
    # Task (c)
    Fs_list = [1000, 3000, 12000]
    play_sound(f1, Fs_list)
    
    # Task (d)
    Fs = 8000
    F1_list = [1000, 3000, 6000]
    play_and_comment(F1_list, Fs)
