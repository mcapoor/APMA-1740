import random 
import matplotlib.pyplot as plt
import numpy as np

# 4.f
def sample_p_hat(n, s=3): 
    sample = [random.randint(1, s) for _ in range(n)]
    return [sample.count(i) / n for i in range(1, s+1)]

def print_samples():
    for n in [10, 10**2, 10**4, 10**6]: 
        print(f"n = {n}: {sample_p_hat(n)}")

#print_samples()

# 4.g
def empirical():
    count = 0
    for m in range(10**5):
        p_hat = sample_p_hat(10)
        if p_hat == [0.5, 0.3, 0.2]:
            count += 1

    print(f"Empirical probability: {count / 10**5}, True probability: {round(280/6561, 4)}")

#empirical()

# 4.h
fig = plt.figure()
axs = fig.subplots(1, 3)

for i, n in enumerate([10, 100, 1000]):
    p_hat = np.array([sample_p_hat(n) for _ in range(10**5)])
    axs[i].set_title(f'n={n}')
    axs[i].set_aspect('equal')
    im = axs[i].hist2d(p_hat[:,0], p_hat[:, 1], bins=[100, 100], range=[[0, 1], [0, 1]], density=True)
    fig.colorbar(im[3], ax=axs[i], fraction=0.046,)
plt.show()