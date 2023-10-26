import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

# Generate Binary White Noise
bw_noise = np.random.choice([1.0, -1.0], size=100000)

# plt.figure(figsize=(10,3))
# plt.stem(bw_noise, use_line_collection=True)
# plt.title('Binary White Noise')
# plt.show()

# Play the sound
print('Playing binary white noise')
sd.play(bw_noise, samplerate=44100)
sd.wait()
print('Finished playing binary white noise')

# Generate White Gaussian Noise
wg_noise = np.random.normal(0, 1, 100000)  # mean=0, standard deviation=1

# plt.figure(figsize=(10,3))
# plt.stem(wg_noise, use_line_collection=True)
# plt.title('White Gaussian Noise')
# plt.show()

# Play the sound
print('Playing binary Gaussian noise')
sd.play(wg_noise, samplerate=44100)
sd.wait()
print('Finished playing Gaussian white noise')

# Generate White Uniform Noise
wu_noise = np.random.uniform(-1, 1, 100000)  # min=-1, max=1

# plt.figure(figsize=(10,3))
# plt.stem(wu_noise, use_line_collection=True)
# plt.title('White Uniform Noise')
# plt.show()

# Play the sound
print('Playing Uniform white noise')
sd.play(wu_noise, samplerate=44100)
sd.wait()
print('Finished playing Uniform white noise')
