def kategori_bilangan(x):
    kategori = []

    # Bilangan bulat
    if isinstance(x, int):
        kategori.append("bulat")

    # Bilangan cacah (>= 0)
    if x >= 0:
        kategori.append("cacah")

    # Bilangan negatif
    if x < 0:
        kategori.append("negatif")

    # Bilangan nol
    if x == 0:
        kategori.append("nol")

    # Bilangan asli (> 0)
    if x > 0:
        kategori.append("asli")

    # Genap atau ganjil
    if x % 2 == 0:
        kategori.append("genap")
    else:
        kategori.append("ganjil")

    # Bilangan prima atau komposit (hanya jika > 1)
    if isinstance(x, int) and x > 1:
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                kategori.append("komposit")
                break
        else:
            kategori.append("prima")

    return kategori

# Membaca input dari pengguna
x = int(input("Ketik angka : "))

# Mencetak hasil
print(kategori_bilangan(x))
