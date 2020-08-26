# SOAL KELIMA (BONUS)
# Buat function untuk membuat list angka ganjil dalam range tertentu
# tapi bergantian ganjil positif dan ganjil negatif
# Contoh: ganjilMix(20) ---> output: [1, -3, 5, -7, 9, -11, 13, -15, 17, -19]

def ganjilMix(batas):
    angka_ganjil = []
    for ganjil in range(batas):           # looping untuk memasukkan semua angka ganjil ke dalam list kosong 
        if ganjil%2 != 0:                 # kondisi angka ganjil adalah jika di mod 2 hasilnya bukan 0
            angka_ganjil.append(ganjil)
    
    for i in range(len(angka_ganjil)):    #looping untuk setiap angka dijadikan minus
        if i%2 != 0:
            angka_ganjil[i] = angka_ganjil[i] * -1
                   
    return angka_ganjil
                   
    
batas = 21
print(ganjilMix(batas))