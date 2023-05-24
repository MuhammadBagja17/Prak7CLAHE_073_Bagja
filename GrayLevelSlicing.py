import cv2
import numpy as np
import matplotlib.pyplot as plt
#Impor library cv2, numpy, dan matplotlib.pyplot yang akan digunakan dalam program.

img = cv2.imread("image/DC.jpeg", 0)#Membaca citra dengan nama file "DC.jpeg" dalam mode grayscale menggunakan fungsi cv2.imread. Hasilnya disimpan dalam variabel img.

row, column = img.shape#Mengambil ukuran baris dan kolom dari citra dan menyimpannya dalam variabel row dan column.

img1 = np.zeros((row,column),dtype = 'uint8')#Membuat array kosong dengan ukuran yang sama dengan citra menggunakan np.zeros. Tipe data yang digunakan adalah 'uint8'. Array ini akan digunakan untuk menyimpan hasil citra keluaran.
 
min_range = 10
max_range = 60
#Menginisialisasi nilai rentang minimum dan maksimum untuk transformasi citra.
 
for i in range(row):
    for j in range(column):
        if img[i,j]>min_range and img[i,j]<max_range:
            img1[i,j] = 255
        else:
            img1[i,j] = 0
            #Melakukan perulangan untuk setiap elemen dalam citra menggunakan indeks baris (i) dan indeks kolom (j). Memeriksa apakah nilai piksel dalam rentang yang ditentukan. Jika ya, setel piksel pada citra keluaran menjadi 255 (putih), jika tidak, setel piksel menjadi 0 (hitam).

fig, axes = plt.subplots(2, 2, figsize=(12, 12))
ax = axes.ravel()#Membuat subplots dengan ukuran 2x2 (total 4 subplot) dan mengatur ukuran figur menjadi 12x12.

ax[0].imshow(img, cmap=plt.cm.gray)
ax[0].set_title("Citra Input")
ax[1].hist(img.ravel(), bins=256)
ax[1].set_title('Histogram Input')#Menampilkan citra asli pada subplot pertama, memberikan judul "Citra Input". Menampilkan histogram citra asli pada subplot kedua, memberikan judul "Histogram Input".

ax[2].imshow(img1, cmap=plt.cm.gray)
ax[2].set_title("Citra Output")
ax[3].hist(img1.ravel(), bins=256)
ax[3].set_title('Histogram Output')#Menampilkan citra hasil transformasi pada subplot ketiga, memberikan judul "Citra Output". Menampilkan histogram citra hasil transformasi pada subplot keempat, memberikan judul "Histogram Output".

plt.show()#Menampilkan keseluruhan plot.