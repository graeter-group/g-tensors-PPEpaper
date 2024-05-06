#!/bin/bash

#SBATCH -N 1                   # number of nodes
#SBATCH -n 16
#SBATCH --cpus-per-task=1
#SBATCH -t 24:00:00
#SBATCH --output=optimization_orca-%j.o
#SBATCH --error=optimization_orca-%j.e
#SBATCH --exclusive

source /hits/basement/mbm/sucerquia/sw/orca/setup_orca.sh

orca="/hits/basement/mbm/sucerquia/sw/orca/orca_5_0_4_linux_x86-64_openmpi411/orca"

cd $1
cp ../basic_scripts/*.inp .

mult=$2

for inp in *.inp
do
  sed -i "s/XYZFile 0 2/XYZFile 0 $mult/g" $inp
done
$orca opt.inp  > opt.out &&

methods=("cc-pVDZ_i" "cc-pVDZ" "EPRII_i" "EPRII")

for met in ${methods[@]}
do
    sbatch ../basic_scripts/submit.sh "$met".inp "$met".out
done

# Note: this code runs all the necessary steps to get the g-values.
# It works with one argument:
# sbatch workflow.sh <model_directory> that has to contain the file model.xyz
