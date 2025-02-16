import numpy as np
import matplotlib.pyplot as plt


def logistic_growth(L=100, k=0.2, x0=25, time_steps=50):
    """Simulates logistic population growth using the equation:
       f(x) = L / (1 + exp(-k(x - x0))) """

    x = np.arange(time_steps)  # Time steps from 0 to time_steps-1
    population = L / (1 + np.exp(-k * (x - x0)))  # Logistic equation

    return x, population  # Returns time and population values


# Example usage:
time, growth_curve = logistic_growth()

# Plot the growth curve
plt.plot(time, growth_curve, label="Population Growth", color='blue')
plt.xlabel("Time")
plt.ylabel("Population Size")
plt.title("Logistic Growth Curve")
plt.legend()
plt.show()
