# Membuat fungsi untuk menghitung FPB
def hitung_fpb(x,y):
    if x < y:
        bil_terkecil = x
    else:
        bil_terkecil = y

    for i in range(1, bil_terkecil + 1):
        if x % i == 0 and y % i == 0:
            fpb = i

    return fpb

# Membuat fungsi untuk menghitung KPK
def hitung_kpk(x, y):
    bil1 = x
    bil2 = y
    while bil1 != bil2:
        if bil1 < bil2:
            bil1 += x
        else:
            bil2 += y
    return bil1

# Membaca input dari pengguna
angka1 = int(input("Ketik angka pertama".ljust(24) + ": "))
angka2 = int(input("Ketik angka kedua".ljust(24) + ": "))

# Memanggil fungsi FPB dan KPK dan menyimpan hasilnya ke dalam variabel
fpb = hitung_fpb(angka1, angka2)
kpk = hitung_kpk(angka1, angka2)

# mencetak hasil
print(f"FPB dari {angka1} dan {angka2} adalah =  {fpb}")
print(f"KPK dari {angka1} dan {angka2} adalah =  {kpk}")
