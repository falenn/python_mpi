# from sharcnet HPC:  https://www.youtube.com/watch?v=36nCgG40DJo

from mpi4py import MPI

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
