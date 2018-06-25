#!/bin/python

"""
This program takes a value in the input when run and outputs some information
about the run, and an estimation of pi.

Run Examples: python py_serial.py 
              python py_serial.py 10000
              python py_serial.py 20000 
"""


####Import module sys below this line

####Import module numpy as np below this line



np.random.seed(2017)

def inside_circle(total_count):
    """
    This function takes total_count as input, generates list x with
    the total_count random x-coordinates, and a list y with the total_count y-coordinates,
    and returns the count of which are inside radius 1 circle
    """

    x = np.float32(np.random.uniform(size=total_count))
    y = np.float32(np.random.uniform(size=total_count))

    radii = ##

    count = ##

    return count

def estimate_pi(n_samples):
    """
    This function takes n_samples and return an estimation of pi
    """
    return ##


n_samples = 10000
if len(sys.argv) > 1:
    n_samples = int(sys.argv[1])

my_pi = ???????????(n_samples)
sizeof = np.dtype(np.float32).itemsize

print("[serial version] required memory %.3f MB" % (n_samples*sizeof*3/(1024*1024)))
print("[serial version] pi is %f from %i samples" % (my_pi,n_samples))

