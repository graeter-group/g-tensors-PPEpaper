from myutils.ase_utils.molecules import MoleculeSetter
from ase.io import read, write
import numpy as np


molecule = read('../reduced/opt.xyz')
CHd = molecule.get_distance(0, 36)
ring=2.75/2

# AlkylShift
ms = MoleculeSetter(molecule)
atoms2remove = [36, 1, 0]
for atom in atoms2remove:
    ms.atoms.pop(atom)

CCd = ms.atoms.get_distance(2, 9)
ms.apply_trans(ms.rot_z(-0.2*np.pi), indexes=list(range(12,21)) + [35])
ms.apply_trans(ms.rot_x(-np.pi), indexes=list(range(12,21)) + [35])
ms.xy_alignment(1, 12, center=1)
ms.apply_trans(np.identity(3), shift=[CCd, 0, 0] - ms.atoms[12].position,
               indexes=list(range(12,21)) + [35])
ms.xy_alignment(4, 1, 2)

write("./model.xyz", ms.atoms)
