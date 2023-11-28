To check how these values were computed, just check
[the instructions](https://github.com/Sucerquia/g-tensor/blob/master/instructions.md)
in this repository.

**Note:** the names on the next tables means
- cc-pVDZ: cc-pVDZ basis set, g-values computed with standard method.
- cc-pVDZ i: cc-pVDZ basis set, g-values computed with invariant method.
- cc-pVDZ: EPR_II basis set (created to this aim), g-values computed with standard method.
- cc-pVDZ i: EPR_II basis set (created to this aim), g-values computed with invariant method. This is suppossed to give the most precise outcomes.

# Alkyl shift
The Carbon with larger radius is the one "with the radical"
<div style="display: flex;">
  <img src="/1_0-AlkylShift/opt.png" alt="Image 1" width="20%">
  <img src="/1_0-AlkylShift/chem.png" alt="Image 2" width="20%">
</div>

```math
\begin{array}{|l|c|c|c|c|}
\hline
                   & \text{experiments} & \text{cc-pVDZ}   & \text{cc-pVDZ i} & \text{EPR II}    & \text{EPR II i}   \\ \hline
g-x                & 2.00218     & 2.002362  & 2.002218  & 2.0023654 & 2.0022121  \\ \hline
g-y                & 2.00263     & 2.0027734 & 2.0027595 & 2.0027789 & 2.0027635  \\ \hline
g-z                & 2.00324     & 2.0029019 & 2.002783  & 2.0029035 & 2.0027898  \\ \hline \\ \hline
\text{max absolute error} &             & 0.0003381 & 0.0004570 & 0.0003365 & 0.0004502  \\ \hline
\text{average error}      &             & 0.0000042 & 0.0000965 & 0.0000007 & 0.0000949  \\ \hline
\end{array}
```

# H shift
The Carbon with larger radius is the one "with the radical"\

<div style="display: flex;">
  <img src="/2_0-Hshift/opt.png" alt="Image 1" width="20%">
  <img src="/2_0-Hshift/chem.png" alt="Image 2" width="25%">
</div>

```math
\begin{array}{|l|c|c|c|c|}
\hline
                   & \text{experiments} & \text{cc-pVDZ}   & \text{cc-pVDZ i} & \text{EPR II}    & \text{EPR II i}   \\ \hline
g-x                & 2.00218     & 2.0022603 & 2.0021781 & 2.0022593 & 2.0021773  \\ \hline
g-y                & 2.00263     & 2.0027316 & 2.002725  & 2.0026843 & 2.0027273  \\ \hline
g-z                & 2.00324     & 2.0028357 & 2.0028232 & 2.0028551 & 2.0028389  \\ \hline \\ \hline
\text{max absolute error} &             & 0.0004043 & 0.0004168 & 0.0003849 & 0.0004011  \\ \hline
\text{average error}      &             & 0.0000741 & 0.0001079 & 0.0000838 & 0.0001022  \\ \hline
\end{array}
```
 
# Radical hopping
The Carbon with larger radius is the one "with the radical"

<div style="display: flex;">
  <img src="/3_0-Rhop/opt.png" alt="Image 1" width="20%">
  <img src="/3_0-Rhop/chem.png" alt="Image 2" width="25%">
</div>

```math
\begin{array}{|l|c|c|c|c|}
\hline
                   & \text{experiments} & \text{cc-pVDZ}   & \text{cc-pVDZ i} & \text{EPR II}    & \text{EPR II i}   \\ \hline
g-x                & 2.00218     & 2.0022717 & 2.0021865 & 2.0022694 & 2.0021885  \\ \hline
g-y                & 2.00263     & 2.0027044 & 2.0026987 & 2.0026425 & 2.0026894  \\ \hline
g-z                & 2.00324     & 2.0028602 & 2.0028433 & 2.0028917 & 2.002868   \\ \hline \\ \hline
\text{max absolute error} &             & 0.0003798 & 0.0003967 & 0.0003483 & 0.0003720  \\ \hline
\text{average error}      &             & 0.0000712 & 0.0001072 & 0.0000821 & 0.0001014  \\ \hline
\end{array}
```

# Radical hopping (left side)
The Carbon with larger radius is the one "with the radical"
<div style="display: flex;">
  <img src="/3_1-Rhop-LeftPhenyl/opt.png" alt="Image 1" width="20%">
  <img src="/3_1-Rhop-LeftPhenyl/chem.png" alt="Image 2" width="25%">
</div>

```math
\begin{array}{|l|c|c|c|c|}
\hline
                   & \text{experiments} & \text{cc-pVDZ}   & \text{cc-pVDZ i} & \text{EPR II}    & \text{EPR II i}   \\ \hline
g-x                & 2.00218     & 2.0023205 & 2.0021848 & 2.0023145 & 2.0021862  \\ \hline
g-y                & 2.00263     & 2.0027172 & 2.0026976 & 2.0026162 & 2.0026893  \\ \hline
g-z                & 2.00324     & 2.0028833 & 2.0028429 & 2.0028678 & 2.0028704  \\ \hline \\ \hline
\text{max absolute error} &             & 0.0003567 & 0.0003971 & 0.0003722 & 0.0003696  \\ \hline
\text{average error}      &             & 0.0000430 & 0.0001082 & 0.0000838 & 0.0001014  \\ \hline
\end{array}
```

# Radical hopping (right side)
The Carbon with larger radius is the one "with the radical"
<div style="display: flex;">
  <img src="/3_2-Rhop-RightPhenyl/opt.png" alt="Image 1" width="20%">
  <img src="/3_2-Rhop-RightPhenyl/chem.png" alt="Image 2" width="25%">
</div>

```math
\begin{array}{|l|c|c|c|c|}
\hline
                   & \text{experiments} & \text{cc-pVDZ}   & \text{cc-pVDZ i} & \text{EPR II}    & \text{EPR II i}   \\ \hline
g-x                & 2.00218     & 2.0022479 & 2.0021864 & 2.0022494 & 2.0021882  \\ \hline
g-y                & 2.00263     & 2.0027115 & 2.0027123 & 2.0026915 & 2.0027008  \\ \hline
g-z                & 2.00324     & 2.0028426 & 2.0028348 & 2.0029415 & 2.0028688  \\ \hline \\ \hline
\text{max absolute error} &             & 0.0003974 & 0.0004052 & 0.0002985 & 0.0003712  \\ \hline
\text{average error}      &             & 0.0000827 & 0.0001055 & 0.0000559 & 0.0000974  \\ \hline
\end{array}
```

# Radical in chain
The Carbon with larger radius is the one "with the radical"
<div style="display: flex;">
  <img src="/4_0-inchain/opt.png" alt="Image 1" width="20%">
  <img src="/4_0-inchain/chem.png" alt="Image 2" width="20%">
</div>

```math
\begin{array}{|l|c|c|c|c|}
\hline
                   & \text{experiments} & \text{cc-pVDZ}   & \text{cc-pVDZ i} & \text{EPR II}    & \text{EPR II i}   \\ \hline
g-x                & 2.00218     & 2.002273  & 2.0021848 & 2.0022716 & 2.0021861  \\ \hline
g-y                & 2.00263     & 2.002724  & 2.0027109 & 2.0026724 & 2.0027002  \\ \hline
g-z                & 2.00324     & 2.0028339 & 2.0028348 & 2.0028969 & 2.0028731  \\ \hline \\ \hline
\text{max absolute error} &             & 0.0004061 & 0.0004052 & 0.0003431 & 0.0003669  \\ \hline
\text{average error}      &             & 0.0000730 & 0.0001065 & 0.0000697 & 0.0000969  \\ \hline
\end{array}
```

# Radical in chain larger
The Carbon with larger radius is the one "with the radical"
<div style="display: flex;">
  <img src="/4_1-inchainLarger/chem.png" alt="Image 1" width="20%">
  <img src="/4_1-inchainLarger/opt.png" alt="Image 2" width="20%">
</div>

```math
\begin{array}{|l|c|c|c|c|}
\hline
                   & experiments & cc-pVDZ   & cc-pVDZ i & EPR II    & EPR II i   \\ \hline
g-x                & 2.00218     & 2.0022746 & 2.0021665 & 2.0022729 & 2.0021613  \\ \hline
g-y                & 2.00263     & 2.0027246 & 2.0026983 & 2.0026724 & 2.0026928  \\ \hline
g-z                & 2.00324     & 2.0028394 & 2.0028226 & 2.0028985 & 2.0028619  \\ \hline
max absolute error &             & 0.0004006 & 0.0004174 & 0.0003415 & 0.0003781  \\ \hline
average error      &             & 0.0000705 & 0.0001209 & 0.0000687 & 0.0001113  \\ \hline
\end{array}
```

# Radical (primary) in ring
The Carbon with larger radius is the one "with the radical"
<div style="display: flex;">
  <img src="/5_0-primary_in_ring/chem.png" alt="Image 1" width="20%">
  <img src="/5_0-primary_in_ring/opt.png" alt="Image 2" width="20%">
</div>

```math
\begin{array}{|l|c|c|c|c|}
\hline
                   & experiments & cc-pVDZ   & cc-pVDZ i & EPR II    & EPR II i   \\ \hline
g-x                & 2.00324     & 2.0031568 & 2.0029417 & 2.0031224 & 2.0029442  \\ \hline
g-y                & 2.00263     & 2.0021621 & 2.0021428 & 2.0021544 & 2.0021412  \\ \hline
g-z                & 2.00218     & 2.0018181 & 2.0016607 & 2.0017249 & 2.0016413  \\ \hline
max absolute error &             & 0.0004679 & 0.0005193 & 0.0004756 & 0.0005387  \\ \hline
average error      &             & 0.0003043 & 0.0004349 & 0.0003494 & 0.0004411  \\ \hline
\end{array}
```

# Radical (primary) in tripple bond
The Carbon with larger radius is the one "with the radical"
<div style="display: flex;">
  <img src="/6_0-primary_in_triple/chem.png" alt="Image 1" width="20%">
  <img src="/6_0-primary_in_triple/opt.png" alt="Image 2" width="20%">
</div>

```math
\begin{array}{|l|c|c|c|c|}
\hline
                   & experiments & cc-pVDZ    & cc-pVDZ i  & EPR II     & EPR II i    \\ \hline
g-x                & 2.00324     & 2.0069754  & 2.0069882  & 2.0068963  & 2.0069249   \\ \hline
g-y                & 2.00263     & 2.0038755  & 2.0035236  & 2.003763   & 2.0034574   \\ \hline
g-z                & 2.00218     & 2.0023755  & 2.0022114  & 2.0023649  & 2.0022072   \\ \hline
max absolute error &             & -0.0001955 & -0.0000314 & -0.0001849 & -0.0000272  \\ \hline
average error      &             & -0.0017255 & -0.0015577 & -0.0016581 & -0.0015132  \\ \hline
\end{array}
```


