import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

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

# Task (c)
def play_fixed_nomralized_frequenxy(f1, Fs_list):
    for Fs in Fs_list:
        x_n = generate_sequence(1, f1, Fs, 4)
        sd.play(x_n, samplerate=Fs)
        sd.wait()
        print(f"Played sound with sampling rate {Fs} Hz and normalized frequency {f1}")


# Task (d)
def play_fixed_sampling_rate(F1_list, Fs):
    for F1 in F1_list:
        f1 = F1 / Fs  # Compute normalized frequency
        x_n = generate_sequence(1, f1, Fs, 4)
        sd.play(x_n, samplerate=Fs)
        sd.wait()
        print(f"Played sound with physical frequency {F1} Hz and normalized frequency {f1}")

def play_corresponding_normalized_frequency(Fs_list, f1_list):
    i=0
    for Fs in Fs_list:
        x_n = generate_sequence(1, f1_list[i], Fs, 4)
        sd.play(x_n, samplerate=Fs)
        sd.wait()
        print(f"Played sound with sampling rate {Fs} Hz and correspondingnormalized frequency {f1_list[i]}")
        i+=1

if __name__ == "__main__":
   
    # # Task (b)
    # x_n = generate_sequence(1, 0.1, 6000, 4)
    # plt.stem(x_n[:100], 'b', markerfmt='bo', basefmt=" ", linefmt='b')
    # plt.xlabel('Sample index n')
    # plt.ylabel('Amplitude')
    # plt.title("First 100 samples of x[n]")
    # plt.grid(True)
    # plt.show()
    
    # # Task (c)
    # Fs_list = [1000, 3000, 12000]
    # f1= 0.3
    # play_fixed_nomralized_frequenxy(f1, Fs_list)
    
    # Task (d)
    Fs = 8000
    F1_list = [1000, 3000, 6000]
    # play_fixed_sampling_rate(F1_list, Fs)

    f1_list = [1000/Fs, 3000/Fs, 6000/Fs]
    play_corresponding_normalized_frequency(F1_list, f1_list)


    