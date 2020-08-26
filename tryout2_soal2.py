# SOAL KEDUA
# Buat function untuk menghitung teks tertentu dalam suatu string
# komentar = 'Saya sedang belajar Data Science'
# HitungTeks('belajar', komentar)   --> Ada 1 kata 'belajar'

def HitungTeks(kata, komentar):
    count = 0
    pecah = komentar.split()
    for i in pecah:
        if i == kata:
            count+=1
    final = print(f'Terdapat {count} kata {kata}')
    return final

komentar = 'Saya sedang belajar Data Science dengan cara belajar dan belajar'
HitungTeks('belajar', komentar)