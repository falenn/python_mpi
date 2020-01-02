# from sharcnet HPC:  https://www.youtube.com/watch?v=36nCgG40DJo

from mpi4py import MPI
from func import f
from traprule import Trap
from getdata2 import Get_data

# This MPI Program demonstrates the following:
# introduces MPI.SUM (map / reduce)

comm = MPI.COMM_WORLD
# int my_rank - My process rank
my_rank = comm.Get_rank()
# int p = number of processes
p = comm.Get_size()

# MAIN
# get configurable params
a,b,n = Get_data(my_rank,p,comm)

# critical point barrier process in charge
dest=0
# var for collecting integration sum
total=-1.0

# each process computes its own partial integral
h = (b-a)/n   # h is the same for all processes
local_n = n/p # trapezoids divided out for the number of processes

# Length of each process' interval of integration = local_n*h
local_a = a + my_rank*local_n*h
local_b = local_a + local_n*h
integral = Trap(local_a, local_b, local_n, h)
# done with integral

# Now, collect results from all other processes!
# Passing integral as the argument targets that property in the host
total = comm.reduce(integral)


# print the result
if(my_rank == 0):
  #time.sleep(2)
  print("With n=",n,"trapezoids, ")
  print("integral from ",a,"to ",b," = ",total,"\n")

MPI.Finalize


