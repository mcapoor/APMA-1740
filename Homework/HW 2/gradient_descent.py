import numpy as np

lambda0 = 1/6
ep = 1e-6

def Z(l):
    return sum([(1/6)*np.exp(l*x) for x in range(1, 7)])

def expectation(l):
    return sum([(1/6)*x*np.exp(l*x)/Z(l) for x in range(1, 7)])

lambda1 = lambda0 - (expectation(lambda0) - 3.2)

count= 0
while np.abs(lambda1 - lambda0) > ep:
    count +=1
    lambda0 = lambda1
    lambda1 = lambda0 - 0.001*(expectation(lambda0) - 3.2)


print(f"Iterations: {count}, lambda = {lambda1}")

for x in range(1, 7):
    print(f"p{x} = {(1/6)*1/Z(lambda1)*np.exp(lambda1*x)}")