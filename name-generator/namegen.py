import numpy as np
import random as rand

# Load the data from the text file
sf = np.loadtxt('suffix.txt', dtype=str)
pf = np.loadtxt('prefix.txt', dtype=str)

# Convert the data to a NumPy array
suffix = np.array(sf)
prefix = np.array(pf)


# Print the array
for i in range(1,20):
  r_suffix = rand.choice(suffix)
  r_prefix = rand.choice(prefix)
  print(r_prefix + r_suffix)
