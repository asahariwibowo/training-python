import matplotlib.pyplot as plt
import numpy as np

path="file_angka"
x = np.loadtxt(path, delimiter=",")

y1 = np.array([1,2,3,4,5,6])
y2 = x**2


plt.plot(x,y1, label="data linear")

plt.scatter(x,y1, marker="+", s=200, c="blue") #scatter memplot(simbol) titik pertemuan sesuai inputan
plt.plot(x,y2, c="red", label="data kuadrat")
plt.legend()
plt.title("belajat ploting matlotlib")
plt.xlabel("nilai x")
plt.ylabel("nilai y")
plt.show()