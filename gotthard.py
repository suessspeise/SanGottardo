import matplotlib.pyplot as plt
from numpy import genfromtxt, transpose
import pandas as pd

# elevation data from http://www.geocontext.org/publ/2010/04/profiler/en/
filename = 'gotthard.csv'
df = pd.read_csv(filename, delimiter=',')
elevation = transpose(genfromtxt(filename, delimiter=','))


# temperature profile from south to north
temp = [17.3, 27.0, 30.8, 27.2, 31.3, 31.8, 28.3, 36.3, 34.5, 30.1, 34.2, 39.6, 40.8, 35.9, 31.7, 32.0, 25.3, 19.4]
temp_ind = list(range(len(temp)))
temp_rev = temp[::-1] # inversion
# 3-point running mean (calculated with pen+paper)
smooth = [25.03, 28.33, 29.77, 30.1, 30.47, 32.13, 33.03, 33.63, 32.93, 34.63, 38.2, 38.77, 36.13, 33.20, 29.67, 27.63]
smooth_ind = list(range(len(smooth)+2))[1:-1]
smooth_rev = smooth[::-1] #inversion

# plots
plt.plot(temp_ind, temp_rev, color='red', label="Temperature")
plt.plot(smooth_ind, smooth_rev, color='red', linestyle=':', label="3-point running mean")
plt.plot(elevation[0]/1000,elevation[1]/50, label="Elevation")

# label
plt.xlabel('Distance from Southern entry')
plt.ylabel('T[°C]')
plt.legend()

plt.show()
