import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.stats import kurtosis

count = 0
sample = np.zeros((10000, 1))
while True:
    sample = np.random.normal(0, 1, (10000, 1))

    if np.mean(sample) > 0.038:
        break 
    else: 
        count += 1

        if count % 1000 == 0:
            print(f"Iteration: {count}")

fig = plt.figure()
ax = fig.add_subplot(111)
ax.hist(sample, bins=100, density=True)
fig.suptitle(r"$\bar X_{10000}$")
plt.show()

print(f"Number of iterations: {count}")
print(f"Mean: {np.mean(sample)}")
print(f"Standard deviation: {np.std(sample)}")
print(f"Kurtois: {kurtosis(sample)}")
