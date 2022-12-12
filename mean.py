import statistics
from mpi4py import MPI
import sys
size = MPI.COMM_WORLD.Get_size()
rank = MPI.COMM_WORLD.Get_rank()
name = MPI.Get_processor_name()
data = [37, 48, 52, 59, 68, 74, 80]
 
# Finding Mean
print("\nMean: ", statistics.mean(data))
 
# Finding Median
print("Median: ", statistics.median(data))
 
# Finding Single Mode
print("Single Mode: ", statistics.mode(data))
 
# Finding Multiple Modes
print("Mode: ", statistics.multimode(data))
sys.stdout.write(
    "Process %d of %d on %s.\n"
    % (rank, size, name))
