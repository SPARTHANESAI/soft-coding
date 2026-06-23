import numpy as np 

rng = np.random.default_rng()
print(rng.random(), "\n") 
print(rng.random(10) , '\n')
print(rng.random((3, 4)))

print(rng.integers(10))
print(rng.integers(0, 10, size = 20))
print(rng.integers(0, 10, size = (2,4)))



