import h5py
import numpy as np
import matplotlib.pyplot as plt

inj = h5py.File('./injection.hdf')
snrCE = h5py.File('./CE/snrs.hdf')
snrET = h5py.File('./ET/snrs.hdf')
snrET_CE = h5py.File('./ET_CE/snrs.hdf')
snrALL = h5py.File('./ALL/snrs.hdf')
snrHLVKI = h5py.File('./HLVKI/snrs.hdf')

coa_phase = np.array(inj.get('coa_phase'))
dec = np.array(inj.get('dec'))
distance = np.array(inj.get('distance'))
inclination = np.array(inj.get('inclination'))
polarization = np.array(inj.get('polarization'))
ra = np.array(inj.get('ra'))
snrsCE = np.array(snrCE.get('snrs'))
snrCE = np.array(snrCE .get('snrs'))
snrET = np.array(snrET .get('snrs'))
snrET_CE =np.array(snrET_CE.get('snrs'))
snrALL =np.array(snrALL.get('snrs'))
snrHLVKI =np.array(snrHLVKI.get('snrs'))


fig, axes = plt.subplots(nrows=2, ncols=3, figsize=[10, 8], dpi=300)

ax5, ax6, ax7, ax8, ax9, ax10 = axes.flat

a=ax5.scatter(distance, snrCE, s=0.1)
b=ax5.scatter(distance, snrET, s=0.1)
c=ax5.scatter(distance, snrET_CE, s=0.1)
d=ax5.scatter(distance, snrALL, s=0.1)
e=ax5.scatter(distance, snrHLVKI, s=0.1)
ax5.set_yscale('log')
ax5.set_xscale('log')


ax6.scatter(inclination, snrCE, s=0.1)
ax6.scatter(inclination, snrET, s=0.1)
ax6.scatter(inclination, snrET_CE, s=0.1)
ax6.scatter(inclination, snrALL, s=0.1)
ax6.scatter(inclination, snrHLVKI, s=0.1)
ax6.set_yscale('log')

ax7.scatter(ra, snrCE, s=0.1)
ax7.scatter(ra, snrET, s=0.1)
ax7.scatter(ra, snrET_CE, s=0.1)
ax7.scatter(ra, snrALL, s=0.1)
ax7.scatter(ra, snrHLVKI, s=0.1)
ax7.set_yscale('log')

ax8.scatter(dec, snrCE, s=0.1)
ax8.scatter(dec, snrET, s=0.1)
ax8.scatter(dec, snrET_CE, s=0.1)
ax8.scatter(dec, snrALL, s=0.1)
ax8.scatter(dec, snrHLVKI, s=0.1)
ax8.set_yscale('log')

ax9.scatter(polarization, snrCE, s=0.1)
ax9.scatter(polarization, snrET, s=0.1)
ax9.scatter(polarization, snrET_CE, s=0.1)
ax9.scatter(polarization, snrALL, s=0.1)
ax9.scatter(polarization, snrHLVKI, s=0.1)
ax9.set_yscale('log')

ax10.scatter(coa_phase, snrCE, s=0.1)
ax10.scatter(coa_phase, snrET, s=0.1)
ax10.scatter(coa_phase, snrET_CE, s=0.1)
ax10.scatter(coa_phase, snrALL, s=0.1)
ax10.scatter(coa_phase, snrHLVKI, s=0.1)
ax10.set_yscale('log')

ax5.set_title('distance')
ax6.set_title('inclination')
ax7.set_title('ra')
ax8.set_title('dec')
ax9.set_title('polarization')
ax10.set_title('coa_phase')


lgnd = plt.legend([a,b,c,d,e],["CE","ET","2CE+ET","ALL","HLVKI"], ncol=5)
lgnd.legendHandles[0]._sizes = [30]
lgnd.legendHandles[1]._sizes = [30]
lgnd.legendHandles[2]._sizes = [30]
lgnd.legendHandles[3]._sizes = [30]
lgnd.legendHandles[4]._sizes = [30]

plt.tight_layout()
plt.savefig('snr-evol-unlens.pdf')
