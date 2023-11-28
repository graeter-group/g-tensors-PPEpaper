from myutils.ase_utils.molecules import MoleculeSetter
from ase.io import read, write
from ase import Atom


molecule = read('../reduced/opt.xyz')
CHd = molecule.get_distance(0, 36)
ring=2.75/2

# H shift
ms = MoleculeSetter(molecule)
atoms2remove = [36, 12, 1, 0]
for atom in atoms2remove:
    ms.atoms.pop(atom)
ms.xy_alignment(1, 4, center=1)
ms.atoms += Atom('H', position=[-CHd, 0, 0])
ms.xy_alignment(4, 1, 2)

write("model.xyz", ms.atoms)
