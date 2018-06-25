#!/bin/python

import sys
import numpy as np
from mpi4py import MPI



comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
np.random.seed(2017 + 1000 * rank)


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

    if rank == 0:
        partitions = []
        counts = []
        for i in range(size):
             partitions.append(int(n_samples/size))
             counts.append(int(0))
    else:
        partitions = None
        counts = None


    # At this point only rank0 knows the value of partitions and counts. It has to be deployed to the other ranks

    partition_item = comm.scatter(partitions, root=0)
    count_item = comm.scatter(counts, root=0)

    # Now I do the real computation on each rank
    count_item = inside_circle(partition_item)

    # And I ask rank 0 to gather all results in counts
    counts = comm.gather(count_item, root=0)

    # And finally I ask rank 0 to make the final estimation of pi

    if rank == 0:
        my_pi = 4.0 * sum(counts)/sum(partitions)
        sizeof = np.dtype(np.float32).itemsize
	print("[MPI version] required memory %.3f MB" % (n_samples*sizeof*3/(1024*1024)))
        print("[MPI version. Ranks= %i ] pi is %f from %i samples" % (size,my_pi,n_samples))

############### Main execution ###########

main()

