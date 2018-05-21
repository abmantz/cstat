#include "cstat.h"

Real cash_mod(const Real mu, const Natural x) {
  if (x == 0) return 2.0 * mu;
  return 2.0 * (mu - x + x*log(x/mu));
}

// See Kaastra (2017) for functions below, specifically eqns 8-22.
// http://adsabs.harvard.edu/abs/2017A%26A...605A..51K

Real cash_mod_Sv(const Real mu, const Real lnmu) {
  const Real ln2 = log(2.0),
             ln3 = log(3.0),
             ln4 = log(4.0);
  Real mu2 = mu*mu;
  Real s, x;
  s = mu2;
  x = mu - (1.0 + lnmu);
  s += mu * x*x;
  x = mu - 2.0*(1.0 + lnmu - ln2);
  s += 0.5*mu2 * x*x;
  x = mu - 3.0*(1.0 + lnmu - ln3);
  s += mu*mu2/6.0 * x*x;
  x = mu - 4.0*(1.0 + lnmu - ln4);
  s += mu2*mu2/24.0 * x*x;
  return 4.0 * exp(-mu) * s;
}

// C_e is the expectation value of the "cash_mod" statistic for a given model mean.
// C_v is its theoretical variance.
// Both of these are approximations to an infinite series, with relative accuracy ~1e-4
// according to the Kaastra paper.
void cash_mod_expectations(const Real mu, Real *C_e, Real *C_v) {
  Real lnmu = log(mu);
  (*C_e) = NAN;
  (*C_v) = NAN;
  if (mu >= 0.0 && mu <= 0.5) {
    (*C_e) = ((-0.25*mu + 1.38)*mu -2.0*lnmu)*mu;
    if (mu <= 0.1) {
      (*C_v) = cash_mod_Sv(mu, lnmu) - (*C_e)*(*C_e);
    } else if (mu <= 0.2) {
      (*C_v) = (((-262.0*mu + 195.0)*mu - 51.24)*mu + 4.34)*mu + 0.77055;
    } else if (mu <= 0.3) {
      (*C_v) = (4.23*mu - 2.8254)*mu + 1.12522;
    } else {
      (*C_v) = ((-3.7*mu + 7.328)*mu - 3.6926)*mu + 1.20641;
    }
  } else if (mu <= 2.0) {
    (*C_e) = ((((-0.00335*mu + 0.04259)*mu - 0.27331)*mu + 1.381)*mu -2.0*lnmu)*mu;
    if (mu <= 1.0) {
      (*C_v) = (((1.28*mu - 5.19)*mu + 7.666)*mu -3.5446)*mu + 1.15431;
    } else {
      (*C_v) = (((0.1125*mu - 0.641)*mu + 0.859)*mu + 1.0914)*mu - 0.05748;
    }
  } else if (mu <= 5.0) {
    (*C_e) = 1.019275 + 0.1345*pow(mu, 0.461 - 0.9*lnmu);
    if (mu <= 3.0) {
      (*C_v) = ((0.089*mu - 0.872)*mu + 2.8422)*mu - 0.67539;
    } else {
      (*C_v) = 2.12336 + 0.012202*pow(mu, 5.717 - 2.6*lnmu);
    }
  } else if (mu <= 10.0) {
    (*C_e) = 1.00624 + 0.604*pow(mu, -1.68);
    (*C_v) = 2.05159 + 0.331*pow(mu, 1.343 - lnmu);
  } else {
    double mi = 1.0/mu;
    (*C_e) = 1.0 + (0.1649 + 0.226*mi)*mi;
    (*C_v) = ((12.0*mi + 0.79)*mi + 0.6747)*mi + 2.0;
  }
}
