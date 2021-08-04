import numpy as np
import sys

rand_seeds = [ 10, 24, 48, 76, 104 ]

array_sizes = [ 10**3, 10**4, 10**5, 10**6, 10**7]


if __name__ == "__main__":
    
    for size in array_sizes:
        for seed in rand_seeds:
        
            np.random.seed(seed)

            arr = np.random.randint(low=-1000, high=1000, size=size)

            np.savetxt( f'../dados/entrada_{size}_{seed}.dat', arr, 
                        delimiter=',', newline='\n')
           
