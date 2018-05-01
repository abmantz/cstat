#include "cstat.h"
#include <math.h>
#include <stdio.h>

int main(int argc, char **argv) {
  double mu, C_e, C_v;

  printf("# %g %g\n", cash_classic(0.5, 1), cash_mod(0.5, 1));
  
  for (int i=0; i<=900; ++i) {
    mu = pow(10.0, 0.01*i - 7.0);
    cash_mod_expectations(mu, &C_e, &C_v);
    printf("%g %g %g\n", mu, C_e, C_v);
  }

  return 0;
}
