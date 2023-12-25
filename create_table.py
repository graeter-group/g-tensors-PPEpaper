from myutils.miscellaneous import output_terminal

out = output_terminal('grep -A 15 "ELECTRONIC G-MATRIX" Rhop/g-tensor_EPRII.out  | grep "g(tot)"', 
                      print_output=False)

print(out)