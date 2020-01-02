#from sharcnet HPC: https://www.youtube.com/watch?v=36nCgG40DJo
#
# This is an integration strategy summing trapezoids over a range (a,b) given 
# a function, for slice n and current height, h.
#

from func import f

def Trap(a,b,n,h):

  integral = (f(a) + f(b))/2.0
  
  x = a

  for i in range(1, int(n)):
    x = x + h
    integral = integral + f(x)

  return integral * h

