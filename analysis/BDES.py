from myutils.miscellaneous import output_terminal


# complet system
E_com = output_terminal("grep 'Total enthalpy' "
                        "../0_0-BeforeRupture/BDE/BDE.out | awk '{print $4}'")

# triple bond brocken
E_t12 = output_terminal("grep 'Total enthalpy' "
                        "../7_1-triple_broken_mult2/BDE/BDE.out | awk '{print $4}'")

print('BDE triple bond: ', 2 * float(E_t12) -  float(E_com))

# single
E_si1 = output_terminal("grep 'Total enthalpy' "
                        "../6_0-primary_in_triple/BDE/BDE.out | awk '{print $4}'")

# triple bond brocken
E_si2 = output_terminal("grep 'Total enthalpy' "
                        "../5_0-primary_in_ring/BDE/BDE.out | awk '{print $4}'")

print('BDE single bond: ', float(E_si1) + float(E_si2) - float(E_com))
