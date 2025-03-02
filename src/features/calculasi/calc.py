# Inisialisasi angka awal
a = int(5000)  # angka pertama
b = int(2000)  # angka kedua
c = int(200)  # angka ketiga
d = int(500)  # nilai penambahan

# Menambahkan 500 pada angka pertama dan kedua
e = int(a + d)  # angka pertama + 500
f = int(b + d)  # angka kedua + 500

# Menghitung hasil akhir: (angka pertama + 500) + (angka kedua + 500) - angka ketiga
g = e + f - c

# Menampilkan hasil
print(f"Angka pertama a = {a}")
print(f"Angka kedua b = {b}")
print(f"Angka ketiga c = {c}")

# separator
print("-" * 50)
# 1. Menampilkan hasil penambahan 500 pada angka pertama
print(f"Hasil penambahan 500 pada angka pertama: {a} + {d} = {e}")

# separator
print("-" * 50)
# 2. Menampilkan hasil penambahan 500 pada angka kedua
print(f"Hasil penambahan 500 pada angka kedua: {b} + {d} = {f}")

# separator
print("-" * 50)
# Menampilkan hasil akhir
print(f"Hasil akhir: {e} + {f} - {c} = {g}")
