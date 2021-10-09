from food import Food
from drink import Drink

#Makanan
food1 = Food('Nasi Goreng', 1, 300)
food2 = Food('Cimol', 2, 200)
food3 = Food('Sate Ayam', 5, 300)

foods = [food1, food2, food3]

#Minuman
drink1 = Drink('Wedang Jahe', 1, 120)
drink2 = Drink('Wedang Uwuh', 2, 200)
drink3 = Drink('Wedang EkstraJoss', 8, 150)

drinks = [drink1, drink2, drink3]

#Ucapan selamat Datang
print(" =========================== ")
print(" Welcome to Vinzz Restaurant ")
print(" =========================== ")

menu = input("Apakah kamu ingin memesan sesuatu? [Y/N] ")
if menu != "Y":
    quit()
print("Okay, silahkan lihat menu yang tersedia :) ")



print("======================")
print('|       Foods        |')
print("======================")
index = 0
for food in foods:
    print(str(index) + '. ' + food.info())
    index += 1

print("======================")
print('|       Drink        |')
print("======================")
index = 0
for drink in drinks:
    print(str(index) + '. ' + drink.info())
    index += 1

print ('-------------------------------------------------------')

food_order = int(input("Masukkan nomor makanan: "))
selected_food = foods[food_order]

drink_order = int(input("Masukkan nomor minuman: "))
selected_drink = drinks[drink_order]

#Mengambil input dari console/terminal 
count = int(input("Mau berapa paket makanan? (Diskon 10% untuk 3 atau lebih) "))

#Memanggil method get_total_price dari selected_food dan selected_drink
result = selected_food.get_total_price(count) + selected_drink.get_total_price(count)

#Cetak total harga
print("===========================")
print("| Total harga adalah " + str(result) + " $ |")
print("===========================")