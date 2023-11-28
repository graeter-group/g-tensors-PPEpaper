from myutils.ase_utils.molecules import MoleculeSetter
from ase.io import read, write
from ase import Atom
import numpy as np


molecule = read('../reduced/opt.xyz')
CHd = molecule.get_distance(5, 9)
ring=2.75/2

# RadHop
ms = MoleculeSetter(molecule)
#ms.atoms.pop(12)

# RadHop with left radical
ms.xy_alignment(6, 3, 4)
ms.apply_trans(np.identity(3), shift=-ms.atoms[35].position)

ms.atoms.pop(37) # H attached to the Carbon
new_phenyl = ms.atoms[3: 9].copy()
ms.atoms += new_phenyl
ms.apply_trans(np.identity(3), shift=-ms.atoms[-6].position - [1.43, 0, 0],
               indexes=[39, 40, 41, 42, 43, 44])

ms.xy_alignment(39, 42)
H = Atom('H', position=[ring+CHd, 0, 0])
ms.atoms += H
ms.xy_alignment(40, 43)
H = Atom('H', position=[ring+CHd, 0, 0])
ms.atoms += H
H = Atom('H', position=[-ring-CHd, 0, 0])
ms.atoms += H
ms.xy_alignment(41, 44)
H = Atom('H', position=[ring+CHd, 0, 0])
ms.atoms += H
H = Atom('H', position=[-ring-CHd, 0, 0])
ms.atoms += H
ms.xy_alignment(3, 6, 7)

ms.atoms.pop(36)
ms.atoms.pop(1)
ms.atoms.pop(0)

write("./model.xyz", ms.atoms)