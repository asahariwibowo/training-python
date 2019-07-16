import numpy as np
#definiskan array pada numpy

array1D = np.array([1,2,3,4,5,6])
print("nilai array1D:\n",array1D)

array2D = np.array([[1,2,3],[4,5,6]])
print("array2D\n ",array2D)

matrix = np.matrix([[1,2,3],[4,5,6]])
print("matrix\n ",matrix)

arrayND = np.array([[[1,1,1],[2,2,2]],[[3,3,3],[4,4,4]],[[5,5,5],[6,6,6]]])
print("martixND\n",arrayND)

np1 = np.full((2,3),5)
print("np1\n",np1)

#melihat deskripsi dari data array: bentuk (size), min, max, std, var
print("ukuran dari array 2D:", array2D.shape[1])
print("ukuran dari arrayND:", arrayND.shape)
print("ukuran min", array2D.min())
print("standar deviasi", array2D.std())

#indexing dari array numpy
print("array2D:\n",array2D)
print("indexing :", array2D[0,1:3])
print("indexing :", array2D[0,:])

#mencoba operasi sederhana
matrix2 = np.matrix([[3,6,7],[8,2,4],[4,5,3]])
print("matrix\n ",matrix)
print("matriks\n",matrix2)
#matrix3 = np.add(matrix,matrix2)
#print("matrix jumlah",matrix3)

matrix4 = np.linalg.inv(matrix2)
print("hasil\n :",matrix4)



