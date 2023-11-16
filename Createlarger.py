from myutils.sith.visualization import MoleculeViewer
from myutils.ase_utils.molecules import MoleculeSetter
from ase.io import read, write
from ase import Atom, Atoms
import numpy as np


atoms = read('./left/opt.xyz')
cc_dist = atoms.get_distance(34, 37)
atoms.pop(35)
ms = MoleculeSetter(atoms)
ms.xy_alignment(2, 34, 7, center=34)
new_phenyl = atoms[37: 48].copy()
ms.xy_alignment(1, 0, 8, center=0)
ms.atoms += new_phenyl
ms.xy_alignment(40, 37)

dlong = atoms.get_distance(2,6)
dshort = atoms.get_distance(2, 34)

# One side
ms.apply_trans(np.identity(3), shift=-ms.atoms[51].position)
ms.apply_trans(np.identity(3), indexes=[54], shift=[dlong+dshort, 0, 0])
ms.atoms += Atoms('CC', [[dlong, 0, 0],
                         [dlong+dshort, 0, 0]])

#the other side
ms.apply_trans(np.identity(3), shift=-ms.atoms[40].position)
ms.apply_trans(np.identity(3), indexes=[43], shift=[-(dlong+dshort), 0, 0])
ms.atoms += Atoms('CC', [[-dlong, 0, 0],
                         [-(dlong+dshort), 0, 0]])


write("larger/larger.xyz", ms.atoms)