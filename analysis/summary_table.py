from myutils.miscellaneous import output_terminal
import numpy as np
from glob import glob
import sys


experiment = np.array([2.00324, 2.00263, 2.00218])

structures = glob('../[123456789]*/')
structures.sort()
output = 'EPRII_i.out'

letters = 'ABCDEFGHIJKLMNOPQRST'
res = []
i_letter = 0
for structur in structures:
    out = output_terminal(f'grep -A 15 "ELECTRONIC G-MATRIX" {structur}' +
                          f'{output} | grep "g(tot)"',
                          print_output=False)
    values = np.sort(np.array(out.split()[1:4],dtype=float))[::-1]
    errors = experiment - values
    maxerror = np.max(errors)
    avr = np.mean(errors)
    values = np.append(values.astype('|S100'),
                       ["{:.7f}".format(round(maxerror, 7)),
                        "{:.7f}".format(round(avr, 7))])
    name = "\\text{" + letters[i_letter] + ") " + structur + "} "
    values = np.insert(values, 0, name)
    i_letter += 1
    res.append(values)

experiment = np.insert(experiment.astype(str), 0, "\\text{Experiment}")
experiment = np.append(experiment, ["", ""])
res.append(experiment)
#res = np.append(res, experiment, axis=1)

header = np.array(["", "g_x", "g_y", "g_z", "\\text{max abs error}", "\\text{avrg error}"])
table = np.insert(res, 0, header, axis=0)


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
