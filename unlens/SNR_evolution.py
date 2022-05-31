import h5py
import numpy as np
import matplotlib.pyplot as plt

inj = h5py.File('./injection.hdf')
snr = h5py.File('./snrs.hdf')

coa_phase = np.array(inj.get('coa_phase'))
dec = np.array(inj.get('dec'))
distance = np.array(inj.get('distance'))
inclination = np.array(inj.get('inclination'))
polarization = np.array(inj.get('polarization'))
ra = np.array(inj.get('ra'))
snrs = np.array(snr.get('snrs'))


fig, axes = plt.subplots(nrows=2, ncols=3, figsize=[9.5, 6], dpi=500)

ax5, ax6, ax7, ax8, ax9, ax10 = axes.flat

ax5.scatter(distance, snrs)
ax5.set_yscale('log')
ax5.set_xscale('log')

ax6.scatter(inclination, snrs)
ax6.set_yscale('log')

ax7.scatter(ra, snrs)
ax7.set_yscale('log')

ax8.scatter(dec, snrs)
ax8.set_yscale('log')

ax9.scatter(polarization, snrs)
ax9.set_yscale('log')

ax10.scatter(coa_phase, snrs)
ax10.set_yscale('log')

ax5.set_title('distance')
ax6.set_title('inclination')
ax7.set_title('ra')
ax8.set_title('dec')
ax9.set_title('polarization')
ax10.set_title('coa_phase')

plt.tight_layout()
plt.savefig('snr-evol-unlens.pdf')
