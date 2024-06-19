from myutils.miscellaneous import output_terminal
import numpy as np
import sys


experiment = np.array([2.00324, 2.00263, 2.00218])

methods = ['cc-pVDZ.out', 'cc-pVDZ_i.out', 'EPRII.out', 'EPRII_i.out' ]
res = []
for method in methods:
    out = output_terminal(f'grep -A 15 "ELECTRONIC G-MATRIX" {sys.argv[1]}' +
                          f'{method} | grep "g(tot)"',
                          print_output=False)
    values = np.sort(np.array(out.split()[1:4],dtype=float))[::-1]
    errors = experiment - values
    maxerror = np.max(errors)
    avr = np.mean(errors)
    values = np.append(values.astype(str),
                       ["{:.7f}".format(round(maxerror, 7)),
                        "{:.7f}".format(round(avr, 7))])
    res.append(values)

res = np.array(res).T

header = np.array(["", "\\text{experiments}", "\\text{cc-pVDZ}",
                   "\\text{cc-pVDZ i}", "\\text{EPR II}", "\\text{EPR II i}"])
rows_labels = ["g_x", "g_y", "g_z", "\\text{max absolute error}",
               "\\text{average error}"]

table = np.insert(res, 0, np.append(experiment.astype(str), ["", ""]),
                  axis=1)
table = np.insert(table, 0, rows_labels, axis=1)
table = np.insert(table, 0, header, axis=0)


def create_table(data_rows):
    # Calculate column widths
    column_widths = [max(len(str(item)) for item in col) for col in zip(*data_rows)]

    # Print the header
    header = [f"{col:{width}}" for col, width in zip(data_rows[0], column_widths)]
    print(" & ".join(header), " \\\\ \hline")

    # Print the data rows
    for row in data_rows[1:]:
        row_data = [f"{col:{width}}" for col, width in zip(row, column_widths)]
        print(" & ".join(row_data), " \\\\ \hline")

create_table(table)