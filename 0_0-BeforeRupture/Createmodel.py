from myutils.ase_utils.molecules import MoleculeSetter
from ase.io import read, write
import numpy as np
from nglview import show_ase

res1 = read('../5_0-primary_in_ring/opt_cc-pVDZ.xyz')
res2 = read('../6_0-primary_in_triple/opt_cc-pVDZ.xyz')

# RadHop
ms1 = MoleculeSetter(res1)
ms1.xy_alignment(1, 39, 41, center=1)
ms1.apply_trans(trans=np.identity(3), shift=[1.42, 0, 0])
#ms.atoms.pop(12)

ms2 = MoleculeSetter(res2)
ms2.xy_alignment(41, 0, 4, center=0)

write("./model.xyz", ms1.atoms + ms2.atoms)