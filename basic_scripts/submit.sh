#!/bin/bash

#SBATCH -N 1                   # number of nodes
#SBATCH -n 16
#SBATCH --cpus-per-task=1
#SBATCH -t 24:00:00
#SBATCH --output=optimization_orca-%j.o
#SBATCH --error=optimization_orca-%j.e
#SBATCH --exclusive

module load GCC/8.2.0-2.31.1
source /hits/sw/ccc/ORCA421/setup_orca.sh

/hits/sw/ccc/ORCA421/orca_4_2_1_linux_x86-64_openmpi314/orca $1 > $2
