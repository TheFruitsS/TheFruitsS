import pandas as pd
import numpy as np
# x = 5 (value corresponding to 95%)
#   y = 17 (value corresponding to 102.5%)
# No I would like to calculate the value for xi which should correspond to 100%.
#
#  x = 5 (value corresponding to 95%)
#  xi = ?? (value corresponding to 100%)
#  y = 17 (value corresponding to 102.5%)
s = pd.Series([5, np.nan, 17], index=[95, 100, 102.5])
l = pd.Series([0.0337 , np.nan, 1610], index=[0.027,1470+1350+1640+1250/4 , 1250])
ls = l.interpolate(method='index')
x_new = s.interpolate(method='index')
print(l)