To check how these values were computed, just check ./00-notes.sh in this
repository.

**Note:** the names on the next tables means
- cc-pVDZ: cc-pVDZ basis set, g-values computed with standard method.
- cc-pVDZ: cc-pVDZ basis set, g-values computed with invariant method.
- cc-pVDZ: EPR_II basis set (created to this aim), g-values computed with standard method.
- cc-pVDZ: EPR_II basis set (created to this aim), g-values computed with invariant method. This is suppossed to give the most precise outcomes.

# Alkyl shift
The Carbon with larger radius is the one "with the radical"
<div style="display: flex;">
  <img src="/AlkylShift/Alkylshift.png" alt="Image 1" width="20%">
  <img src="/AlkylShift/Alkyl.png" alt="Image 2" width="20%">
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
  <img src="/Hshift/Hshift.png" alt="Image 1" width="20%">
  <img src="/Hshift/H.png" alt="Image 2" width="25%">
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
  <img src="/Rhop/Rhop.png" alt="Image 1" width="20%">
  <img src="/Rhop/radical.png" alt="Image 2" width="25%">
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
  <img src="/left/left.png" alt="Image 1" width="20%">
  <img src="/left/left2.png" alt="Image 2" width="25%">
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
  <img src="/right/right.png" alt="Image 1" width="20%">
  <img src="/Rhop/radical.png" alt="Image 2" width="25%">
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
  <img src="/inchain/inchain.png" alt="Image 1" width="20%">
  <img src="/inchain/chain.png" alt="Image 2" width="20%">
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
