from nglview import show_ase
from myutils.ase_utils.molecules import MoleculeSetter
from ase.io import read, write
from ase import Atom, Atoms
import numpy as np



molecule = read('../reduced/opt.xyz')
CHd = molecule.get_distance(5, 9)
ring=2.75/2

# RadHop
ms = MoleculeSetter(molecule)

# RadHop with left radical
ms.xy_alignment(6, 3, 4)
at1 = ms.atoms.pop(12)
ms.apply_trans(np.identity(3), shift=-ms.atoms[34].position)
ms.atoms.pop(36) # H attached to the Carbon

new_phenyl = ms.atoms[3: 9].copy()
ms.atoms += new_phenyl
ms.apply_trans(np.identity(3), shift=-ms.atoms[-6].position - [1.43, 0, 0],
               indexes=[38, 39, 40, 41, 42, 43])
ms.xy_alignment(38, 41)
H = Atom('H', position=[ring+CHd, 0, 0])
ms.atoms += H
ms.xy_alignment(39, 42)
H = Atom('H', position=[ring+CHd, 0, 0])
ms.atoms += H
H = Atom('H', position=[-ring-CHd, 0, 0])
ms.atoms += H
ms.xy_alignment(40, 43)
H = Atom('H', position=[ring+CHd, 0, 0])
ms.atoms += H
H = Atom('H', position=[-ring-CHd, 0, 0])
ms.atoms += H
ms.xy_alignment(3, 6, 7)


atoms = ms.atoms
cc_dist = atoms.get_distance(34, 37)
atoms.pop(35)

ms = MoleculeSetter(atoms)
ms.xy_alignment(2, 34, 7, center=34)
new_phenyl = atoms[37: 48].copy()
ms.xy_alignment(1, 0, 8, center=0)
ms.atoms += new_phenyl
ms.xy_alignment(40, 37)

ms.xy_alignment(6, 3, 4)
ms.atoms += at1

write("./model.xyz", ms.atoms)