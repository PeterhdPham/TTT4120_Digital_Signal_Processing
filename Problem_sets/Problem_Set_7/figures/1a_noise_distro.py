import numpy as np
import matplotlib.pyplot as plt

# Number of samples
N = 20000

# 1. Binary White Noise
bw_noise = np.random.choice([1.0, -1.0], size=N)

plt.figure(figsize=(10,4))
plt.hist(bw_noise, bins=3, density=True)
plt.title('Amplitude Distribution of Binary White Noise')
plt.xlabel('Amplitude')
plt.ylabel('Probability Density')
plt.show()

# 2. White Gaussian Noise
wg_noise = np.random.normal(0, 1, N)

plt.figure(figsize=(10,4))
plt.hist(wg_noise, bins=100, density=True)
plt.title('Amplitude Distribution of White Gaussian Noise')
plt.xlabel('Amplitude')
plt.ylabel('Probability Density')
plt.show()

# 3. White Uniform Noise
wu_noise = np.random.uniform(-1, 1, N)

plt.figure(figsize=(10,4))
plt.hist(wu_noise, bins=100, density=True)
plt.title('Amplitude Distribution of White Uniform Noise')
plt.xlabel('Amplitude')
plt.ylabel('Probability Density')
plt.show()
