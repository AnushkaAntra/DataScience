import math
import matplotlib.pyplot as plt

SQRT_TWO_PI = math.sqrt(2 * math.pi)

def normal_pdf(x: float, mu: float = 0, sigma: float = 1) -> float:
    return (math.exp(-(x - mu) ** 2 / 2 / sigma ** 2) / (SQRT_TWO_PI * sigma))
    

def plot_line(mu: float = 0, sigma: float = 1, line_type='-') -> None:
    xs = [x/10.0 for x in range(-50, 50)]
    plt.plot(xs, [normal_pdf(x, sigma=sigma) for x in xs], line_type, label=f'mu={mu}, sigmma={sigma}')
    
plot_line(sigma=1, line_type='r-')
plot_line(sigma=2, line_type='b--')
plot_line(sigma=0.5, line_type='g:')
plot_line(mu=-1, line_type='y-.')
plt.legend()
plt.title("Various Normal pdfs")
plt.show()
    