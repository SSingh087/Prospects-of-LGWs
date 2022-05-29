import h5py
import numpy as np
import matplotlib.pyplot as plt

inj = h5py.File('./unlens/injection.hdf')
un_snr = h5py.File('./unlens/snrs.hdf')
snr = h5py.File('./lens/snrs.hdf')

coa_phase = np.array(inj.get('coa_phase'))
dec = np.array(inj.get('dec'))
distance = np.array(inj.get('distance'))
inclination = np.array(inj.get('inclination'))
polarization = np.array(inj.get('polarization'))
ra = np.array(inj.get('ra'))
snrs = np.array(snr.get('snrs'))
snrs1 = np.array(snr.get('snrs1'))
snrs2 = np.array(snr.get('snrs2'))
unsnrs = np.array(un_snr.get('snrs'))

fig, axes = plt.subplots(nrows=2, ncols=3, figsize=[9.5, 6], dpi=500)

ax5, ax6, ax7, ax8, ax9, ax10 = axes.flat

ax5.scatter(distance, unsnrs)
ax5.scatter(distance, snrs)
ax5.scatter(distance, snrs1)
ax5.scatter(distance, snrs2)
ax5.set_yscale('log')
ax5.set_xscale('log')

ax6.scatter(inclination, unsnrs)
ax6.scatter(inclination, snrs)
ax6.scatter(inclination, snrs1)
ax6.scatter(inclination, snrs2)
ax6.set_yscale('log')

ax7.scatter(ra, unsnrs)
ax7.scatter(ra, snrs)
ax7.scatter(ra, snrs1)
ax7.scatter(ra, snrs2)
ax7.set_yscale('log')

ax8.scatter(dec, unsnrs)
ax8.scatter(dec, snrs)
ax8.scatter(dec, snrs1)
ax8.scatter(dec, snrs2)
ax8.set_yscale('log')

ax9.scatter(polarization, unsnrs)
ax9.scatter(polarization, snrs)
ax9.scatter(polarization, snrs1)
ax9.scatter(polarization, snrs2)
ax9.set_yscale('log')

ax10.scatter(coa_phase, unsnrs)
ax10.scatter(coa_phase, snrs)
ax10.scatter(coa_phase, snrs1)
ax10.scatter(coa_phase, snrs2)
ax10.set_yscale('log')

ax5.set_title('distance')
ax6.set_title('inclination')
ax7.set_title('ra')
ax8.set_title('dec')
ax9.set_title('polarization')
ax10.set_title('coa_phase')

plt.tight_layout()
plt.savefig('snr-evol-lens.pdf')