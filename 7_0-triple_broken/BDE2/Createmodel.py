from myutils.ase_utils.molecules import MoleculeSetter
from ase import Atom
from ase.io import read, write
import numpy as np


atoms = read("../../7_0-triple_broken//opt.xyz")

#side1 = [ i for i in range(86, 97)]
side2 = [ i for i in range(38, 49)]
all = np.array([2, 35] + side2)
for n in all[::-1]:
    atoms.pop(n - 1)

ms = MoleculeSetter(atoms)
CHd = atoms.get_distance(8, 6)
ms.xy_alignment(4, 1, center=4)
ms.atoms += Atom('H', position=[-CHd, 0, 0])

write("model.xyz", ms.atoms)
