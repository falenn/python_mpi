# Python and MPI

## Installing MPI 

### Install MPICC
We actually need MPI installed on the host already.  mpi4py is a wrapper
yum install mpich-devel mpich-autoload

### Install Python 
https://linuxize.com/post/how-to-install-python-3-on-centos-7/

Running in virtual env:
cd to this dir
enable python3.6
scl enable rh-python36 bash

if venv enabled already, dir will exist, so just source env
. python_mpi/bin/activate

### Install openMPI mpi.h
yum whatprovides '*/mpi.h'
...
sudo yum install openmpi-devel

we have to have openMPI installed for mpi4py to install.

Setup Includes path so mpi4py can install



### Install mpi4py
pip install mpi4py


To know where packages are installed:
python -c "import site; print(site.USER_BASE)"

pip list
this shows what's installed - run for sanity

## Executing hello_mpi.py
mpirun -np 4 python hello_mpi.py

we execute using the compiled python wrapper around mpicc in order to specify number of
 processes to execute


try running like so:

time mpirun -np <X> python integral.py

https://stackoverflow.com/questions/556405/what-do-real-user-and-sys-mean-in-the-output-of-time1

See the time output?  Oversubscribing the number of cores doesn't make the processs run faster (generally).  Try it out!
