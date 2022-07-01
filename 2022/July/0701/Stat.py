import numpy as np
import statistics
from scipy import stats
a= np.random.randint(1,40,1000)
mode = stats.mode(a)
print("mode",mode[0].item())
print("count", mode[0].item())

median = statistics.median(a)
print("median", median)


