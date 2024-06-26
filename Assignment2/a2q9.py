import math
from matplotlib import pyplot as plt

def normal_cdf(x : float, mu : float = 0, sigma : float = 1) -> float:
    return (1+math.erf((x-mu)/math.sqrt(2)/sigma))/2

xs = [x/10.0 for x in range(-50, 50)]
plt.plot(xs, [normal_cdf(x, sigma = 1) for x in xs], 'r-', label='mu=0, sigma = 1')
plt.plot(xs, [normal_cdf(x, sigma = 2) for x in xs], 'g--', label='mu=0, sigma = 2')
plt.plot(xs, [normal_cdf(x, sigma = 0.5) for x in xs], 'b:', label='mu=0, sigma = 0.5')
plt.plot(xs, [normal_cdf(x, mu = -1) for x in xs], 'y-.', label='mu=-1, sigma = 1')
plt.legend(loc = 4)
plt.title("Various Normal Distribution")
plt.show()