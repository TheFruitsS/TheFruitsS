# 1D Interpolation
# The function interp1d() is used to interpolate a distribution with 1 variable.
#
# It takes x and y points and returns a callable function that can be called with new x and returns corresponding y.
#
# Example
# For given xs and ys interpolate values from 2.1, 2.2... to 2.9:

from scipy.interpolate import interp1d
import numpy as np

xs = np.arange(10)
ys = 2*xs + 1

interp_func = interp1d(xs, ys)

newarr = interp_func(np.arange(2.1, 3, 0.1))

print(newarr)