# %%
from myutils.plotters import StandardPlotter
from construct_variables import (extract_values,
                                 extract_atoms,
                                 uppercase_letters)
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl


fig, ax = plt.subplots(3,1)
sp = StandardPlotter(fig=fig, ax=ax, ax_pref={'sci_not':True})


yticks = [[2.0017, 2.0020, 2.0023],
          [2.0024, 2.0030, 2.0036],
          [2.0035, 2.0050, 2.0065]]

xyz_lab = ['x', 'y', 'z']

for i in [0, 1, 2]: #x, y, z
    # Add used values
    xlims = sp.ax[i].get_xlim()

    sp.axis_setter(ax=i,
                   ylabel='y-axis',
                   xlabel='x-axis',
                   xlim=xlims,
                   xticks=[],
                   yticks=yticks[i])

# Setting axis
#sp.ax[2].set_xticks(range(1, 5),
#                    uppercase_letters[:5])
sp.spaces[0].set_axis(axes=sp.ax, rows_cols=(3, 1),
                      borders=[[0.175, 0.16], [0.99, 0.91]],
                      spaces=[0.015, 0.015])
sp.show()

mpl.rcParams['font.size']
#sp.spaces[0].show_frame(majordelta=0.1, minordelta=0.025)
# %%