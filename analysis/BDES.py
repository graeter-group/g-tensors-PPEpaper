from myutils.miscellaneous import output_terminal
import sys


kind = int(sys.argv[1]) # 1 or 2
sw = sys.argv[2] # orga or g09

if kind == 1:
    whole = '0_0-BeforeRupture'
    num = ''
elif kind == 2:
    whole = '0_1-BeforeRupture_wo_extRings'
    num = '2'

if sw == 'orca':
    keyword = "Total enthalpy"
    awk = "awk '{print $4}'"
    sw = ''
    output = 'BDE.out'
elif sw == 'g09':
    keyword = "Enthalpies"
    awk = "awk '{print $7}'"
    output = 'g09BDE.log'
else:
    raise ValueError("Not recognized software")

# complet system
E_com = output_terminal(f"grep '{keyword}' "
                        f"../{whole}/BDE{num}{sw}/{output}"
                        f" | {awk}",
                        print_output=False)

# triple bond brocken
E_t12 = output_terminal(f"grep '{keyword}' "
                        f"../7_0-triple_broken/BDE{num}{sw}/{output}"
                        f" | {awk}",
                        print_output=False)

deltaE = 2 * float(E_t12) -  float(E_com)
print('BDE triple bond: ', deltaE, " Ha / ", deltaE * 2600,  " kJ/mol")

# single
E_si1 = output_terminal(f"grep '{keyword}' "
                        f"../6_0-primary_in_triple/BDE{num}{sw}/{output}"
                        f" | {awk}",
                        print_output=False)

# triple bond brocken
E_si2 = output_terminal(f"grep '{keyword}' "
                        f"../5_0-primary_in_ring/BDE{num}{sw}/{output}"
                        f" | {awk}",
                        print_output=False)

deltaE = float(E_si1) + float(E_si2) - float(E_com)
print('BDE single bond: ', deltaE, " Ha / ", deltaE * 2600,  " kJ/mol")
