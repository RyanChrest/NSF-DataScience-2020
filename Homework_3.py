# Amortorization schedule calculator

import numpy_financial as npf
import numpy as np
# Amoritization Schedule
principal = 2_500
years = 1
rate = 0.0824
per = np.arange(years * 12) + 1
ipmt = npf.ipmt(rate/12, per, years*12, principal)
ppmt = npf.ppmt(rate/12, per, years*12, principal)
pmt = npf.pmt(rate/12, per, years*12, principal)

fmt = '{0:2d} {1:8.2f} {2:8.2f} {3:8.2f}' # formatting
for payment in per:
    index = payment - 1
    principal = principal + ppmt[index]
    print(fmt.format(payment, ppmt[index], ipmt[index], principal))
