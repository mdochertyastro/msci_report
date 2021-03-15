import numpy

datapath = './'
imgpath  = './' 

# load data
h1 = numpy.loadtxt(datapath + 'O3-H1-C01_CLEAN_SUB60HZ-1251752040.0_sensitivity_strain_asd.txt') # G1902351
l1 = numpy.loadtxt(datapath + 'O3-L1-C01_CLEAN_SUB60HZ-1240573680.0_sensitivity_strain_asd.txt') # G1902347
v1 = numpy.loadtxt(datapath + 'O3-V1_sensitivity_strain_asd.txt')

# compute BNS range
# from gwpy.frequencyseries import FrequencySeries
# from gwpy.astro import inspiral_range
# range_llo = inspiral_range(FrequencySeries(l1[:,1]**2, f0=l1[0,0], df=l1[1,0]-l1[0,0]), fmin=10, mass1=1.4, mass2=1.4).value
# range_lho = inspiral_range(FrequencySeries(h1[:,1]**2, f0=h1[0,0], df=h1[1,0]-h1[0,0]), fmin=10, mass1=1.4, mass2=1.4).value
# range_vir = inspiral_range(FrequencySeries(v1[:,1]**2, f0=v1[0,0], df=v1[1,0]-v1[0,0]), fmin=10, mass1=1.4, mass2=1.4).value

import matplotlib
matplotlib.use('agg')
# matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['font.size'] = 9
matplotlib.rcParams['savefig.dpi'] = 300
matplotlib.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'
matplotlib.rcParams['legend.fontsize'] = 9
from matplotlib import pyplot
pyplot.rc('axes', axisbelow=True)

colors = {'L1': '#4ba6ff', 'H1': '#ee0000', 'V1': '#9b59b6'}

fig = pyplot.figure(figsize=(5,4))
pyplot.loglog(h1[:,0], h1[:,1], label=r'$\mathrm{LIGO}\,\mathrm{Hanford}$', color=colors['H1'], linewidth=1, alpha=0.7)
pyplot.loglog(l1[:,0], l1[:,1], label=r'$\mathrm{LIGO}\,\mathrm{Livingston}$', color=colors['L1'], linewidth=1, alpha=0.7)
pyplot.loglog(v1[:,0], v1[:,1], label=r'$\mathrm{Virgo}$', color=colors['V1'], linewidth=1, alpha=0.7)

pyplot.legend(loc=(0.065, 0.73))

pyplot.xlabel(r'$\mathrm{Frequency}\,\mathrm{[Hz]}$')
pyplot.ylabel(r'$\mathrm{Strain}\,[1/\sqrt{\mathrm{Hz}}]$')
pyplot.xlim([10, 4000])
pyplot.ylim(1e-24, 1e-19)

pyplot.grid()
fig.tight_layout()
pyplot.savefig(imgpath + "o3a_strain.png")
