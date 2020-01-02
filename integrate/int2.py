# from sharcnet HPC:  https://www.youtube.com/watch?v=36nCgG40DJo

from mpi4py import MPI
from func import f
from traprule import Trap
import time

# This MPI Program demonstrates the following:
# introduces Broadcast
# Comm.bcast(self, object, int root=0)  int root=0 is the type and the node that contains the data.  Object is the data being broadcast
# Broadcasting saves time when haveing to communicate with all other nodes.  Instead, this now becomes
# logrithmically

comm = MPI.COMM_WORLD
# int my_rank - My process rank
my_rank = comm.Get_rank()
# int p = number of processes
p = comm.Get_size()

# Read input from stdio and make available to all other processes
def Get_data(my_rank, p, comm):
  a=None
  b=None
  n=None
  if my_rank == 0:
    print("Rank ",my_rank,": Enter a,b and n\n")
    a=float(input("Enter a (left-side int range): \n"))
    b=float(input("Enter b (right-side int range): \n"))
    n=int(input("Enter n (# of trapezoids): \n"))  
    print(" ready for broadcast \n")

  # at the end, every process has these values
  a=comm.bcast(a)
  b=comm.bcast(b)
  n=comm.bcast(n)
  
  return a,b,n


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


