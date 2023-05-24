import matplotlib.pyplot as plt
import numpy as np
import cv2
#Impor library matplotlib.pyplot, numpy, dan cv2 yang akan digunakan dalam program.

citra1 = cv2.imread("image/DC.jpeg", 0)
citra2 = cv2.imread("image/marvel.jpg", 0)#Membaca dua citra dengan nama file "DC.jpeg" dan "marvel.jpg" dalam mode grayscale menggunakan fungsi cv2.imread. Citra pertama disimpan dalam variabel citra1 dan citra kedua disimpan dalam variabel citra2.

print('Shape citra 1 : ', citra1.shape)
print('Shape citra 2 : ', citra2.shape)#Mencetak dimensi citra pertama (shape) menggunakan atribut shape dan mencetak dimensi citra kedua. Dimensi citra ditampilkan dalam format "(jumlah baris, jumlah kolom)".

fig, axes = plt.subplots(1, 2, figsize=(10, 10))
ax = axes.ravel()#Membuat subplots dengan ukuran 1x2 (total 2 subplot) dan mengatur ukuran figur menjadi 10x10.

ax[0].imshow(citra1, cmap = 'gray')
ax[0].set_title("Citra 1")
ax[1].imshow(citra2, cmap = 'gray')
ax[1].set_title("Citra 2")#Menampilkan citra pertama pada subplot pertama dengan menggunakan colormap 'gray', memberikan judul "Citra 1". Menampilkan citra kedua pada subplot kedua dengan menggunakan colormap 'gray', memberikan judul "Citra 2".

plt.show()#Menampilkan keseluruhan plot.

#proses filter rerata untuk citra mobil
#F2 = double(inputMobil);
#for baris=2 : tinggiA-1
#    for kolom=2 : lebarA-1
#        jum = F2(baris-1, kolom-1)+ F2(baris-1, kolom) + F2(baris-1, kolom-1) + ...
#              F2(baris, kolom-1) + F2(baris, kolom) + F2(baris, kolom+1) + ...
#              F2(baris+1, kolom-1) + F2(baris+1, kolom) + F2(baris+1, kolom+1);         
#         outputMobil(baris, kolom) = uint8(1/9 * jum);
#    end
#end

copyCitra1 = citra1.copy().astype(float)
copyCitra2 = citra2.copy().astype(float)#Membuat salinan dari citra pertama (citra1) dan citra kedua (citra2) menggunakan metode copy() dan mengubah tipe data salinan menjadi float menggunakan metode astype(float). Hasilnya disimpan dalam variabel copyCitra1 dan copyCitra2.

m1,n1 = copyCitra1.shape
output1 = np.empty([m1, n1])

m2,n2 = copyCitra2.shape
output2 = np.empty([m2, n2])
#Mengambil ukuran baris dan kolom dari copyCitra1 dan copyCitra2 menggunakan atribut shape. Membuat array kosong dengan ukuran yang sama seperti copyCitra1 dan copyCitra2 menggunakan np.empty(). Array ini akan digunakan untuk menyimpan hasil citra keluaran. Array pertama disimpan dalam variabel output1 dan array kedua disimpan dalam variabel output2.

print('Shape copy citra 1 : ', copyCitra1.shape)
print('Shape output citra 1 : ', output1.shape)
print('m1 : ',m1)
print('n1 : ',n1)
print()
#Mencetak dimensi dari copyCitra1 dan output1. Mencetak nilai m1 dan n1 yang merupakan ukuran baris dan kolom dari copyCitra1.

print('Shape copy citra 2 : ', copyCitra2.shape)
print('Shape output citra 3 : ', output2.shape)
print('m2 : ',m2)
print('n2 : ',n2)
print()
#Mencetak dimensi dari copyCitra2 dan output2. Mencetak nilai m2 dan n2 yang merupakan ukuran baris dan kolom dari copyCitra2.

for baris in range(0, m1-1):
    for kolom in range(0, n1-1):
        a1 = baris
        b1 = kolom
        jumlah = copyCitra1[a1-1, b1-1] + copyCitra1[a1-1, b1] + copyCitra1[a1-1, b1-1] + \
                 copyCitra1[a1, b1-1] + copyCitra1[a1, b1] + copyCitra1[a1, b1+1] + \
                 copyCitra1[a1+1, b1-1] + copyCitra1[a1+1, b1] + copyCitra1[a1+1, b1+1];  
        output1[a1, b1] = (1/9 * jumlah)
        #Melakukan perulangan untuk setiap elemen dalam copyCitra1 menggunakan indeks baris (baris) dan indeks kolom (kolom). Menghitung jumlah dari nilai piksel pada lingkungan 3x3 setiap piksel dan membaginya dengan 9. Hasilnya disimpan dalam output1.

for baris1 in range(0, m2-1):
    for kolom1 in range(0, n2-1):
        a1 = baris1
        b1 = kolom1
        jumlah = copyCitra2[a1-1, b1-1] + copyCitra2[a1-1, b1] + copyCitra2[a1-1, b1-1] + \
                 copyCitra2[a1, b1-1] + copyCitra2[a1, b1] + copyCitra2[a1, b1+1] + \
                 copyCitra2[a1+1, b1-1] + copyCitra2[a1+1, b1] + copyCitra2[a1+1, b1+1];  
        output2[a1, b1] = (1/9 * jumlah)
        #Melakukan perulangan untuk setiap elemen dalam copyCitra2 menggunakan indeks baris1 (baris1) dan indeks kolom1 (kolom1). Menghitung jumlah dari nilai piksel pada lingkungan 3x3 setiap piksel dan membaginya dengan 9. Hasilnya disimpan dalam output2.

fig, axes = plt.subplots(2, 2, figsize=(10, 10))
ax = axes.ravel()

ax[0].imshow(citra1, cmap = 'gray')
ax[0].set_title("Input Citra 1")

ax[1].imshow(citra2, cmap = 'gray')
ax[1].set_title("Input Citra 1")

ax[2].imshow(output1, cmap = 'gray')
ax[2].set_title("Output Citra 1")

ax[3].imshow(output2, cmap = 'gray')
ax[3].set_title("Output Citra 2")

plt.show()#Membuat subplots dengan ukuran 2x2 (total 4 subplot) dan mengatur ukuran figur menjadi 10x10. Menampilkan citra pertama (citra1) pada subplot pertama, citra kedua (citra2) pada subplot kedua, output1 pada subplot ketiga, dan output2 pada subplot keempat. Setiap subplot diberi judul yang sesuai. Menampilkan keseluruhan plot.