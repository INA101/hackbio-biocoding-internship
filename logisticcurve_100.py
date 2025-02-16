import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def logistic_growth(L=100, k=0.2, x0=25, time_steps=50):
    """Simulates logistic population growth."""

    x = np.arange(time_steps)  # Time from 0 to time_steps-1
    population = L / (1 + np.exp(-k * (x - x0)))  # Logistic equation

    return population  # Returns only the population values


# Create a DataFrame with 100 different growth curves
num_curves = 100
time_steps = 50
growth_data = {}

for i in range(1, num_curves + 1):
    random_k = np.random.uniform(0.1, 0.3)  # Random growth rate between 0.1 and 0.3
    random_x0 = np.random.randint(15, 35)  # Random midpoint between 15 and 35
    growth_data[f'Curve_{i}'] = logistic_growth(k=random_k, x0=random_x0, time_steps=time_steps)

df = pd.DataFrame(growth_data)

# Plot all 100 curves
plt.figure(figsize=(10, 6))
for i in range(1, num_curves + 1):
    plt.plot(df.index, df[f'Curve_{i}'], alpha=0.3, color='blue')  # Alpha makes them semi-transparent

plt.xlabel("Time")
plt.ylabel("Population Size")
plt.title("Logistic Growth Curves (100 Simulations)")
plt.show()
