#!/bin/bash

#SBATCH -N 1                   # number of nodes
#SBATCH -n 16
#SBATCH --cpus-per-task=1
#SBATCH -t 24:00:00
#SBATCH --output=%x-%j.o
#SBATCH --error=%x-%j.e
#SBATCH --exclusive


source /hits/basement/mbm/sucerquia/sw/orca/setup_orca.sh
orca="/hits/basement/mbm/sucerquia/sw/orca/orca_5_0_4_linux_x86-64_openmpi411/orca"

print_help() {
echo "
This tool runs all the necessary steps to get the g-values. It works with some flags:
    
  -d    <directory='./'> directory containing at least model.xyz
  -m    <multiplicity=2> multiplicity of the system.
  -o    Use this flag to avoid the optimization step. opt.xyz must exist, then.

  -h   prints this message.
"
exit 0
}

directory='.'
mult=2
optimization='true'
while getopts 'd:m:oh' flag;
do
    case "${flag}" in
      d) directory=${OPTARG} ;;
      m) mult=${OPTARG} ;;
      o) optimization='false' ;;

      h) print_help ;;
      *) echo "for usage check: myutils <function> -h" >&2 ; exit 1 ;;
    esac
done

cd $directory
cp ../basic_scripts/*.inp .

for inp in *.inp
do
  sed -i "s/XYZFile 0 2/XYZFile 0 $mult/g" $inp
done

if $optimization
then
  $orca opt.inp  > opt.out
else
  [ -f opt.xyz ] || $orca opt.inp  > opt.out
fi

methods=("cc-pVDZ_i" "cc-pVDZ" "EPRII_i" "EPRII")

for met in ${methods[@]}
do
    sbatch -J ${SLURM_JOB_NAME}_${met} ../basic_scripts/submit.sh "$met".inp "$met".out
done
