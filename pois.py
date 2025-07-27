import numpy as np 
from scipy.stats import poisson 
import matplotlib.pyplot as plt 
# Simulate Poisson distribution 
x = np.arange(0, 11)  # possible number of arrivals 
lambda_val = 4 
probs = poisson.pmf(x, mu=lambda_val) 
# Plot the distribution 
plt.figure(figsize=(6, 4)) 
plt.bar(x, probs, color='lightgreen') 
plt.title('Poisson Distribution (Customer Arrivals per Hour)') 
plt.xlabel('Number of Customers') 
plt.ylabel('Probability') 
plt.grid(True) 
plt.show() 
