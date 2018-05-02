# cstat
Notes on the C version:

The Makefile should (hopefully) be able to produce
* A compiled object file, `cstat.o`
* An archive containing that compiled code, `cstat.a`
* A PNG graphic comparing the calculated values of the mean and variance of C_m to Fig. 1 of [Kaastra (2017)](http://adsabs.harvard.edu/abs/2017A%26A...605A..51K), `test.png`. Making the graphic requires the [`R`](https://www.r-project.org/) computing environment to be installed on your system, but you can also compile and run the `testexe` program and compare its output to the data stored in `test_data/` manually.
