from myutils.ase_utils.molecules import MoleculeSetter
from ase import Atom
from ase.io import read, write
import numpy as np


atoms = read("../0_0-BeforeRupture/opt.xyz")

side1 = [ i for i in range(86, 97)]
side2 = [ i for i in range(37, 48)]
all = np.array([1, 34] + side2 + [50, 83] + side1)
for n in all[::-1]:
    atoms.pop(n - 1)

ms = MoleculeSetter(atoms)
CHd = atoms.get_distance(42, 38)
ms.xy_alignment(39, 36, center=39)
ms.atoms += Atom('H', position=[-CHd, 0, 0])
ms.xy_alignment(3, 0, center=3)
ms.atoms += Atom('H', position=[-CHd, 0, 0])

write("model.xyz", ms.atoms)
