import numpy as np


#membaca file dengan numpy
path = "file_angka"
data = np.loadtxt(path, delimiter=',')
print("data :\n",data)

