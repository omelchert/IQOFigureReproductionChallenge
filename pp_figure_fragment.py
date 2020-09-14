"""
Module file containing functions that allow to reproduce FIG. 1 of the article

    Experimental Observation of Picosecond Pulse Narrowing and Solitons in Optical Fibers
    L. F. Mollenauer, R. H. Stolen, and J. P. Gordon
    Phys. Rev. Lett. 45, 1095 (1980)

This module was prepared as a part of the scientific short course

  A brief guide to publication-ready scientific figures using Python's matplotlib

held during the 2020 seminar week of the Ultrafast Laser Laboratory
at Institute of Quantum Optics at Leibniz University Hannover.

Author: O. Melchert
Date: 2020-09-12
"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

__author__ = 'Oliver Melchert'
__date__ = '2020-09-12'


def fetch_data(path):
    """fetch data

    Reads in data from file in numpy npz-format

    Args:
      path (str): path to npz-file

    Returns: (z, t, Azt, N)
      z (1D array): z samples
      t (1D array): t samples
      Azt (2D array): complex-valued field A(z,t)
      N (float): soliton order
    """
    dat = np.load(path)
    return dat['z'], dat['t'], dat['Azt'], dat['N']


def set_style():
    """set figure style

    Function that customizes the default style to be conform with the Physical
    Review style and notation guide [1]. For instructions on how to set the
    default style using style sheets see [2].

    Notes:
    - main font size is chosen as 8pt, matching the fontsize of figure captions
    - fontsize of legends and auxiliary text labels are set to 6pt, exceeding
      the minimally required pointsize of 4.25 pt. (1.5 mm)
    - default rc (rc = "run commands", i.e. startup information) settings are
      changed dynamically
    - the custom font-scheme 'type2' depends on your latex installation and
      is not guaranteed to run on your specific system

    Refs:
      [1] https://journals.aps.org/prl/authors
      [2] https://matplotlib.org/3.3.1/tutorials/introductory/customizing.html
    """

    fig_width_1col = 3.4        # figure width in inch
    fig_width_2col = 7.0        # figure width in inch
    fig_aspect_ratio = 1.       # width to height aspect ratio
    font_size = 8               # font size in pt
    font_size_small = 6         # font size in pt
    font_scheme = None          # options: 
                                #   None    - default matplotlib fonts
                                #   'type1' - text: Helvetica, math: Computer modern
                                #   'type2' - text: Helvetica, math: Helvetica 

    mpl.rcParams['figure.figsize'] = fig_width_1col, fig_aspect_ratio*fig_width_1col
    mpl.rcParams['axes.labelsize'] = font_size
    mpl.rcParams['font.size'] = font_size
    mpl.rcParams['legend.fontsize'] = font_size_small
    mpl.rcParams['xtick.labelsize'] = font_size
    mpl.rcParams['ytick.labelsize'] = font_size
    mpl.rcParams['xtick.direction'] = 'out'
    mpl.rcParams['ytick.direction'] = 'out'
    mpl.rcParams['lines.linewidth'] = 1.0
    mpl.rcParams['axes.linewidth'] =  0.5

    if font_scheme == 'type1':
        mpl.rcParams['text.usetex'] = True
        mpl.rcParams['font.family'] = 'sans-serif'
        mpl.rcParams['font.sans-serif'] = 'Helvetica'
        mpl.rcParams['mathtext.fontset'] = 'cm'

    if font_scheme == 'type2':
        mpl.rcParams['text.usetex'] = True
        mpl.rcParams['text.latex.preamble'] = [
           r'\usepackage{siunitx}',
           r'\sisetup{detect-all}',
           r'\usepackage{helvet}',
           r'\usepackage{sansmath}',
           r'\sansmath'
        ]


def set_legend(ax, lines):
    """set legend

    Function generating a custom legend, see [1] for more options

    Refs:
      [1] https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.legend.html

    Args:
      ax (object): figure part for which the legend is intended
      lines (list): list of  Line2D objects
    """
    # -- extract labels from lines
    labels = [x.get_label() for x in lines]
    # -- customize legend 
    ax.legend(lines,                # list of Line2D objects
              labels,               # labels 
              title = '',           # title shown on top of legend 
              loc = 0,              # location of the legend
              ncol = 1,             # number of columns
              labelspacing = 0.3,   # vertical space between handles in font-size units
              borderpad = 0.3,      # distance to legend border in font-size units
              handletextpad = 0.6,  # distance between handle and label in font-size units
              handlelength = 2.0,   # length of handle in font-size units
              frameon = False       # remove background patch
              )


def save_figure(fig_format = None, fig_name = 'test'):
    """ save figure

    Function that saves figure or shows interactive plot

    Note:
    - if no valid option is provided, an interactive plot is shown

    Args:
      fig_format (str): format to save figure in (options: png, pdf, svg)
      fig_name (str): name for figure (default: 'test')
    """
    if fig_format == 'png':
        plt.savefig(fig_name+'.png', format='png', dpi=600)
    elif fig_format == 'pdf':
        plt.savefig(fig_name+'.pdf', format='pdf', dpi=600)
    elif fig_format == 'svg':
        plt.savefig(fig_name+'.svg', format='svg')
    else:
        plt.show()


def generate_figure(data_set_01, data_set_02, fig_format=None, fig_name='fig01'):
    """generate figure

    Function generating a figure reproducing FIG. 3 of [1].

    Refs:
      [1] Experimental Observation of Picosecond Pulse Narrowing and Solitons in Optical Fibers
          L. F. Mollenauer, R. H. Stolen, and J. P. Gordon
          Phys. Rev. Lett. 45, 1095 (1980)

    Args:
      data_set_01 (tuple): data set of the form (z, t, Azt, N), where
                              z (1D array): z samples
                              t (1D array): t samples
                              Azt (2D array): complex-valued field A(z,t)
                              N (float): soliton order
      data_set_02 (tuple): data set of the form (z, t, Azt, N)
      fig_format (str): format for output figure
                        (choices: png, pdf, svg; default: interactive figure)
      fig_name (str): name for output figure wihtout suffix (default='fig01')
    """

    # (1) SET A STYLE THAT FITS THE TARGET JOURNAL
    set_style()

    # (2) SET FIGURE LAYOUT
    fig = plt.figure()
    plt.subplots_adjust(left = 0.13, bottom = 0.11,
                        right = 0.97, top = 0.98,
                        wspace = 0.05, hspace = 0.4)
    # -- 3x3 grid on which subplots can be arranged 
    gs00 = GridSpec(nrows = 3, ncols = 3)
    # -- generate axes for all subplots
    ax01 = fig.add_subplot(gs00[1:3,0])
    ax11 = fig.add_subplot(gs00[0,0])


    # SUBFIGURE A ###########################################################

    # (3) SET AXES CONTENT
    # NOTE: notation chosen so that z = xi, t = s
    z, t, Azt, N = data_set_01
    _Pz = lambda z0: np.abs(Azt[np.argmin(np.abs(z-z0))])**2

    z0=0.
    P0 = np.max(_Pz(z0))/N/N
    l1 = ax11.plot(t, _Pz(z0)/P0, color='black', lw=1., label=r'$\xi = 0$')

    # (4) SET AXIS DETAILS
    ax11.set_xlim((-3,3))
    ax11.set_xticks((-2,0,2))
    ax11.tick_params(axis='x', direction='out', length=3.5, pad=2, top=False)
    ax11.set_ylim((0,20))
    ax11.set_yticks((0,10,20))
    ax11.tick_params(axis='y', direction='out', length=3.5, pad=2, right=False)




    # (6) SAVE FIGURE
    save_figure(fig_format, fig_name)


def main():
    data_set_01 = fetch_data('NSE_N2.npz')
    data_set_02 = fetch_data('NSE_N3.npz')
    generate_figure(data_set_01, data_set_02, fig_format='png', fig_name='figure_fragment')


if __name__ == '__main__':
    main()
