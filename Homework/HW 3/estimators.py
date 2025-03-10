import numpy as np 
import matplotlib.pyplot as plt

n = 5

def p1(p): 
    return 0.5

def p2(p): 
    return np.average(np.random.binomial(1, p, n))

def p3(p):
    return n/(n+2)*p1(p) + n/(n+2)*p2(p)

p_span = np.linspace(0, 1, 100)

plt.xlabel('p')
plt.ylabel('MSE')
plt.plot(p_span, [(0.5 - p)**2 for p in p_span], label=r'$\hat p_1$')
plt.plot(p_span, [p*(1-p)/n for p in p_span] , label=r'$\hat p_2$')
plt.plot(p_span, [((4-n)*p**2 + (n-4)*p + 1)/(n+2)**2 for p in p_span] , label=r'$\hat p_3$')
plt.legend()
plt.show()