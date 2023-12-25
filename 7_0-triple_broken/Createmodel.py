from myutils.ase_utils.molecules import MoleculeSetter
from ase.io import read, write
import numpy as np
from nglview import show_ase

mol = read('../6_0-primary_in_triple/opt.xyz')

# RadHop
ms = MoleculeSetter(mol)
ms.atoms.pop(0)

write("./model.xyz", ms.atoms)