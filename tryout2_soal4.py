# SOAL KEEMPAT
# Buat function untuk menghitung gaji bersih karyawan-karyawan setelah dikurangi pajak 5 persen
# Buat 2 versi: 1) menggunakan function biasa, 2) menggunakan lambda function
# gaji = [5, 8, 9, 10, 20, 6, 5]
# output = [4.75, 7.6, 8.55, 9.5, 19.0, 5.7, 4.75]

def gajibersih(gajikotor):
    list_gajibersih = []
    for i in gajikotor:
        bersih = i * 0.95
        bersih = round(bersih, 2)
        list_gajibersih.append(bersih)
    return list_gajibersih


print(gajibersih([5, 8, 9, 10, 20, 6, 5]))