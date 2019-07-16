import numpy as np

array = np.array([1,2,3,4,5,6,7,8,9])
print("nilai array :\n", array)

#reshoping array numpy
reshapedArray = np.reshape(array,(3,-1))
print("reshaped array:\n",reshapedArray)

#menghapus bagian dari array
deletearray = np.delete(reshapedArray,slice(1,3),1)
print("terhapus:\n",deletearray)

#menggabungkan array numpy
gabungan = np.concatenate((reshapedArray,deletearray.reshape((1,3))),axis=0)
print("gabungan:\n",gabungan)

#sorting array numpy
sortindex = np.argsort(gabungan[:,1])
print("sort index\n",sortindex)
sortedArray = gabungan[sortindex]
print("hasil sortie\n",sortedArray)

#conditional array
cond = sortedArray  <4
print("cond\n",cond)
sortedArray[cond] =1
print("conditon array:\n",sortedArray)
