from myutils.ase_utils.molecules import MoleculeSetter
from ase.io import read, write
from ase.visualize import view
from ase import Atom

molecule = read('reduced.pdb')
CHd = molecule.get_distance(20, 21)

ms = MoleculeSetter(molecule)

ms.xy_alignment(0, 1, center=0)
ms.atoms += Atom('H', position=[-CHd, 0, 0])

ms.xy_alignment(35, 2, center=35)
ms.atoms += Atom('H', position=[-CHd, 0, 0])

ms.xy_alignment(20, 21, 22, center=20)
ms.atoms += Atom('H', position=[0, 0, -CHd])

ms.xy_alignment(32, 33, 34, center=32)
ms.atoms += Atom('H', position=[0, 0, -CHd])

ms.xy_alignment(35, 0, 20)
write("capping.xyz", ms.atoms)
