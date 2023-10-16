cd $1

mv g-tensor_cc-pVDZ.out cc-pVDZ.out
mv g-tensor.inp cc-pVDZ.inp || mv g-tensor_cc-pVDZ.inp cc-pVDZ.inp

mv g-tensor_cc-pVDZ_invariant.out cc-pVDZ_i.out
mv g-tensor_cc-pVDZ_invariant.inp cc-pVDZ_i.inp

mv g-tensor_EPRII.inp EPRII.inp 
mv g-tensor_EPRII.out EPRII.out

mv g-tensor_EPRII_invariant.inp EPRII_i.inp 
mv g-tensor_EPRII_invariant.out EPRII_i.out

rm *.eprnmr.inp
rm *.tmp
rm *.gori.*
rm *.gbw
rm *_property.txt
rm *.engrad
rm *.opt
rm -f vmdscene.dat
rm *.prop
rm *.scfp *.scfr

cd ..