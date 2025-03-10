import numpy as np
import matplotlib.pyplot as plt

N = np.arange(50, 400, 50)

p_star = {1: 0.21272877540538992, 
          2: 0.19173894182005788, 
          3: 0.17282016379879023, 
          4: 0.1557680914056046, 
          5: 0.1403985378025353, 
          6: 0.12654548976762195}

def distance(p: dict, q: dict) -> float:
    return np.max([np.abs(p[i] - q[i]) for i in range(1, 7)])

delta_bars = []
delta_stds = []
probabilities = [] #m /M

for n in N:
    count = 0
    iterations = 0

    deltas = np.zeros(100)

    while count < 100:
        iterations += 1

        sample = np.random.randint(1, 7, n)
        sample_mean = np.mean(sample)

        if (3.0 < sample_mean < 3.2):
            unique, counts = np.unique(sample, return_counts=True)
            empirical = dict(zip(unique, counts/n))

            deltas[count] = distance(p_star, empirical)

            count += 1
        
    delta_bars.append(np.mean(deltas))
    delta_stds.append(np.std(deltas))
    probabilities.append(100/iterations)

    print(f"n = {n}: M = {iterations}, P = {100/iterations}")

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

ax1.plot(N, delta_bars)
ax1.set_title(r"$\bar{\Delta}\text{ vs. } n$")
ax1.set_xlabel("n")
ax1.set_ylabel(r"$\bar{\Delta}$", rotation=0)

ax2.plot(N, delta_stds)
ax2.set_title(r"$S_{\Delta}\text{ vs. } n$")
ax2.set_xlabel("n")
ax2.set_ylabel(r"$S_{\Delta}$", rotation=0)

ax3.plot(N, probabilities)
ax3.set_title(r"$m/M\text{ vs. } n$")
ax3.set_xlabel("n")
ax3.set_ylabel(r"m/M", rotation=0)

ax4.plot(N, [1/n*np.log(p) for n, p in zip(N, probabilities)])
ax4.set_title(r"$\frac{1}{n}\log\left(\frac{m}{M}\right)\text{ vs. } n$")
ax4.set_xlabel("n")
ax4.set_ylabel(r"$\frac{1}{n}\log\left(\frac{m}{M}\right)$", rotation=0)

plt.show()
