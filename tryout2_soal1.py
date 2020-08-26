# SOAL PERTAMA
# Buat function untuk mendapatkan domain dari alamat user
# alamat = 'alamatku@gmail.com'
# emailku = 'belajar@yahoo.com'
# domain(alamat) -----> output: 'gmail.com'
# domain(emailku) -----> output: 'yahoo.com'

def domain(email):
    index = email.index('@')          #menggunakan function index untuk menemukan pada index berapa parameter ditemukan. variabel index akan menampung nomor index '@' pertama
    domain = email[index:]            #kita gunakan slicing berawal dari index sampai akhir
    return domain

print(domain('yosafat@gmail.com'))
print(domain('yosafat@yahoo.com'))
print(domain('yosafat@opera.com'))