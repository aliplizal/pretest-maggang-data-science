import requests

API_KEY = '59db832294e74d5580f2d694c49bd5f8'

BASE_URL = "https://newsapi.org/v2/top-headlines"

# Dictionary untuk menyambungkan pilihan user ke kategori NewsAPI
kategori_berita = {
    '1': 'technology',
    '2': 'business',
    '3': 'sports',
    '4': 'health',
    '5': 'science'
}

# Menampilkan pilihan ke user
print("Selamat datang, mau tahu berita apa hari ini?")
print("[1] Berita seputar teknologi")
print("[2] Berita seputar bisnis")
print("[3] Berita seputar olahraga")
print("[4] Berita seputar kesehatan")
print("[5] Berita seputar science")

# Meminta input user
pilihan = input("Ketik pilihan Anda [1/2/3/4/5] : ").strip()

# Mengecek apakah pilihan valid
if pilihan not in kategori_berita:
    print("Pilihan tidak valid.")

else:
    kategori = kategori_berita[pilihan]

    # Membuat URL dan parameter untuk request
    parameter = {
        'country': 'id',
        'category': kategori,
        'apiKey': API_KEY,
        'pageSize': 5
    }

    # Mengirim request ke NewsAPI
    response = requests.get(BASE_URL, params=parameter)

    # Cek status request
    if response.status_code == 200:
        data = response.json()              # Mengubah hasil response ke format JSON (dictionary)
        articles = data['articles']

        # Mencetak hasil
        print(f"\nBerikut adalah top 5 berita Indonesia bidang {kategori}:\n")

        if not articles:
            print("Maaf, tidak ada berita terbaru untuk kategori ini.")
        else:
            for i, item in enumerate(articles, start=1):
                print(f"{i} - {item['title']} - {item['source']['name']}")
    else:
        print("Terjadi kesalahan saat mengambil data. Cek API Key atau koneksi internet.")


# Catatan:
# Saat ini, data untuk semua kategori berita di wilayah Indonesia belum tersedia atau kosong di API NewsAPI seperti yang ditunjukan pada "/jawaban/output/soal3_buktidatakosong.png". 
# Namun ntuk keperluan pengujian dan pembuktian bahwa permintaan data berhasil dilakukan, parameter 'country' telah diuji dengan diganti menjadi 'us' (Amerika Serikat), 
# dan data berhasil ditampilkan sebagaimana mestinya seperti yang ditunjukan pada "/jawaban/output/soal3_mengganticountry".