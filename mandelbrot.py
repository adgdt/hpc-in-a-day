def mandelbrot (x, y, maxit):
    c = x + y*1j
    z = 0 + 0j
    it = 0
    while abs(z) < 2 and it < maxit:
        z = z**2 + c
        it += 1
    return it

x1, x2 = -2.0, 1.0
y1, y2 = -1.0, 1.0
w, h = 150, 100
maxit = 127
dx = (x2 - x1) / w
dy = (y2 - y1) / h

from mpi4py import MPI
import numpy
  
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

# number of rows to compute here
N = h // size 
rest = h % size

if (rest > rank):
	N = N + 1
#Pro version: N = h // size + ( h % size > rank )


# first row to compute here
#Pro version: start = comm.scan(N)-N

#start = comm.scan(N)-N
start = comm.exscan(N)
if (rank == 0 ):
    start = 0

# array to store local result
Cl = numpy.zeros([N, w], dtype='i')

# compute owned rows
for i in range(N):
    y = y1 + (i + start) * dy
    for j in range(w):
        x = x1 + j * dx
        Cl[i, j] = mandelbrot(x, y, maxit)

# gather results at root (process 0)
counts = comm.gather(N, root=0)

C = None
if rank == 0:
    C = numpy.zeros([h, w], dtype='i')

rowtype = MPI.INT.Create_contiguous(w)
rowtype.Commit()

comm.Gatherv(sendbuf=[Cl, MPI.INT], recvbuf=[C, (counts, None), rowtype],root=0)

rowtype.Free()



#Plotting


if rank == 0:

   import matplotlib
   matplotlib.use('Agg')
   import matplotlib.pyplot as plt
   image = plt.imshow(C)
   plt.savefig('mandelimg.jpg')
