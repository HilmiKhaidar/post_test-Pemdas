jumlah_pasien = int(input("masukan jumlah pasien : "))

list_nama = []
list_darah_dishtolik = []
list_darah_sistolik =[]

for nama in range(jumlah_pasien):
    nama = input("masukan nama :")
    distolik = float(input("Masukan tekanan darah diastolik : "))
    sistolik = float(input("Masukan tekanan darah sistolik : "))

    list_nama.append(nama)
    list_darah_dishtolik.append(distolik)
    list_darah_sistolik.append(sistolik)

ratarata_distolik = sum(list_darah_dishtolik) / len(list_darah_dishtolik)
ratarata_sistolik = sum(list_darah_sistolik) / len(list_darah_sistolik)

print(f"rata -rata tekanan darah diastolik {ratarata_distolik}")
print(f"rata-rata tekanan darah sistolik {ratarata_sistolik}")

for i in range(jumlah_pasien) :
    if list_darah_sistolik[i] > 140 or list_darah_dishtolik[i] > 90 :
        print(f"psien ke {i+1}")
        print(f"nama {list_nama[i]}")
        print(f"tekanan darah sistolik {list_darah_sistolik [i]}")
        print(f"tekanan darah diastolik {list_darah_dishtolik[i]}")
        print(f"harus cepat cepat di tanganin dikarnakan hipertensi")