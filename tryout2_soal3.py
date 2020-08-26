# SOAL KETIGA
# Gunakan lambda expressions dan filter() function untuk memfilter nama-nama orang yang diawali huruf 'B'
# nama = ['Andi', 'Caca', 'Budi', Dody','Bambang','Edi','Ari','Bintang']
# output = ['Budi','Bambang','Bintang']

list_nama = ['Andi', 'Caca', 'Budi', 'Dody','Bambang','Edi','Ari','Bintang']
# start_name = 'B' 
# result = list(filter(lambda nama: nama.startswith(start_name) , list_nama))
result = list(filter(lambda nama: 'B' in nama[0], list_nama))
print(result)