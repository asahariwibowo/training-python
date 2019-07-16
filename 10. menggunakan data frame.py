#data frame untuk gabungan antara string dan file campuran, numpy hanya angka

import pandas as pd

#membaca dari file dengan panda

path = "file campuran"
data = pd.read_csv(path, delimiter =",") #tambahkan header untuk mengenali judul
print("data :\n",data, "shape :", data.shape)

#indexing pada data frame
print("baris data pertama:\n", data.iloc[0,2])
print("nama-nama\n",data['nama'])

#menghapus data
deleteddata = data.drop('No', axis=1)
print("hapus data:\n",deleteddata)

#membuat data frame sendiri
newdf = pd.DataFrame([['ami',23,'riau']], columns=('Nama','Umur','Asal'))
print("frame baru\n",newdf)

#menggabungkan dua data frame
gabungan = pd.concat([deleteddata,newdf], ignore_index=True)
print('gabungan\n',gabungan)

#menghapus data data terduplikat
noDup = gabungan.drop_duplicates()
print("no duplicated\n",noDup)

#normalsasi rang [0,1] --> rumus = (nilai-min)/(max-min)
min = noDup['Umur'].min()
max = noDup['Umur'].max()
normalized = noDup.copy()
normalized ['Umur']=  (noDup['Umur']-min)/(max-min)
print('hasil normalisasi:\n',normalized)
