from myutils.ase_utils.molecules import MoleculeSetter
from ase.io import read, write
from ase import Atom

molecule = read('reduced.pdb')
CHd = molecule.get_distance(20, 21)

ms = MoleculeSetter(molecule)

ms.xy_alignment(0, 1, center=0)

ms.atoms += Atom('H', position=[-CHd, 0, 0])

ms.xy_alignment(44, 2, center=44)
ms.atoms += Atom('H', position=[-CHd, 0, 0])

ms.xy_alignment(20, 14, 17, center=20)
ms.atoms += Atom('H', position=[-CHd, 0, 0])

ms.xy_alignment(41, 35, 38, center=41)
ms.atoms += Atom('H', position=[-CHd, 0, 0])

ms.xy_alignment(35, 0, 20)
write("capping.xyz", ms.atoms)
