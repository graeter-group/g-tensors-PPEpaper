from myutils.miscellaneous import output_terminal
import sys

subdir = sys.argv[1]

# complet system
E_com = output_terminal("grep 'Total enthalpy' "
                        f"../0_0-BeforeRupture/{subdir}/BDE.out" + " | awk '{print $4}'", print_output=False)

# triple bond brocken
E_t12 = output_terminal("grep 'Total enthalpy' "
                        f"../7_0-triple_broken/{subdir}/BDE.out" + " | awk '{print $4}'", print_output=False)

deltaE = 2 * float(E_t12) -  float(E_com)
print('BDE triple bond: ', deltaE, " Ha / ", deltaE * 2600,  " kJ/mol")

# single
E_si1 = output_terminal("grep 'Total enthalpy' "
                        f"../6_0-primary_in_triple/{subdir}/BDE.out" + " | awk '{print $4}'", print_output=False)

# triple bond brocken
E_si2 = output_terminal("grep 'Total enthalpy' "
                        f"../5_0-primary_in_ring/{subdir}/BDE.out" + " | awk '{print $4}'", print_output=False)

deltaE = float(E_si1) + float(E_si2) - float(E_com)
print('BDE single bond: ', deltaE, " Ha / ", deltaE * 2600,  " kJ/mol")
