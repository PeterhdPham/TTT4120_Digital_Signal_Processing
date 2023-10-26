import numpy as np
import matplotlib.pyplot as plt

# Generate Binary White Noise
bw_noise = np.random.choice([1, -1], size=20000)

plt.figure(figsize=(10,3))
plt.stem(bw_noise, use_line_collection=True)
plt.title('Binary White Noise')
plt.show()

# Generate White Gaussian Noise
wg_noise = np.random.normal(0, 1, 20000)  # mean=0, standard deviation=1

plt.figure(figsize=(10,3))
plt.stem(wg_noise, use_line_collection=True)
plt.title('White Gaussian Noise')
plt.show()

# Generate White Uniform Noise
wu_noise = np.random.uniform(-1, 1, 20000)  # min=-1, max=1

plt.figure(figsize=(10,3))
plt.stem(wu_noise, use_line_collection=True)
plt.title('White Uniform Noise')
plt.show()
