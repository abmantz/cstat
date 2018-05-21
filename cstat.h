#ifndef _CSTAT_
#define _CSTAT_

#include <math.h>

typedef double Real;
typedef unsigned long Natural;

inline Real cash_classic(const Real mu, const Natural x) {
  return 2.0 * (mu - x*log(mu));
}

Real cash_mod(const Real, const Natural);

void cash_mod_expectations(const Real, Real*, Real*);

#endif
