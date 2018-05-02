.. image:: https://img.shields.io/pypi/v/cashstatistic.svg
   :alt: PyPi
   :target: https://pypi.python.org/pypi/cashstatistic
.. image:: https://img.shields.io/pypi/l/cashstatistic.svg
   :alt: MIT
   :target: https://mit-license.org/license.txt
===============
cashstatistic
===============
**Utility functions related to the Cash statistic**


The Poisson distribution is

P(x|mu) = exp(-mu) mu^x / x!

The `Cash statistic <http://adsabs.harvard.edu/abs/1979ApJ...228..939C>`_ is defined to be the model (mu) dependent part of -2ln(P), analogous to the role that chi^2 plays for the Gaussian distribution,

C = 2( mu - x\*ln(mu) ).

A modified version,

C_m = 2( mu - x + x\*ln(x/mu) ),

is equivalent to C for parameter inference (i.e. has the same dependence on mu), and also has the nice property of becoming equivalent to chi^2 when x is large. `Kaastra (2017) <http://adsabs.harvard.edu/abs/2017A%26A...605A..51K>`_ was kind enough to provide approximate expressions for the mean and variance of C_m, which can be used to determine whether the actual C_m corresponding to a fitted model is indicative of a good fit (just as chi^2 does for the Gaussian distribution).

This package contains python code to calculate C, C_m, and the theoretical mean and variance of C_m. The `GitHub repo <https://github.com/abmantz/cstat>`_ contains implementations in other languages.
