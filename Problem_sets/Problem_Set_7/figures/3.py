import numpy as np
import matplotlib.pyplot as plt


# Parameters
N = 20000
K = 20
sigma_w = np.sqrt(3/4)

# Generate white Gaussian noise w[n]
w = np.random.normal(0, sigma_w, N)

# Filter w[n] to get x[n]
# Using the given transfer function H(z) = 1 / (1 + 0.5 z^-1)
# This results in a difference equation: x[n] = w[n] - 0.5 * x[n-1]
x = np.zeros(N)
for n in range(1, N):
    x[n] = w[n] - 0.5 * x[n-1]

# Divide x[n] into non-overlapping segments of length K
num_segments = N // K
segments = np.array_split(x, num_segments)

# Compute the mean estimate for each segment
mean_estimates = [np.mean(segment) for segment in segments]
print(mean_estimates[:10])  # Display the first 10 mean estimates for verification

# Plot histogram of the mean estimates
plt.figure(figsize=(10, 6))
plt.hist(mean_estimates, bins=20, edgecolor='black', alpha=0.7)
plt.title('Histogram of Mean Estimates for $K=20$')
plt.xlabel('Mean Estimate')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# 3(c): Estimate the mean and variance of mean estimates for K=20
mean_K20 = np.mean(mean_estimates)
variance_K20 = np.var(mean_estimates)
print(mean_K20)
print(variance_K20)
# 3(d): Repeat the procedure for K=40 and K=100
K_values = [40, 100]
mean_estimates_dict = {"K=20": mean_estimates}
means = {"K=20": mean_K20}
variances = {"K=20": variance_K20}

for K in K_values:
    # Divide x[n] into non-overlapping segments of length K
    segments = np.array_split(x, N // K)
    
    # Compute the mean estimate for each segment
    mean_estimates_dict[f"K={K}"] = [np.mean(segment) for segment in segments]
    
    # Compute mean and variance
    means[f"K={K}"] = np.mean(mean_estimates_dict[f"K={K}"])
    variances[f"K={K}"] = np.var(mean_estimates_dict[f"K={K}"])
    print(means[f"K={K}"])
    print(variances[f"K={K}"])