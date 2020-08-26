list_gajikotor = [5, 8, 9, 10, 20, 6, 5]
list_gajibersih = []

gajibersih = list(map(lambda hitung: hitung * 0.95, list_gajikotor))
for i in gajibersih:
    i = round(i, 2)
    list_gajibersih.append(i)
print(list_gajibersih)
