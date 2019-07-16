class pasien:
    jumlah=0
    def __init__(self,nama,berat,tinggi):
        self.nama=nama
        self.berat=berat
        self.tinggi=tinggi
        pasien.jumlah = pasien.jumlah +1

    def hitungBMI(self):
        print("Nama Pasien:",self.nama)
        BMI=self.berat/(self.tinggi**2)
        print("BMInya adalah",BMI)
        if (BMI<18.5):
            print("kekurangan berat badan")
        elif(BMI>=18.5 and BMI<24.9):
            print("berat badan ideal")
        elif(BMI>=24.9 and BMI<29.9):
            print("kelebihan berat badan level1")
        else:
            print("obesitas")

    def berat_ideal(self):
        bbideal=(self.tinggi*100-100) - (10/100 *(self.tinggi*100-100))
        print("berat ideal adalah",bbideal)

        print("===========================================================================================")

pasien1= pasien("edward",60,1.70)#instiantion
pasien1.hitungBMI()
pasien1.berat_ideal()

pasien1= pasien("koed",70,2)#instiantion
pasien1.hitungBMI()
pasien1.berat_ideal()
print("jumlah pasien adalah",pasien.jumlah)