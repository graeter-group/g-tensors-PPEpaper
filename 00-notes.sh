#!/usr/bin/bash

# This code runs all the codes to get the G-values of the hypothized radicals
# see ./summarized.odp, second slide

# ==== Prepare first (reduced) molecule =======================================
# the original molecule was sent by Matthias and it is copied to
# reduced/2mers-Octadecyl.pdb

# ==== Remove additional atoms
cd ./reduced
./reducing.sh 2mers-Octadecyl.pdb
python add_Hatoms.py
sbatch ../submit.sh opt.inp opt.out

# ==== Create structures with radicals
cd ..
python createStructures.py

# ==== Run each candicate =====================================================
# Alkyshift
cd Alkyshift
sbatch ../submit.sh opt.inp opt.out

# H shift
cd Hshift
sbatch ../submit.sh opt.inp opt.out

# Radikal hopping
cd Rhop
sbatch ../submit.sh opt.inp opt.out
