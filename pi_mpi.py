#!/bin/python

import sys
import numpy as np
###Import MPI from mpi4py below this line

### Create communicator using MPI.COMM_WORLD###
comm = ###

### Use methods Get_size() and Get_rank() to gather info
size = ##
rank = ##

### Make random seed depending on the rank ###
### Starting at 2017 for rank_0 and increasing 1000 per rank####
np.random.seed(#)


def inside_circle(total_count):

    x = np.float32(np.random.uniform(size=total_count))
    y = np.float32(np.random.uniform(size=total_count))

    radii = np.sqrt(x*x + y*y)

    count = len(radii[np.where(radii<=1.0)])

    return count

def main():
    n_samples = 10000
    if len(sys.argv) > 1:
        n_samples = int(sys.argv[1])


### Make rank 0 to calculate partitions and initialize containers for data ###

    if ##:
        partitions = ##
	counts = ##

        for i in range(size):
             partitions.append(int(###))
             counts.append(int(###))
    else:

### Other ranks than zero must initialize containers to None####
        partitions = ##
        counts = ##


### Use scatter method to scatter containers into local lists. The use is: communicator.scatter(structured_data,root=rank_of_origin)###

    partition_item = ##
    count_item = ##

### Use count_item to store the local result. Hint: Just call function inside_circle on local partition### 
    count_item = ###



### Use communicator's gather method to gather partial results stored in local counter. The use is: communicator.gather(local_counter, root=destination_rank)### 

    counts = ###


### And finally ask rank 0 to make the final estimation of pi

    if ###:
        my_pi = 4.0 * sum(###)/sum(###)
        sizeof = np.dtype(np.float32).itemsize
        print("[MPI version] required memory %.3f MB" % (n_samples*sizeof*3/(1024*1024)))
        print("[MPI version. Ranks= %i ] pi is %f from %i samples" % (size,my_pi,n_samples))


main()

