#Cirkeldiagram
#Navne til hver del
import matplotlib.pyplot as plt
name = ['Hund', 'Kat', 'Gris', 'Hest']
#Data til hver del (husk samme rækkefølge som labels)
number = [10, 20, 30,. 40]
# Plot/Graf
#plt.figure()
#plt.subplot(131)
plt.pie(number, labels=name)
# ,autopct='%1.1f%%'
# ,startangle=90
# ,explode=(0,0.1,0.,0.3)
#plt.title("Dyr")
#plt.legende()
plt.show()

