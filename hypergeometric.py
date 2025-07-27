from scipy.stats import hypergeom 
# Parameters: M = population size, n = total defectives, N = sample size 
M = 20  # total products 
n = 5   # defective products 
N = 6   # sample taken 
# Probability of getting exactly 2 defective items 
prob_2_defectives = hypergeom.pmf(2, M, n, N) 
print("P(Exactly 2 defectives in sample):", round(prob_2_defectives, 4)) 
