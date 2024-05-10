
cd $1

methods=( "cc-pVDZ" "EPRII")

for met in ${methods[@]}
do
    cp ../basic_scripts/${met}.inp .
    sbatch -J ${1:0:3}_${met} ../basic_scripts/submit.sh "$met".inp "$met".out
done
