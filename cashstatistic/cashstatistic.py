import numpy as np

def cash_classic(mu, x):
  """
Inputs:
  mu: Mean parameter of the Poisson distribution
  x:  Observed counts
Output:
  Cash statistic = 2.0 * (mu - x*ln(mu))
  """
  return 2.0 * (mu - x*np.log(mu))

def cash_mod(mu, x):
  """
Inputs:
  mu: Mean parameter of the Poisson distribution
  x:  Observed counts
Output:
  Modified Cash statistic = 2.0 * (mu - x + x*ln(x/mu))
  """
  if x == 0:
    return 2.0 * mu
  return 2.0 * (mu - x + x*np.log(x/mu))

ln2 = np.log(2.0)
ln3 = np.log(3.0)
ln4 = np.log(4.0)
def _cash_mod_Sv(mu, lnmu):
  mu2 = mu**2
  return 4.0 * np.exp(-mu) * ( mu2 + mu * (mu - (1.0 + lnmu))**2 + 0.5*mu2 * (mu - 2.0*(1.0 + lnmu - ln2))**2 + mu*mu2/6.0 * (mu - 3.0*(1.0 + lnmu - ln3))**2 + mu2*mu2/24.0 * (4.0*(1.0 + lnmu - ln4))**2 )

def cash_mod_expectations(mu_in):
  """
Input:
  mu_in: Mean parameter of the Poisson distribution (can be a numpy array)
Output: a tuple containing
  C_e = theoretical mean of the modified Cash statistic
  C_e = theoretical variance of the modified Cash statistic
  Each of these is an approximations to an infinite series, with relative accuracy ~1e-4.
  See Kaastra (2017), specifically eqns 8-22.
  http://adsabs.harvard.edu/abs/2017A%26A...605A..51K
  """
  mu = np.asarray(mu_in)
  lnmu = np.log(mu)
  mi = 1.0/mu
  C_e = np.empty(mu.shape)
  C_v = np.empty(mu.shape)
  C_e[mu < 0.0] = np.nan
  j = np.all([mu >= 0.0, mu <= 0.5], axis=0)
  C_e[j] = ((-0.25*mu[j] + 1.38)*mu[j] -2.0*lnmu[j])*mu[j]
  j = np.all([mu > 0.5, mu <= 2.0], axis=0)
  C_e[j] = ((((-0.00335*mu[j] + 0.04259)*mu[j] - 0.27331)*mu[j] + 1.381)*mu[j] -2.0*lnmu[j])*mu[j]
  j = np.all([mu > 2.0, mu <= 5.0], axis=0)
  C_e[j] = 1.019275 + 0.1345*mu[j]**(0.461 - 0.9*lnmu[j])
  j = np.all([mu > 5.0, mu <= 10.0], axis=0)
  C_e[j] = 1.00624 + 0.604*mu[j]**-1.68
  j = (mu >= 10.0)
  C_e[j] = 1.0 + (0.1649 + 0.226*mi[j])*mi[j]
  C_v[mu < 0.0] = np.nan
  j = np.all([mu >= 0.0, mu <= 0.1], axis=0)
  C_v[j] = _cash_mod_Sv(mu[j], lnmu[j]) - C_e[j]**2
  j = np.all([mu > 0.1, mu <= 0.2], axis=0)
  C_v[j] = (((-262.0*mu[j] + 195.0)*mu[j] - 51.24)*mu[j] + 4.34)*mu[j] + 0.77055
  j = np.all([mu > 0.2, mu <= 0.3], axis=0)
  C_v[j] = (4.23*mu[j] - 2.8254)*mu[j] + 1.12522
  j = np.all([mu > 0.3, mu <= 0.5], axis=0)
  C_v[j] = ((-3.7*mu[j] + 7.328)*mu[j] - 3.6926)*mu[j] + 1.20641
  j = np.all([mu > 0.5, mu <= 1.0], axis=0)
  C_v[j] = (((1.28*mu[j] - 5.19)*mu[j] + 7.666)*mu[j] -3.5446)*mu[j] + 1.15431
  j = np.all([mu > 1.0, mu <= 2.0], axis=0)
  C_v[j] = (((0.1125*mu[j] - 0.641)*mu[j] + 0.859)*mu[j] + 1.0914)*mu[j] - 0.05748
  j = np.all([mu > 2.0, mu <= 3.0], axis=0)
  C_v[j] = ((0.089*mu[j] - 0.872)*mu[j] + 2.8422)*mu[j] - 0.67539
  j = np.all([mu > 3.0, mu <= 5.0], axis=0)
  C_v[j] = 2.12336 + 0.012202*mu[j]**(5.717 - 2.6*lnmu[j])
  j = np.all([mu > 5.0, mu <= 10.0], axis=0)
  C_v[j] = 2.05159 + 0.331*mu[j]**(1.343 - lnmu[j])
  j = (mu > 10.0)
  C_v[j] = ((12.0*mi[j] + 0.79)*mi[j] + 0.6747)*mi[j] + 2.0
  return C_e, C_v
