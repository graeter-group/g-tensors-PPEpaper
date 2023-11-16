methods=("cc-pVDZ_i.inp" "cc-pVDZ.inp" "EPRII_i.inp" "EPRII.inp")

for met in ${methods[@]}
do
    sbatch ../submit.sh "$met".in "$met".out
done
