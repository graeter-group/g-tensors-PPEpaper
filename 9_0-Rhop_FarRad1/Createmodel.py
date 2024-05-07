from myutils.ase_utils.molecules import MoleculeSetter
from ase.io import read, write
import numpy as np
from ase.visualize import view
from ase import Atom

mol = read('../reduced2/opt.xyz')
ms = MoleculeSetter(mol)

ms.atoms.pop(33)

ms.xy_alignment(3, 6, 32)

write("./model.xyz", ms.atoms)
