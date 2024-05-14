from myutils.miscellaneous import output_terminal
import numpy as np
from glob import glob
from ase.io import read
import string
import sys



uppercase_letters = list(string.ascii_uppercase)


def extract_values(base='./', exclude=None):
    """This function extracts the information of the gvalues.
    
    Parameters
    ==========
    base: str
        relative path to the base directory that contains the systems.
    
    Return
    ======
    (np.ndarray) shape=[systems[N_systems],
                        method[cc-pVDZ,
                               cc-pVDZ i,
                               EPR II,
                               EPR II i],
                        gvalues[g-x, g-y, g-z]]
    """
    if exclude is None:
        exclude = []

    len_base = len(base)
    i = 1
    sys_counter = 0
    conf = []
    while True:
        systems = output_terminal(f'find {base} -mindepth 1 -maxdepth 1 -name {i}* -type d', print_output=False).split('\n')
        systems.pop(-1)
        if len(systems) == 0: break
        systems.sort()
        for system in systems:
            if system in exclude:
                continue
            print(f"{sys_counter} {system}")
            sys_counter += 1

            gval = []
            for method in [5, 7, 9, 11]:
                a = output_terminal(f'cd {base}; ' +
                                    'python analysis/create_tables.py' +
                                    f' {system[len_base:]}/ | grep "^g" |' +
                                    ' awk \'{' +f'print ${method}' +'}\'',
                                    print_output=False)
                
                gval.append(np.array(a.split(), dtype=float))
            conf.append(np.array(gval))

        i += 1

    return np.array(conf)

def extract_atoms(base='./'):
    """This function extracts the configuration information as an Atoms object
    from opt.xyz

    Parameters
    ==========
    base: str
        relative path to the base directory that contains the systems.

    Return
    ======
    (np.ndarray) shape=[systems[N_systems],
                        method[cc-pVDZ,
                               cc-pVDZ i,
                               EPR II,
                               EPR II i],
                        gvalues[g-x, g-y, g-z]]
    """
    len_base = len(base)
    i = 1
    sys_counter = 0
    conf = []
    while True:
        systems = glob(f'{base}/{i}*')
        if len(systems) == 0: break
        systems.sort()
        for system in systems:
            sys_counter += 1
            atoms = read(f'{system}/opt_EPRII.xyz')
            conf.append(atoms)
        i += 1

    return conf

def arrange_by_mass(confs, values, remove_last=0):
    """Function to organize the data in order of the number of carbon
    atoms in the system.

    Parameters
    ==========
    confs: list of ase.Atoms
        atoms of each configuration
    vales: array-like
        list of values associated with each configuration.
    
    Returns
    =======
    (array-like) values arranged in the order of mass of each system
    """
    masses = []
    for conf in confs:
        masses.append(int(conf.get_chemical_formula().split('C')[1].split('H')[0]))
    masses_sorted = list(set(masses[:-remove_last]))
    masses_sorted.sort()

    sorted_gvals = {}
    sorted_indexes = {}
    for i in masses_sorted:
        sorted_gvals[str(i)] = []
        sorted_indexes[str(i)] = []

    for i in range(len(masses)):
        try:
            sorted_gvals[str(masses[i])].append(values[i])
            sorted_indexes[str(masses[i])].append(i+1)
        except:
            continue