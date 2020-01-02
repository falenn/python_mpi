# from sharcnet HPC:  https://www.youtube.com/watch?v=36nCgG40DJo

from mpi4py import MPI
from func import f
from traprule import Trap
import time

# This MPI Program demonstrates the following:
# 1. import of mpi4py
# 2. initialization of comm = MPI.COMM_WORLD
# 3. comm.Get_rank()
# 4. comm.Get_size()
# 5. comm.send(...)
# 6. comm.receive(...)
# 7. MPI.Finalize

comm = MPI.COMM_WORLD
# int my_rank - My process rank
my_rank = comm.Get_rank()
# int p = number of processes
p = comm.Get_size()

# float a - left endpoint
a = 0.0

# float b - right endpoint
b = 1.0

# int n - number of trapezoids
n = 1024

# critical point barrier process in charge
dest=0

# var for collecting integration sum
total=-1.0

# MAIN
# each process computes its own partial integral
h = (b-a)/n   # h is the same for all processes
local_n = n/p # trapezoids divided out for the number of processes

# Length of each process' interval of integration = local_n*h
local_a = a + my_rank*local_n*h
local_b = local_a + local_n*h
integral = Trap(local_a, local_b, local_n, h)
# done with integral

# Now, manage message communication...
if my_rank == 0:
  # if rank = 0, first remember to start with local-computed partial integration
  total = integral
  # now receive data from the rest of the processes
  for source in range(1,p):
    integral = comm.recv(source=source)
    print("RECV ",my_rank,"<-",source,",",integral,"\n")
    total = total + integral
else:
  print("SEND ",my_rank,"->",dest,",",integral,"\n")
  comm.send(integral, dest=0)

# print the result
if(my_rank == 0):
  #time.sleep(2)
  print("With n=",n,"trapezoids, ")
  print("integral from ",a,"to ",b," = ",total,"\n")

MPI.Finalize


