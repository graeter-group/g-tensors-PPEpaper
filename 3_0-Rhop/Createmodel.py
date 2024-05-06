from myutils.ase_utils.molecules import MoleculeSetter
from ase.io import read, write


molecule = read('../reduced/opt.xyz')
CHd = molecule.get_distance(0, 36)
ring=2.75/2

# RadHop
ms = MoleculeSetter(molecule)
ms.atoms.pop(12)
ms.xy_alignment(6, 3, 4)

write("model.xyz", ms.atoms)
