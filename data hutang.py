import os
import random
import string
data_hutang = dict()
while True:
    os.system("cls")
    keyFinal = "".join(random.choice(string.ascii_uppercase) for i in range(3))
    nama_penghutang = input(" nama penghutang\t: ")
    jumlah_hutang = input(" jumlah hutang\t\t: ")
    jatuh_tempo = input(" jatuh tempo\t\t: ")
    data_hutang[keyFinal] = {
        'nama': nama_penghutang,
        'jumlah': jumlah_hutang,
        'jatuh_tempo': jatuh_tempo
    }
    opsi = input("Input data hutang LAGI (y/t)? ").lower()
    if opsi == 't':
        break

print("-" * 50)
print(f"key\t nama\t\t jumlah Hutang\t jatuh Tempo")
print("-" * 50)
for key, value in data_hutang.items():
    print(f"{key}\t {value['nama']}\t\t {value['jumlah']}\t\t {value['jatuh_tempo']}\t")
