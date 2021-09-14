import cashstatistic as cstat
import numpy as np
import matplotlib.pyplot as plt
plt.rc('text', usetex=True)

mean = np.loadtxt('test_data/fig1_mean.dat')
rms = np.loadtxt('test_data/fig1_rms.dat')

mu = 10.0**np.arange(-7.0, 2.01, 0.01)
C_e, C_v = cstat.cash_mod_expectations(mu)

np.savetxt('test.dat', np.array([mu, C_e, C_v]).transpose())

plt.plot(mean[:,0], mean[:,1], 'ro')
plt.plot(rms[:,0], rms[:,1], 'bo')
plt.plot(mu, C_e, 'r-')
plt.plot(mu, np.sqrt(C_v), 'b-')
plt.xscale('log')
plt.xlabel(r'$\mu$')
plt.ylabel('Contribution per bin to Cstat')
plt.title('cash\_mod\_expectations')
plt.show()
