#list

list1=["agus","busi","tina","Zimbabwe"]
print("list ke dua adalah",list1[2])
print("list semuanya",list1[0:4])
print("panjang list1 adalah",list1.__len__())

list1.append(100)
print("isi seluruh list :",list1)

list1.remove("agus")
print("isi",list1)

del list1[2]
print("isi lagi",list1)

#dictionary

dictionary1={'nama':'asa','umur':'21','status':'kuliah'}
print("namanya",dictionary1["nama"])
dictionary1["nama"]="edward"
print("namanya",dictionary1["nama"])
dictionary1["hobi"]="bola"
print("hobi :",dictionary1["hobi"])
del dictionary1['status']
print(dictionary1)

#tuple untuk menyimpan koordinat
tuple1=(1,2,3,4,5,6)
print("nilai tuple",tuple1[1:4])

#array---sarankan menggunakan array
