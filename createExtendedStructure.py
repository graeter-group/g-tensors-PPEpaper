from myutils.ase_utils.molecules import MoleculeSetter
from ase.io import read, write
from ase.visualize import view
from ase import Atom
import numpy as np


molecule = read('../opt.xyz')
CHd = molecule.get_distance(5, 9)
ring=2.75/2

# RadHop with left radical
ms = MoleculeSetter(molecule)
ms.xy_alignment(6, 3, 4)
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

write("./left/Rhop.xyz", ms.atoms)

# RadHop with right Radical
molecule = read('../opt.xyz')
ms = MoleculeSetter(molecule)
ms.xy_alignment(1, 0, 4, center=0)
ms.atoms.pop(35) # H attached to the Carbon

new_phenyl = ms.atoms[3: 9].copy()
ms.atoms += new_phenyl
ms.apply_trans(np.identity(3), shift=-ms.atoms[-3].position  + [1.43, 0, 0],
               indexes=[38, 39, 40, 41, 42, 43])
ms.xy_alignment(41, 38)
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
ms.xy_alignment(6, 3, 4)

write("./right/Rhop.xyz", ms.atoms)