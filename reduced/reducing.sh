cp $1 tmp.pdb

rem_res=( 1 2 3 4 5 6 7 9 10 )
for res in ${rem_res[@]}
do
    awk -v residue=$res '{if ($1 == "ATOM") { 
                                        if ($6 != residue) {
                                            print $0}
                                        }
                                    else {
                                        print $0
                                    }
                                    }' tmp.pdb > reduced.pdb
    cp reduced.pdb tmp.pdb    
done

rem_atoms_in_8=( "HA1" "HA2" "CAS1" 
    "CAS2" "CAL1" "CAL2" "CA1" "CA2" "CL2")

for atom in ${rem_atoms_in_8[@]}
do
    awk -v atom=$atom '{if ($1 == "ATOM" && $6 == 8) { 
                               if ($3 != atom) {
                                   print $0}
                               }
                               else {
                                   print $0
                               }}' tmp.pdb > reduced.pdb
    cp reduced.pdb tmp.pdb    
done

rem_atoms_in_14=( "HAa" "HAb" "HAc" "HAd" "HAe" 
    "CAa" "CAb" "CAc" "CAd" "CAe" "CAL0")

for atom in ${rem_atoms_in_14[@]}
do
    awk -v atom=$atom '{if ($1 == "ATOM" && $6 == 14) { 
                               if ($3 != atom) {
                                   print $0}
                               }
                               else {
                                   print $0
                               }}' tmp.pdb > reduced.pdb
    cp reduced.pdb tmp.pdb    
done

rem_atoms_in_12=( "CST3" "HS1" "HS2" "HS3")

# H side chain terminal
for i in {7..9}
do
    rem_atoms_in_12=( ${rem_atoms_in_12[@]} "HST$i")
done

# C side chain
for i in {39..51}
do
    rem_atoms_in_12=( ${rem_atoms_in_12[@]} "CS$i")
done

# H side chain
for i in {77..99}
do
    rem_atoms_in_12=( ${rem_atoms_in_12[@]} "HS$i")
done

for atom in ${rem_atoms_in_12[@]}
do
    awk -v atom=$atom '{if ($1 == "ATOM" && $6 == 12) { 
                               if ($3 != atom) {
                                   print $0}
                               }
                               else {
                                   print $0
                               }}' tmp.pdb > reduced.pdb
    cp reduced.pdb tmp.pdb    
done


rem_atoms_in_13=( "CST4")

# H side chain terminal
for i in {1..3}
do
    rem_atoms_in_13=( ${rem_atoms_in_13[@]} "HST$i")
done

# C side chain
for i in {56..68}
do
    rem_atoms_in_13=( ${rem_atoms_in_13[@]} "CS$i")
done

# H side chain
for i in {12..37}
do
    rem_atoms_in_13=( ${rem_atoms_in_13[@]} "HS$i")
done

for atom in ${rem_atoms_in_13[@]}
do
    awk -v atom=$atom '{if ($1 == "ATOM" && $6 == 13) { 
                               if ($3 != atom) {
                                   print $0}
                               }
                               else {
                                   print $0
                               }}' tmp.pdb > reduced.pdb
    cp reduced.pdb tmp.pdb    
done

rm tmp.pdb
