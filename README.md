To check how these values were computed, just check
[the instructions](https://github.com/Sucerquia/g-tensor/blob/master/instructions.md)
in this repository.

# Summary table
```math
\begin{array}{|l|c|c|c|c|}
\hline
                                    & g_x       & g_y       & g_z       & \text{max abs error} & \text{avrg error}  \\ \hline
\text{A) AlkylShift}                & 2.0027891 & 2.0027628 & 2.0022129 & 0.0004509            & 0.0000951          \\ \hline
\text{B) Hshift}                    & 2.0028366 & 2.0027276 & 2.0021779 & 0.0004034            & 0.0001026          \\ \hline
\text{C) Rhop}                      & 2.0028675 & 2.0026892 & 2.0021881 & 0.0003725            & 0.0001017          \\ \hline
\text{D) Rhop-LeftPhenyl}           & 2.0028709 & 2.0026882 & 2.0021857 & 0.0003691            & 0.0001017          \\ \hline
\text{E) Rhop-RightPhenyl}          & 2.0028687 & 2.0027009 & 2.002188  & 0.0003713            & 0.0000975          \\ \hline
\text{F) inchain}                   & 2.0028687 & 2.0027033 & 2.0021858 & 0.0003713            & 0.0000974          \\ \hline
\text{G) inchainLarger}             & 2.0028596 & 2.0026923 & 2.002155  & 0.0003804            & 0.0001144          \\ \hline
\text{H) primary in ring}           & 2.0029459 & 2.0021419 & 2.0016379 & 0.0005421            & 0.0004414          \\ \hline
\text{I) primary in triple}         & 2.0069279 & 2.0034545 & 2.0022073 & -0.0000273           & -0.0015132         \\ \hline
\text{J) triple broken}             & 2.0219089 & 2.0031983 & 2.0020915 & 0.0000885            & -0.0063829         \\ \hline
\text{K) Hshift FarRad1}            & 2.0028061 & 2.0027633 & 2.0021821 & 0.0004339            & 0.0000995          \\ \hline
\text{L) Hshift FarRad2}            & 2.0027372 & 2.0027246 & 2.0021729 & 0.0005028            & 0.0001384          \\ \hline
\text{M) Rhop FarRad1}              & 2.0028097 & 2.0027589 & 2.0021822 & 0.0004303            & 0.0000997          \\ \hline
\text{N) Rhop FarRad2}              & 2.0027359 & 2.0027201 & 2.002173  & 0.0005041            & 0.0001403          \\ \hline
\text{Experiment}                   & 2.00324   & 2.00263   & 2.00218   &                      &                    \\ \hline
\end{array}
```

<div style="text-align:center">
  <img src="/structuresPPE.png" alt="Image 1" width="80%">
</div>

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
                          & experiments & cc-pVDZ   & cc-pVDZ i & EPR II    & EPR II i   \\ \hline
g-x                       & 2.00324     & 2.0027825 & 2.0027825 & 2.0027891 & 2.0027891  \\ \hline
g-y                       & 2.00263     & 2.0027585 & 2.0027585 & 2.0027628 & 2.0027628  \\ \hline
g-z                       & 2.00218     & 2.0022185 & 2.0022185 & 2.0022129 & 2.0022129  \\ \hline
\text{max absolute error} &             & 0.0004575 & 0.0004575 & 0.0004509 & 0.0004509  \\ \hline
\text{average error}      &             & 0.0000968 & 0.0000968 & 0.0000951 & 0.0000951  \\ \hline
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
                          & experiments & cc-pVDZ   & cc-pVDZ i & EPR II    & EPR II i   \\ \hline
g-x                       & 2.00324     & 2.0028218 & 2.0028218 & 2.0028366 & 2.0028366  \\ \hline
g-y                       & 2.00263     & 2.0027232 & 2.0027232 & 2.0027276 & 2.0027276  \\ \hline
g-z                       & 2.00218     & 2.0021786 & 2.0021786 & 2.0021779 & 2.0021779  \\ \hline
\text{max absolute error} &             & 0.0004182 & 0.0004182 & 0.0004034 & 0.0004034  \\ \hline
\text{average error}      &             & 0.0001088 & 0.0001088 & 0.0001026 & 0.0001026  \\ \hline
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
                          & experiments & cc-pVDZ   & cc-pVDZ i & EPR II    & EPR II i   \\ \hline
g-x                       & 2.00324     & 2.0028431 & 2.0028431 & 2.0028675 & 2.0028675  \\ \hline
g-y                       & 2.00263     & 2.0026971 & 2.0026971 & 2.0026892 & 2.0026892  \\ \hline
g-z                       & 2.00218     & 2.0021861 & 2.0021861 & 2.0021881 & 2.0021881  \\ \hline
\text{max absolute error} &             & 0.0003969 & 0.0003969 & 0.0003725 & 0.0003725  \\ \hline
\text{average error}      &             & 0.0001079 & 0.0001079 & 0.0001017 & 0.0001017  \\ \hline
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
                          & experiments & cc-pVDZ   & cc-pVDZ i & EPR II    & EPR II i   \\ \hline
g-x                       & 2.00324     & 2.0028424 & 2.0028424 & 2.0028709 & 2.0028709  \\ \hline
g-y                       & 2.00263     & 2.0026955 & 2.0026955 & 2.0026882 & 2.0026882  \\ \hline
g-z                       & 2.00218     & 2.0021843 & 2.0021843 & 2.0021857 & 2.0021857  \\ \hline
\text{max absolute error} &             & 0.0003976 & 0.0003976 & 0.0003691 & 0.0003691  \\ \hline
\text{average error}      &             & 0.0001093 & 0.0001093 & 0.0001017 & 0.0001017  \\ \hline
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
                          & \text{experiments} & \text{cc-pVDZ} & \text{cc-pVDZ i} & \text{EPR II} & \text{EPR II i}  \\ \hline
g_x                       & 2.00324            & 2.0028344      & 2.0028344        & 2.0028687     & 2.0028687        \\ \hline
g_y                       & 2.00263            & 2.0027116      & 2.0027116        & 2.0027009     & 2.0027009        \\ \hline
g_z                       & 2.00218            & 2.0021863      & 2.0021863        & 2.002188      & 2.002188         \\ \hline
\text{max absolute error} &                    & 0.0004056      & 0.0004056        & 0.0003713     & 0.0003713        \\ \hline
\text{average error}      &                    & 0.0001059      & 0.0001059        & 0.0000975     & 0.0000975        \\ \hline
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
                          & \text{experiments} & \text{cc-pVDZ} & \text{cc-pVDZ i} & \text{EPR II} & \text{EPR II i}  \\ \hline
g_x                       & 2.00324            & 2.0028328      & 2.0028328        & 2.0028687     & 2.0028687        \\ \hline
g_y                       & 2.00263            & 2.0027091      & 2.0027091        & 2.0027033     & 2.0027033        \\ \hline
g_z                       & 2.00218            & 2.0021842      & 2.0021842        & 2.0021858     & 2.0021858        \\ \hline
\text{max absolute error} &                    & 0.0004072      & 0.0004072        & 0.0003713     & 0.0003713        \\ \hline
\text{average error}      &                    & 0.0001080      & 0.0001080        & 0.0000974     & 0.0000974        \\ \hline
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
                          & \text{experiments} & \text{cc-pVDZ} & \text{cc-pVDZ i} & \text{EPR II} & \text{EPR II i}  \\ \hline
g_x                       & 2.00324            & 2.0028218      & 2.0028218        & 2.0028596     & 2.0028596        \\ \hline
g_y                       & 2.00263            & 2.0026959      & 2.0026959        & 2.0026923     & 2.0026923        \\ \hline
g_z                       & 2.00218            & 2.0021625      & 2.0021625        & 2.002155      & 2.002155         \\ \hline
\text{max absolute error} &                    & 0.0004182      & 0.0004182        & 0.0003804     & 0.0003804        \\ \hline
\text{average error}      &                    & 0.0001233      & 0.0001233        & 0.0001144     & 0.0001144        \\ \hline
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
                          & \text{experiments} & \text{cc-pVDZ} & \text{cc-pVDZ i} & \text{EPR II} & \text{EPR II i}  \\ \hline
g_x                       & 2.00324            & 2.0029419      & 2.0029419        & 2.0029459     & 2.0029459        \\ \hline
g_y                       & 2.00263            & 2.0021429      & 2.0021429        & 2.0021419     & 2.0021419        \\ \hline
g_z                       & 2.00218            & 2.0016572      & 2.0016572        & 2.0016379     & 2.0016379        \\ \hline
\text{max absolute error} &                    & 0.0005228      & 0.0005228        & 0.0005421     & 0.0005421        \\ \hline
\text{average error}      &                    & 0.0004360      & 0.0004360        & 0.0004414     & 0.0004414        \\ \hline
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
                          & \text{experiments} & \text{cc-pVDZ} & \text{cc-pVDZ i} & \text{EPR II} & \text{EPR II i}  \\ \hline
g_x                       & 2.00324            & 2.0069736      & 2.0069736        & 2.0069279     & 2.0069279        \\ \hline
g_y                       & 2.00263            & 2.0035202      & 2.0035202        & 2.0034545     & 2.0034545        \\ \hline
g_z                       & 2.00218            & 2.0022107      & 2.0022107        & 2.0022073     & 2.0022073        \\ \hline
\text{max absolute error} &                    & -0.0000307     & -0.0000307       & -0.0000273    & -0.0000273       \\ \hline
\text{average error}      &                    & -0.0015515     & -0.0015515       & -0.0015132    & -0.0015132       \\ \hline
\end{array}
```

# Triple bond brocken
The Carbon with larger radius is the one "with the radical"
<div style="display: flex;">
  <img src="/7_0-triple_broken/chem.png" alt="Image 1" width="20%">
  <img src="/7_0-triple_broken/opt.png" alt="Image 2" width="20%">
</div>

```math
\begin{array}{|l|c|c|c|c|}
\hline
                          & \text{experiments} & \text{cc-pVDZ} & \text{cc-pVDZ i} & \text{EPR II} & \text{EPR II i}  \\ \hline
g_x                       & 2.00324            & 2.0125144      & 2.0125144        & 2.0219089     & 2.0219089        \\ \hline
g_y                       & 2.00263            & 2.0031968      & 2.0031968        & 2.0031983     & 2.0031983        \\ \hline
g_z                       & 2.00218            & 2.0020959      & 2.0020959        & 2.0020915     & 2.0020915        \\ \hline
\text{max absolute error} &                    & 0.0000841      & 0.0000841        & 0.0000885     & 0.0000885        \\ \hline
\text{average error}      &                    & -0.0032524     & -0.0032524       & -0.0063829    & -0.0063829       \\ \hline
\end{array}
```


# Hshift side-chain Radical
The Carbon with larger radius is the one "with the radical"
<div style="display: flex;">
  <img src="/8_0-Hshift_FarRad1/chem.png" alt="Image 1" width="20%">
  <img src="/8_0-Hshift_FarRad1/opt.png" alt="Image 2" width="20%">
</div>

```math
\begin{array}{|l|c|c|c|c|}
\hline
                          & \text{experiments} & \text{cc-pVDZ} & \text{cc-pVDZ i} & \text{EPR II} & \text{EPR II i}  \\ \hline
g_x                       & 2.00324            & 2.0028002      & 2.0028002        & 2.0028061     & 2.0028061        \\ \hline
g_y                       & 2.00263            & 2.0027434      & 2.0027434        & 2.0027633     & 2.0027633        \\ \hline
g_z                       & 2.00218            & 2.0021818      & 2.0021818        & 2.0021821     & 2.0021821        \\ \hline
\text{max absolute error} &                    & 0.0004398      & 0.0004398        & 0.0004339     & 0.0004339        \\ \hline
\text{average error}      &                    & 0.0001082      & 0.0001082        & 0.0000995     & 0.0000995        \\ \hline
\end{array}
```

# Hshift Extreme Far Radical
The Carbon with larger radius is the one "with the radical"
<div style="display: flex;">
  <img src="/8_1-Hshift_FarRad2/chem.png" alt="Image 1" width="20%">
  <img src="/8_1-Hshift_FarRad2/opt.png" alt="Image 2" width="20%">
</div>

```math
\begin{array}{|l|c|c|c|c|}
\hline
                          & \text{experiments} & \text{cc-pVDZ} & \text{cc-pVDZ i} & \text{EPR II} & \text{EPR II i}  \\ \hline
g_x                       & 2.00324            & 2.0027203      & 2.0027203        & 2.0027372     & 2.0027372        \\ \hline
g_y                       & 2.00263            & 2.00271        & 2.00271          & 2.0027246     & 2.0027246        \\ \hline
g_z                       & 2.00218            & 2.0021852      & 2.0021852        & 2.0021729     & 2.0021729        \\ \hline
\text{max absolute error} &                    & 0.0005197      & 0.0005197        & 0.0005028     & 0.0005028        \\ \hline
\text{average error}      &                    & 0.0001448      & 0.0001448        & 0.0001384     & 0.0001384        \\ \hline
\end{array}
```

# Rhop side-chain Radical
The Carbon with larger radius is the one "with the radical"
<div style="display: flex;">
  <img src="/9_0-Rhop_FarRad1/chem.png" alt="Image 1" width="20%">
  <img src="/9_0-Rhop_FarRad1/opt.png" alt="Image 2" width="20%">
</div>

```math
\begin{array}{|l|c|c|c|c|}
\hline
                   & experiments & cc-pVDZ   & cc-pVDZ i & EPR II    & EPR II i   \\ \hline
g-x                & 2.00324     & 2.0028028 & 2.0028028 & 2.0028092 & 2.0028092  \\ \hline
g-y                & 2.00263     & 2.002737  & 2.002737  & 2.0027579 & 2.0027579  \\ \hline
g-z                & 2.00218     & 2.0021831 & 2.0021831 & 2.0021827 & 2.0021827  \\ \hline
max absolute error &             & 0.0004372 & 0.0004372 & 0.0004308 & 0.0004308  \\ \hline
average error      &             & 0.0001090 & 0.0001090 & 0.0001001 & 0.0001001  \\ \hline
\end{array}
```

# Rhop extreme far radical
The Carbon with larger radius is the one "with the radical"
<div style="display: flex;">
  <img src="/9_1-Rhop_FarRad2/chem.png" alt="Image 1" width="20%">
  <img src="/9_1-Rhop_FarRad2/opt.png" alt="Image 2" width="20%">
</div>

```math
\begin{array}{|l|c|c|c|c|}
\hline
                          & \text{experiments} & \text{cc-pVDZ} & \text{cc-pVDZ i} & \text{EPR II} & \text{EPR II i}  \\ \hline
g_x                       & 2.00324            & 2.0027178      & 2.0027178        & 2.0027359     & 2.0027359        \\ \hline
g_y                       & 2.00263            & 2.0027086      & 2.0027086        & 2.0027201     & 2.0027201        \\ \hline
g_z                       & 2.00218            & 2.0021849      & 2.0021849        & 2.002173      & 2.002173         \\ \hline
\text{max absolute error} &                    & 0.0005222      & 0.0005222        & 0.0005041     & 0.0005041        \\ \hline
\text{average error}      &                    & 0.0001462      & 0.0001462        & 0.0001403     & 0.0001403        \\ \hline
\end{array}
```

