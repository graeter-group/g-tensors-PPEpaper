cat <<EOF
To check how these values were computed, just check
[the instructions](https://github.com/Sucerquia/g-tensor/blob/master/instructions.md)
in this repository.

# Distances(Å)

<div style="display: flex;">
<img src="/distances/distance1.png" alt="Image 1" width="20%">
<img src="/distances/distance2.png" alt="Image 2" width="20%">
</div>

# BDEs

The system considered here are:

- left: with Phenyl group.
- right: without Phenyl group.
- red: tripple bond
- blue: single bond.

<div style="display: flex;">
<img src="/0_0-BeforeRupture/BDE/opt.png" alt="Image 1" width="20%">
<img src="/0_1-BeforeRupture_wo_extRings/BDE2/opt.png" alt="Image 2" width="20%">
</div>

EOF


echo "### Orca"
echo "- With Phenyl group:"
python BDES.py 1 orca

echo -e "\n\n- Without Phenyl group"
python BDES.py 2 orca

echo -e "\n### g09"
echo "- With Phenyl group:"
python BDES.py 1 g09

echo -e "\n\n- Without Phenyl group"
python BDES.py 2 g09

cat <<EOF

# G-values

### Summary table

\`\`\`math
\begin{array}{|l|c|c|c|c|}
\hline
EOF

python summary_table.py | sed "s/\.\.\/._.-//g" | sed "s/\/\}/}/g" | sed "s/_/-/g"

cat <<EOF
\end{array}
\`\`\`

<div style="text-align:center">
  <img src="/structuresPPE.png" alt="Image 1" width="80%">
</div>

**Note:** the names on the next tables means
- cc-pVDZ: cc-pVDZ basis set, g-values with the origin in the center of the electronic distribution.
- cc-pVDZ i: cc-pVDZ basis set, g-values computed with invariant method.
- cc-pVDZ: EPR_II basis set (created to this aim), g-values with the origin in the center of the electronic distribution.
- cc-pVDZ i: EPR_II basis set (created to this aim), g-values computed with invariant method. This is suppossed to give the most precise outcomes.

EOF

cd ..

for system in [123456789]*
do
  if [ -d $system ]
  then
    cat <<EOF
### ${system:4}
The Carbon with larger radius is the one "with the radical"
<div style="display: flex;">
<img src="/$system/opt.png" alt="Image 1" width="20%">
<img src="/$system/chem.png" alt="Image 2" width="20%">
</div>

\`\`\`math
\begin{array}{|l|c|c|c|c|}
\hline
EOF
    python analysis/create_tables.py ${system}/
  cat <<EOF
\end{array}
\`\`\`

EOF
  fi
done

cat <<EOF

# Plot of g-values.

<div style="display: flex;">
<img src="/analysis/g-values.png" alt="Image 1" width="50%">
</div>
EOF