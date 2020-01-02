# Pthon and MPI

## Installing MPI 

### Install Python 
https://linuxize.com/post/how-to-install-python-3-on-centos-7/

### Install openMPI mpi.h
yum whatprovides '*/mpi.h'
...
sudo yum install openmpi-devel

we have to have openMPI installed for mpi4py to install.

### Install mpi4py
pip install mpi4py
