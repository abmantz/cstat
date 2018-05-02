import numpy as np
import matplotlib.pyplot as plt
plt.rc('text', usetex=True)

mean = np.loadtxt('test_data/fig1_mean.dat')
rms = np.loadtxt('test_data/fig1_rms.dat')

test = np.loadtxt('test.dat')

plt.plot(mean[:,0], mean[:,1], 'ro')
plt.plot(rms[:,0], rms[:,1], 'bo')
plt.plot(test[:,0], test[:,1], 'r-')
plt.plot(test[:,0], np.sqrt(test[:,2]), 'b-')
plt.xscale('log')
plt.xlabel(r'$\mu$')
plt.ylabel('Contribution per bin to Cstat')
plt.title('cash\_mod\_expectations')
plt.show()
