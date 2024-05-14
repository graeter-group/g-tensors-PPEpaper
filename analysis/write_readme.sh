cat <<EOF
To check how these values were computed, just check
[the instructions](https://github.com/Sucerquia/g-tensor/blob/master/instructions.md)
in this repository.

# Summary table

\`\`\`math
\begin{array}{|l|c|c|c|c|}
\hline
EOF

python summary_table.py

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
# ${system:4}
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