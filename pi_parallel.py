#!/bin/python

import sys
import numpy as np

######Import Pool and cpu_count from multiprocessing 
######below this line

np.random.seed(2017)

def inside_circle(total_count):

    x = np.float32(np.random.uniform(size=total_count))
    y = np.float32(np.random.uniform(size=total_count))

    radii = np.sqrt(x*x + y*y)

    count = len(radii[np.where(radii<=1.0)])

    return count

def estimate_pi(n_samples, n_cores):
    partitions = []
    for i in range(n_cores):
        partitions.append(int(n_samples/n_cores))

### Initialize pool. You must tell the number of cores for map to run######

    pool = Pool(processes=###)

### Call pool.map. It takes the form pool.map(function_name,structured_data)###

    counts = pool.map(###, ###)

### Compute total count. Use function sum. Why??###
    total_count = sum(###)

### Compute return. Use function sum ####

    return (4.0 * #### / total_count)


###Use cpu_count() to get the number of cores

ncores = #####
n_samples = 10000
if len(sys.argv) > 1:
    n_samples = int(sys.argv[1])

my_pi = estimate_pi(n_samples,ncores)
sizeof = np.dtype(np.float32).itemsize

print("[parallel version] required memory %.3f MB" % (n_samples*sizeof*3/(1024*1024)))
print("[using %3i cores ] pi is %f from %i samples" % (ncores,my_pi,n_samples))
