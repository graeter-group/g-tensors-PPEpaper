from myutils.ase_utils.molecules import MoleculeSetter
from ase.io import read, write
import numpy as np
from ase.visualize import view
from ase import Atom

mol = read('../reduced2/opt.xyz')
ms = MoleculeSetter(mol)
CHd = ms.atoms.get_distance(0, 45)

ms = MoleculeSetter(mol)
for index in [45, 33, 1, 0]:
    ms.atoms.pop(index)

ms.xy_alignment(1, 4, 5, center=1)
H = Atom('H', position=[-CHd, 0, 0])
ms.atoms += H

write("./model.xyz", ms.atoms)
