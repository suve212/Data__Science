import numpy as np 
import matplotlib.pyplot as plt 
# Simulate 1000 random outcomes between 1 and 6 
results = np.random.randint(1, 7, size=1000) 
# Plot the frequency of outcomes 
plt.hist(results, bins=np.arange(0.5, 7.5, 1), edgecolor='black') 
plt.title('Uniform Distribution Simulation (Die Roll)') 
plt.xlabel('Game Outcome') 
plt.ylabel('Frequency') 
plt.xticks(range(1, 7)) 
plt.grid(True) 
plt.show() 
