import numpy as np


def logistic_growth(L=100, k=0.2, x0=25, time_steps=50):
    """Simulates logistic population growth."""

    x = np.arange(time_steps)  # Time from 0 to time_steps-1
    population = L / (1 + np.exp(-k * (x - x0)))  # Logistic equation

    return population  # Returns only the population values


def time_to_80_percent(L=100, k=0.2, x0=25, time_steps=50):
    """Finds the time when the population reaches 80% of the carrying capacity."""

    population = logistic_growth(L, k, x0, time_steps)  # Get population values
    threshold = 0.8 * L  # 80% of max growth

    for time, value in enumerate(population):
        if value >= threshold:
            return time  # Return the first time step where it reaches 80%

    return None  # If never reached (shouldn't happen in a good simulation)



time_reached = time_to_80_percent()
print("Time to reach 80% of maximum growth:", time_reached)
