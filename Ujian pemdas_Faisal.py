# Rumus Volume Balok
print ("\n1.Volume Balok")
panjang = int(input("masukkan panjang :"))
lebar= int(input("masukkan lebar: "))
tinggi= int(input("masukkan tinggi: "))
volume_balok = panjang * lebar * tinggi

print ("Volume Balok Adalah",volume_balok)

# Rumus Volume Kubus
print ("\n2.Volume Kubus")
sisi = int(input("masukkan nilai sisi: "))
volume_kubus = sisi * sisi * sisi

print ("Volume kubus adalah", volume_kubus)

# Rumus Volume Limas
print ("\n3.Volume Limas")
sisi_l = int(input("masukkan nilai sisi_l: "))
tinggi_l = int(input("masukkan nilai tinggi_l: "))
luas_l = sisi_l * sisi_l
volume_limas = luas_l * tinggi_l

print ("volume limas adalah",volume_limas)

# Rumus volume tabung
print ("\n4. Volume Tabung")
r = int(input("masukkan nilai r: "))
tinggi_t = int(input("masukkan nilai tinggi_t: "))
volume_tabung = 22/7 * r * r * tinggi_t

print ("volume tabung adalah",volume_tabung)

# Celcius Ke Reamur
print ("\n5.Celcius ke Reamur")
C = int(input("masukkan nilai Celcius: "))
Reamur = 4/5 * C

print ("Celcius ke Reamur adalah",Reamur)
