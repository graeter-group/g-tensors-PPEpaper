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
# ==== Alkyshift
cd Alkyshift
sbatch ../submit.sh opt.inp opt.out

sbatch ../submit.sh g-tensor_EPRII.inp g-tensor_EPRII.out
# In the next output, g(tot) shows the x y z components of g tensor
grep -A 15 "ELECTRONIC G-MATRIX" g-tensor_EPRII.out 

sbatch ../submit.sh g-tensor_EPRII_i.inp g-tensor_EPRII_i.out
# In the next output, g(tot) shows the x y z components of g tensor
grep -A 15 "ELECTRONIC G-MATRIX" g-tensor_EPRII_i.out

sbatch ../submit.sh g-tensor_cc-pVDZ.inp \
    g-tensor_cc-pVDZ.out
# In the next output, g(tot) shows the x y z components of g tensor
grep -A 15 "ELECTRONIC G-MATRIX" g-tensor_cc-pVDZ.out

sbatch ../submit.sh g-tensor_cc-pVDZ_invariant.inp \
    g-tensor_cc-pVDZ_invariant.out
# In the next output, g(tot) shows the x y z components of g tensor
grep -A 15 "ELECTRONIC G-MATRIX" g-tensor_cc-pVDZ_invariant.out

# ==== H shift
cd Hshift
sbatch ../submit.sh opt.inp opt.out

sbatch ../submit.sh g-tensor_EPRII.inp g-tensor_EPRII.out
# In the next output, g(tot) shows the x y z components of g tensor
grep -A 15 "ELECTRONIC G-MATRIX" g-tensor_EPRII.out 

sbatch ../submit.sh g-tensor_EPRII_i.inp g-tensor_EPRII_i.out
# In the next output, g(tot) shows the x y z components of g tensor
grep -A 15 "ELECTRONIC G-MATRIX" g-tensor_EPRII_i.out

sbatch ../submit.sh g-tensor_cc-pVDZ.inp \
    g-tensor_cc-pVDZ.out
# In the next output, g(tot) shows the x y z components of g tensor
grep -A 15 "ELECTRONIC G-MATRIX" g-tensor_cc-pVDZ.out

sbatch ../submit.sh g-tensor_cc-pVDZ_invariant.inp \
    g-tensor_cc-pVDZ_invariant.out
# In the next output, g(tot) shows the x y z components of g tensor
grep -A 15 "ELECTRONIC G-MATRIX" g-tensor_cc-pVDZ_invariant.out

# ==== Radikal hopping
cd Rhop
sbatch ../submit.sh opt.inp opt.out

sbatch ../submit.sh g-tensor_EPRII.inp g-tensor_EPRII.out
# In the next output, g(tot) shows the x y z components of g tensor
grep -A 15 "ELECTRONIC G-MATRIX" g-tensor_EPRII.out 

sbatch ../submit.sh g-tensor_EPRII_i.inp g-tensor_EPRII_i.out
# In the next output, g(tot) shows the x y z components of g tensor
grep -A 15 "ELECTRONIC G-MATRIX" g-tensor_EPRII_i.out

sbatch ../submit.sh g-tensor_cc-pVDZ.inp \
    g-tensor_cc-pVDZ.out
# In the next output, g(tot) shows the x y z components of g tensor
grep -A 15 "ELECTRONIC G-MATRIX" g-tensor_cc-pVDZ.out

sbatch ../submit.sh g-tensor_cc-pVDZ_invariant.inp \
    g-tensor_cc-pVDZ_invariant.out
# In the next output, g(tot) shows the x y z components of g tensor
grep -A 15 "ELECTRONIC G-MATRIX" g-tensor_cc-pVDZ_invariant.out
