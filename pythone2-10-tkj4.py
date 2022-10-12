# membuat Tipe data koleksi

koleksi_data_str=["pisang","mangga","jambu","semangka"]

koleksi_data_int=[200,300,400,500]

koleksi_data_mix=["Rizky billar", 100, True,"Reza arap"]

print("koleksi data string:",koleksi_data_str)

print("koleksi data intger:",koleksi_data_int)

print("koleksi data campuran:",koleksi_data_mix)

koleksi_nama_hewan =["gajah","harimau","singa"]

koleksi_nilai_uts =[77,89,90]

koleksi_teman_sebangku =["ridho","isal","pai"]

print("Koleksi nama Hewan:", koleksi_nama_hewan)

print("Koleksi nilai UTS:", koleksi_nilai_uts)

print("Koleksi teman Sebangku:", koleksi_teman_sebangku)

#Tampilkan data koleksi dengan indeks

# Data kes 2 nama hewan
print("nama hewan data ke-2:",koleksi_nama_hewan[1])

# Data pertama nili UTS
print("nilai uts data ke-1:",koleksi_nilai_uts[0])

# Data terakhir teman Sebangku
print("nama teman sebangku data ke-3:",koleksi_teman_sebangku[2])


# Tambahkan 1 data disetiap data koleksi
koleksi_teman_sebangku.append("bilal")
koleksi_nama_hewan.append("trex")
koleksi_nilai_uts.append("88")

print(koleksi_teman_sebangku)
print(koleksi_nama_hewan)
print(koleksi_nilai_uts)

# ubalah data terakhir nilai uts
koleksi_nilai_uts[2]=98

print(koleksi_nilai_uts)

# ubalah data ke-3 nama hewan
koleksi_nama_hewan[2]="megalodon"

print(koleksi_nama_hewan)
