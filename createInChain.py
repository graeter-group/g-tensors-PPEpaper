from myutils.sith.visualization import MoleculeViewer
from myutils.ase_utils.molecules import MoleculeSetter
from ase.io import read, write
from ase import Atom


atoms = read('./left/opt.xyz')
cc_dist = atoms.get_distance(34, 37)
atoms.pop(35)
ms = MoleculeSetter(atoms)
ms.xy_alignment(2, 34, 7, center=34)
new_phenyl = atoms[37: 48].copy()
ms.xy_alignment(1, 0, 8, center=0)
ms.atoms += new_phenyl
ms.xy_alignment(3, 6)
write("./inchain/chain.xyz", ms.atoms)