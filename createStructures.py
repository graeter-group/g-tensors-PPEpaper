from myutils.ase_utils.molecules import MoleculeSetter
from ase.io import read, write
from ase.visualize import view
from ase import Atom
import numpy as np


molecule = read('./reduced/opt.xyz')
CHd = molecule.get_distance(0, 36)
ring=2.75/2
# 
# # H shift
# ms = MoleculeSetter(molecule)
# atoms2remove = [36, 12, 1, 0]
# for atom in atoms2remove:
#     ms.atoms.pop(atom)
# ms.xy_alignment(1, 4, center=1)
# ms.atoms += Atom('H', position=[-CHd, 0, 0])
# ms.xy_alignment(4, 1, 2)
# 
# write("Hshift/Hshift.xyz", ms.atoms)
# 
# # AlkylShift
# ms = MoleculeSetter(molecule)
# atoms2remove = [36, 1, 0]
# for atom in atoms2remove:
#     ms.atoms.pop(atom)
# 
# CCd = ms.atoms.get_distance(2, 9)
# ms.apply_trans(ms.rot_z(-0.2*np.pi), indexes=list(range(12,21)) + [35])
# ms.apply_trans(ms.rot_x(-np.pi), indexes=list(range(12,21)) + [35])
# ms.xy_alignment(1, 12, center=1)
# ms.apply_trans(np.identity(3), shift=[CCd, 0, 0] - ms.atoms[12].position,
#                indexes=list(range(12,21)) + [35])
# ms.xy_alignment(4, 1, 2)
# 
# write("AlkylShift/Ashift.xyz", ms.atoms)
# 
# # RadHop
# ms = MoleculeSetter(molecule)
# ms.atoms.pop(12)
# ms.xy_alignment(6, 3, 4)
# 
# write("Rhop/Rhop.xyz", ms.atoms)
# 
# # RadHop
# ms = MoleculeSetter(molecule)
# ms.atoms.pop(12)
# ms.xy_alignment(6, 3, 4)
# 
# write("Rhop/Rhop.xyz", ms.atoms)


# RadHop with left phenyl
ms = MoleculeSetter(molecule)
ms.xy_alignment(6, 3, 4)
ms.apply_trans(np.identity(3), shift=-ms.atoms[35].position)
ms.atoms.pop(37) # H attached to the Carbon
ms.atoms.pop(12) # radical

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
ms.xy_alignment(3, 6)

write("Rhop/extended1/Rhop.xyz", ms.atoms)