from mpi4py import MPI
import sys
size = MPI.COMM_WORLD.Get_size()
rank = MPI.COMM_WORLD.Get_rank()
name = MPI.Get_processor_name()
 
# Finding Mean
print("\nNama Anggota Kelompok:\n1. Aldi Winata\n2. Febry Afriansyah\n3. Fadli Ilhami")
sys.stdout.write(
    "Process %d of %d on %s.\n"
    % (rank, size, name))
