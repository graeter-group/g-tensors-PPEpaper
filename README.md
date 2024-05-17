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

### Orca
- With Phenyl group:
BDE triple bond:  0.28992840000000797  Ha /  753.8138400000207  kJ/mol
BDE single bond:  0.19708169999989877  Ha /  512.4124199997368  kJ/mol


- Without Phenyl group
BDE triple bond:  0.15881231000003027  Ha /  412.9120060000787  kJ/mol
BDE single bond:  0.07075292000013178  Ha /  183.95759200034263  kJ/mol

### g09
- With Phenyl group:
BDE triple bond:  0.3037380000000667  Ha /  789.7188000001734  kJ/mol
BDE single bond:  0.2125549999998384  Ha /  552.6429999995798  kJ/mol


- Without Phenyl group
BDE triple bond:  0.30262000000016087  Ha /  786.8120000004183  kJ/mol
BDE single bond:  0.21594000000027336  Ha /  561.4440000007107  kJ/mol

# G-values

### Summary table

```math
\begin{array}{|l|c|c|c|c|}
\hline
                                     & g-x       & g-y       & g-z       & \text{max abs error} & \text{avrg error}  \\ \hline
\text{A) AlkylShift}         & 2.0027921 & 2.0027617 & 2.002214  & 0.0004479            & 0.0000941          \\ \hline
\text{B) Hshift}             & 2.0028401 & 2.0027267 & 2.0021777 & 0.0003999            & 0.0001018          \\ \hline
\text{C) Rhop}               & 2.0028697 & 2.0026887 & 2.0021882 & 0.0003703            & 0.0001011          \\ \hline
\text{D) Rhop-LeftPhenyl}    & 2.0028722 & 2.0026881 & 2.0021858 & 0.0003678            & 0.0001013          \\ \hline
\text{E) Rhop-RightPhenyl}   & 2.0028699 & 2.0027005 & 2.0021878 & 0.0003701            & 0.0000973          \\ \hline
\text{F) inchain}            & 2.0028729 & 2.0026999 & 2.0021857 & 0.0003671            & 0.0000972          \\ \hline
\text{G) inchainLarger}      & 2.0028614 & 2.0026918 & 2.0021557 & 0.0003786            & 0.0001137          \\ \hline
\text{H) primary-in-ring}    & 2.0029464 & 2.0021418 & 2.001633  & 0.0005470            & 0.0004429          \\ \hline
\text{I) primary-in-triple}  & 2.0069655 & 2.0034297 & 2.0022073 & -0.0000273           & -0.0015175         \\ \hline
\text{J) triple-broken}      & 2.0269326 & 2.0031967 & 2.0020897 & 0.0000903            & -0.0080563         \\ \hline
\text{K) Hshift-FarRad1}     & 2.0028127 & 2.0027716 & 2.0021815 & 0.0004273            & 0.0000947          \\ \hline
\text{L) Hshift-FarRad2}     & 2.0027441 & 2.0027325 & 2.0021738 & 0.0004959            & 0.0001332          \\ \hline
\text{M) Rhop-FarRad1}       & 2.0028156 & 2.0027666 & 2.0021818 & 0.0004244            & 0.0000953          \\ \hline
\text{N) Rhop-FarRad2}       & 2.002743  & 2.0027282 & 2.002174  & 0.0004970            & 0.0001349          \\ \hline
\text{Experiment}                    & 2.00324   & 2.00263   & 2.00218   &                      &                    \\ \hline
\end{array}
```

<div style="text-align:center">
  <img src="/structuresPPE.png" alt="Image 1" width="80%">
</div>

**Note:** the names on the next tables means
- cc-pVDZ: cc-pVDZ basis set, g-values with the origin in the center of the electronic distribution.
- cc-pVDZ i: cc-pVDZ basis set, g-values computed with invariant method.
- cc-pVDZ: EPR_II basis set (created to this aim), g-values with the origin in the center of the electronic distribution.
- cc-pVDZ i: EPR_II basis set (created to this aim), g-values computed with invariant method. This is suppossed to give the most precise outcomes.

### AlkylShift
The Carbon with larger radius is the one "with the radical"
<div style="display: flex;">
<img src="/1_0-AlkylShift/opt.png" alt="Image 1" width="20%">
<img src="/1_0-AlkylShift/chem.png" alt="Image 2" width="20%">
</div>

```math
\begin{array}{|l|c|c|c|c|}
\hline
                          & \text{experiments} & \text{cc-pVDZ} & \text{cc-pVDZ i} & \text{EPR II} & \text{EPR II i}  \\ \hline
g_x                       & 2.00324            & 2.002902       & 2.0027826        & 2.0029046     & 2.0027921        \\ \hline
g_y                       & 2.00263            & 2.002772       & 2.0027585        & 2.0027801     & 2.0027617        \\ \hline
g_z                       & 2.00218            & 2.0023613      & 2.0022185        & 2.0023653     & 2.002214         \\ \hline
\text{max absolute error} &                    & 0.0003380      & 0.0004574        & 0.0003354     & 0.0004479        \\ \hline
\text{average error}      &                    & 0.0000049      & 0.0000968        & 0.0000000     & 0.0000941        \\ \hline
\end{array}
```

### Hshift
The Carbon with larger radius is the one "with the radical"
<div style="display: flex;">
<img src="/2_0-Hshift/opt.png" alt="Image 1" width="20%">
<img src="/2_0-Hshift/chem.png" alt="Image 2" width="20%">
</div>

```math
\begin{array}{|l|c|c|c|c|}
\hline
                          & \text{experiments} & \text{cc-pVDZ} & \text{cc-pVDZ i} & \text{EPR II} & \text{EPR II i}  \\ \hline
g_x                       & 2.00324            & 2.0028359      & 2.0028217        & 2.0028587     & 2.0028401        \\ \hline
g_y                       & 2.00263            & 2.0027302      & 2.0027232        & 2.0026851     & 2.0027267        \\ \hline
g_z                       & 2.00218            & 2.0022594      & 2.0021786        & 2.0022577     & 2.0021777        \\ \hline
\text{max absolute error} &                    & 0.0004041      & 0.0004183        & 0.0003813     & 0.0003999        \\ \hline
\text{average error}      &                    & 0.0000748      & 0.0001088        & 0.0000828     & 0.0001018        \\ \hline
\end{array}
```

### Rhop
The Carbon with larger radius is the one "with the radical"
<div style="display: flex;">
<img src="/3_0-Rhop/opt.png" alt="Image 1" width="20%">
<img src="/3_0-Rhop/chem.png" alt="Image 2" width="20%">
</div>

```math
\begin{array}{|l|c|c|c|c|}
\hline
                          & \text{experiments} & \text{cc-pVDZ} & \text{cc-pVDZ i} & \text{EPR II} & \text{EPR II i}  \\ \hline
g_x                       & 2.00324            & 2.0028608      & 2.0028423        & 2.0028944     & 2.0028697        \\ \hline
g_y                       & 2.00263            & 2.0027038      & 2.002698         & 2.0026433     & 2.0026887        \\ \hline
g_z                       & 2.00218            & 2.0022715      & 2.0021861        & 2.0022684     & 2.0021882        \\ \hline
\text{max absolute error} &                    & 0.0003792      & 0.0003977        & 0.0003456     & 0.0003703        \\ \hline
\text{average error}      &                    & 0.0000713      & 0.0001079        & 0.0000813     & 0.0001011        \\ \hline
\end{array}
```

### Rhop-LeftPhenyl
The Carbon with larger radius is the one "with the radical"
<div style="display: flex;">
<img src="/3_1-Rhop-LeftPhenyl/opt.png" alt="Image 1" width="20%">
<img src="/3_1-Rhop-LeftPhenyl/chem.png" alt="Image 2" width="20%">
</div>

```math
\begin{array}{|l|c|c|c|c|}
\hline
                          & \text{experiments} & \text{cc-pVDZ} & \text{cc-pVDZ i} & \text{EPR II} & \text{EPR II i}  \\ \hline
g_x                       & 2.00324            & 2.0028855      & 2.0028413        & 2.0028726     & 2.0028722        \\ \hline
g_y                       & 2.00263            & 2.0027167      & 2.0026956        & 2.0026196     & 2.0026881        \\ \hline
g_z                       & 2.00218            & 2.002321       & 2.0021841        & 2.0023143     & 2.0021858        \\ \hline
\text{max absolute error} &                    & 0.0003545      & 0.0003987        & 0.0003674     & 0.0003678        \\ \hline
\text{average error}      &                    & 0.0000423      & 0.0001097        & 0.0000812     & 0.0001013        \\ \hline
\end{array}
```

### Rhop-RightPhenyl
The Carbon with larger radius is the one "with the radical"
<div style="display: flex;">
<img src="/3_2-Rhop-RightPhenyl/opt.png" alt="Image 1" width="20%">
<img src="/3_2-Rhop-RightPhenyl/chem.png" alt="Image 2" width="20%">
</div>

```math
\begin{array}{|l|c|c|c|c|}
\hline
                          & \text{experiments} & \text{cc-pVDZ} & \text{cc-pVDZ i} & \text{EPR II} & \text{EPR II i}  \\ \hline
g_x                       & 2.00324            & 2.0028408      & 2.0028327        & 2.0029394     & 2.0028699        \\ \hline
g_y                       & 2.00263            & 2.0027108      & 2.0027108        & 2.0026909     & 2.0027005        \\ \hline
g_z                       & 2.00218            & 2.0022471      & 2.0021856        & 2.0022474     & 2.0021878        \\ \hline
\text{max absolute error} &                    & 0.0003992      & 0.0004073        & 0.0003006     & 0.0003701        \\ \hline
\text{average error}      &                    & 0.0000838      & 0.0001070        & 0.0000574     & 0.0000973        \\ \hline
\end{array}
```

### inchain
The Carbon with larger radius is the one "with the radical"
<div style="display: flex;">
<img src="/4_0-inchain/opt.png" alt="Image 1" width="20%">
<img src="/4_0-inchain/chem.png" alt="Image 2" width="20%">
</div>

```math
\begin{array}{|l|c|c|c|c|}
\hline
                          & \text{experiments} & \text{cc-pVDZ} & \text{cc-pVDZ i} & \text{EPR II} & \text{EPR II i}  \\ \hline
g_x                       & 2.00324            & 2.0028335      & 2.0028328        & 2.0028977     & 2.0028729        \\ \hline
g_y                       & 2.00263            & 2.002724       & 2.0027088        & 2.0026735     & 2.0026999        \\ \hline
g_z                       & 2.00218            & 2.0022731      & 2.0021842        & 2.0022707     & 2.0021857        \\ \hline
\text{max absolute error} &                    & 0.0004065      & 0.0004072        & 0.0003423     & 0.0003671        \\ \hline
\text{average error}      &                    & 0.0000731      & 0.0001081        & 0.0000694     & 0.0000972        \\ \hline
\end{array}
```

### inchainLarger
The Carbon with larger radius is the one "with the radical"
<div style="display: flex;">
<img src="/4_1-inchainLarger/opt.png" alt="Image 1" width="20%">
<img src="/4_1-inchainLarger/chem.png" alt="Image 2" width="20%">
</div>

```math
\begin{array}{|l|c|c|c|c|}
\hline
                          & \text{experiments} & \text{cc-pVDZ} & \text{cc-pVDZ i} & \text{EPR II} & \text{EPR II i}  \\ \hline
g_x                       & 2.00324            & 2.0028397      & 2.002821         & 2.0028996     & 2.0028614        \\ \hline
g_y                       & 2.00263            & 2.0027243      & 2.0026962        & 2.0026731     & 2.0026918        \\ \hline
g_z                       & 2.00218            & 2.0022746      & 2.0021626        & 2.0022718     & 2.0021557        \\ \hline
\text{max absolute error} &                    & 0.0004003      & 0.0004190        & 0.0003404     & 0.0003786        \\ \hline
\text{average error}      &                    & 0.0000705      & 0.0001234        & 0.0000685     & 0.0001137        \\ \hline
\end{array}
```

### primary_in_ring
The Carbon with larger radius is the one "with the radical"
<div style="display: flex;">
<img src="/5_0-primary_in_ring/opt.png" alt="Image 1" width="20%">
<img src="/5_0-primary_in_ring/chem.png" alt="Image 2" width="20%">
</div>

```math
\begin{array}{|l|c|c|c|c|}
\hline
                          & \text{experiments} & \text{cc-pVDZ} & \text{cc-pVDZ i} & \text{EPR II} & \text{EPR II i}  \\ \hline
g_x                       & 2.00324            & 2.0031548      & 2.0029421        & 2.0031225     & 2.0029464        \\ \hline
g_y                       & 2.00263            & 2.0021617      & 2.0021429        & 2.0021539     & 2.0021418        \\ \hline
g_z                       & 2.00218            & 2.001818       & 2.0016573        & 2.0017157     & 2.001633         \\ \hline
\text{max absolute error} &                    & 0.0004683      & 0.0005227        & 0.0004761     & 0.0005470        \\ \hline
\text{average error}      &                    & 0.0003052      & 0.0004359        & 0.0003526     & 0.0004429        \\ \hline
\end{array}
```

### primary_in_triple
The Carbon with larger radius is the one "with the radical"
<div style="display: flex;">
<img src="/6_0-primary_in_triple/opt.png" alt="Image 1" width="20%">
<img src="/6_0-primary_in_triple/chem.png" alt="Image 2" width="20%">
</div>

```math
\begin{array}{|l|c|c|c|c|}
\hline
                          & \text{experiments} & \text{cc-pVDZ} & \text{cc-pVDZ i} & \text{EPR II} & \text{EPR II i}  \\ \hline
g_x                       & 2.00324            & 2.0069623      & 2.006973         & 2.0069426     & 2.0069655        \\ \hline
g_y                       & 2.00263            & 2.0038729      & 2.003522         & 2.0037258     & 2.0034297        \\ \hline
g_z                       & 2.00218            & 2.0023758      & 2.0022109        & 2.002365      & 2.0022073        \\ \hline
\text{max absolute error} &                    & -0.0001958     & -0.0000309       & -0.0001850    & -0.0000273       \\ \hline
\text{average error}      &                    & -0.0017203     & -0.0015520       & -0.0016611    & -0.0015175       \\ \hline
\end{array}
```

### triple_broken
The Carbon with larger radius is the one "with the radical"
<div style="display: flex;">
<img src="/7_0-triple_broken/opt.png" alt="Image 1" width="20%">
<img src="/7_0-triple_broken/chem.png" alt="Image 2" width="20%">
</div>

```math
\begin{array}{|l|c|c|c|c|}
\hline
                          & \text{experiments} & \text{cc-pVDZ} & \text{cc-pVDZ i} & \text{EPR II} & \text{EPR II i}  \\ \hline
g_x                       & 2.00324            & 2.0126297      & 2.012587         & 2.0270687     & 2.0269326        \\ \hline
g_y                       & 2.00263            & 2.0037159      & 2.0031968        & 2.0036261     & 2.0031967        \\ \hline
g_z                       & 2.00218            & 2.0023688      & 2.0020968        & 2.0023129     & 2.0020897        \\ \hline
\text{max absolute error} &                    & -0.0001888     & 0.0000832        & -0.0001329    & 0.0000903        \\ \hline
\text{average error}      &                    & -0.0035548     & -0.0032769       & -0.0083192    & -0.0080563       \\ \hline
\end{array}
```

### Hshift_FarRad1
The Carbon with larger radius is the one "with the radical"
<div style="display: flex;">
<img src="/8_0-Hshift_FarRad1/opt.png" alt="Image 1" width="20%">
<img src="/8_0-Hshift_FarRad1/chem.png" alt="Image 2" width="20%">
</div>

```math
\begin{array}{|l|c|c|c|c|}
\hline
                          & \text{experiments} & \text{cc-pVDZ} & \text{cc-pVDZ i} & \text{EPR II} & \text{EPR II i}  \\ \hline
g_x                       & 2.00324            & 2.0028834      & 2.0028003        & 2.0029103     & 2.0028127        \\ \hline
g_y                       & 2.00263            & 2.0027474      & 2.0027434        & 2.0028148     & 2.0027716        \\ \hline
g_z                       & 2.00218            & 2.0022701      & 2.0021818        & 2.0022681     & 2.0021815        \\ \hline
\text{max absolute error} &                    & 0.0003566      & 0.0004397        & 0.0003297     & 0.0004273        \\ \hline
\text{average error}      &                    & 0.0000497      & 0.0001082        & 0.0000189     & 0.0000947        \\ \hline
\end{array}
```

### Hshift_FarRad2
The Carbon with larger radius is the one "with the radical"
<div style="display: flex;">
<img src="/8_1-Hshift_FarRad2/opt.png" alt="Image 1" width="20%">
<img src="/8_1-Hshift_FarRad2/chem.png" alt="Image 2" width="20%">
</div>

```math
\begin{array}{|l|c|c|c|c|}
\hline
                          & \text{experiments} & \text{cc-pVDZ} & \text{cc-pVDZ i} & \text{EPR II} & \text{EPR II i}  \\ \hline
g_x                       & 2.00324            & 2.0030016      & 2.00272          & 2.0030251     & 2.0027441        \\ \hline
g_y                       & 2.00263            & 2.0028498      & 2.0027097        & 2.0028914     & 2.0027325        \\ \hline
g_z                       & 2.00218            & 2.0024106      & 2.0021851        & 2.0024004     & 2.0021738        \\ \hline
\text{max absolute error} &                    & 0.0002384      & 0.0005200        & 0.0002149     & 0.0004959        \\ \hline
\text{average error}      &                    & -0.0000707     & 0.0001451        & -0.0000890    & 0.0001332        \\ \hline
\end{array}
```

### Rhop_FarRad1
The Carbon with larger radius is the one "with the radical"
<div style="display: flex;">
<img src="/9_0-Rhop_FarRad1/opt.png" alt="Image 1" width="20%">
<img src="/9_0-Rhop_FarRad1/chem.png" alt="Image 2" width="20%">
</div>

```math
\begin{array}{|l|c|c|c|c|}
\hline
\end{array}
```

### Rhop_FarRad2
The Carbon with larger radius is the one "with the radical"
<div style="display: flex;">
<img src="/9_1-Rhop_FarRad2/opt.png" alt="Image 1" width="20%">
<img src="/9_1-Rhop_FarRad2/chem.png" alt="Image 2" width="20%">
</div>

```math
\begin{array}{|l|c|c|c|c|}
\hline
                          & \text{experiments} & \text{cc-pVDZ} & \text{cc-pVDZ i} & \text{EPR II} & \text{EPR II i}  \\ \hline
g_x                       & 2.00324            & 2.0030102      & 2.0027176        & 2.0030353     & 2.002743         \\ \hline
g_y                       & 2.00263            & 2.0028492      & 2.0027082        & 2.0028891     & 2.0027282        \\ \hline
g_z                       & 2.00218            & 2.0024236      & 2.0021849        & 2.0024135     & 2.002174         \\ \hline
\text{max absolute error} &                    & 0.0002298      & 0.0005224        & 0.0002047     & 0.0004970        \\ \hline
\text{average error}      &                    & -0.0000777     & 0.0001464        & -0.0000960    & 0.0001349        \\ \hline
\end{array}
```


# Plot of g-values.

<div style="display: flex;">
<img src="/analysis/g-values.png" alt="Image 1" width="50%">
</div>
