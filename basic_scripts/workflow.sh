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


orca="/hits/sw/ccc/ORCA421/orca_4_2_1_linux_x86-64_openmpi314/orca"

cd $1
cp ../basic_scripts/*.inp .
$orca opt.inp  > opt.out &&

methods=("cc-pVDZ_i" "cc-pVDZ" "EPRII_i" "EPRII")
for met in ${methods[@]}
do
    sbatch ../basic_scripts/submit.sh "$met".inp "$met".out
done

# Note: this code runs all the necessary steps to get the g-values.
# It works with one argument:
# sbatch workflow.sh <model_directory> that has to contain the file model.xyz