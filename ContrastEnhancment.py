import numpy as np
import matplotlib.pyplot as plt
# Impor library numpy dan matplotlib.pyplot yang akan digunakan dalam program.
import cv2
# Impor library cv2 (OpenCV).

image = cv2.imread("image/marvel.jpg", 0)#input variabel image dalam folder image

image_equalized = cv2.equalizeHist(image) # Melakukan ekualisasi histogram pada citra menggunakan fungsi equalizeHist dari OpenCV dan menyimpan hasilnya ke dalam variabel image_equalized.

clahe = cv2.createCLAHE(clipLimit=2, tileGridSize=(8,8)) #Membuat objek CLAHE (Contrast Limited Adaptive Histogram Equalization) dengan batasan klip sebesar 2 dan ukuran grid tegel sebesar 8x8.

#Apply CLAHE to the original image
image_clahe = clahe.apply(image)#Menerapkan CLAHE ke citra asli dengan menggunakan metode apply dari objek CLAHE yang telah dibuat sebelumnya. Hasilnya disimpan dalam variabel image_clahe.

# Create an empty array to store the final output
image_cs = np.zeros((image.shape[0],image.shape[1]),dtype = 'uint8')#Membuat array kosong dengan ukuran yang sama dengan citra asli untuk menyimpan output akhir. Tipe data yang digunakan adalah 'uint8'.

# Apply Min-Max Contrasting
min = np.min(image)
max = np.max(image)#Menghitung nilai minimum dan maksimum dari citra asli menggunakan fungsi np.min dan np.max. Hasilnya disimpan dalam variabel min dan max.

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        image_cs[i,j] = 255*(image[i,j]-min)/(max-min)
        #Melakukan perulangan untuk setiap elemen dalam citra menggunakan indeks baris (i) dan indeks kolom (j). Menghitung nilai baru untuk setiap elemen citra dengan menggunakan rumus (255 * (pixel - min) / (max - min)). Hasilnya disimpan dalam array image_cs.

copyCamera = image.copy().astype(float)#Membuat salinan citra asli dan mengubah tipe datanya menjadi float. Salinan ini akan digunakan dalam operasi selanjutnya.

m1,n1 = copyCamera.shape
output1 = np.empty([m1, n1])#Mengambil ukuran citra salinan dan membuat array kosong dengan ukuran yang sama untuk menyimpan output operasi selanjutnya.

for baris in range(0, m1-1):
    for kolom in range(0, n1-1):
        a1 = baris
        b1 = kolom
        output1[a1, b1] = copyCamera[baris, kolom] * 1.9
        # Melakukan perulangan untuk setiap elemen dalam citra salinan menggunakan indeks baris (baris) dan indeks kolom (kolom). Mengalikan setiap elemen dengan konstanta 1.9 dan menyimpan hasilnya dalam array output1.

fig, axes = plt.subplots(5, 2, figsize=(20, 20))
ax = axes.ravel() #Membuat subplots dengan ukuran 5x2 (total 10 subplot) dan mengatur ukuran figur menjadi 20x20.

ax[0].imshow(image, cmap=plt.cm.gray)
ax[0].set_title("Citra Input")
ax[1].hist(image.ravel(), bins=256)
ax[1].set_title('Histogram Input')# Menampilkan citra asli pada subplot pertama, memberikan judul "Citra Input". Menampilkan histogram citra asli pada subplot kedua, memberikan judul "Histogram Input".

ax[2].imshow(image_equalized, cmap=plt.cm.gray)
ax[2].set_title("Citra Output HE")
ax[3].hist(image_equalized.ravel(), bins=256)
ax[3].set_title('Histogram Output HE Method')#Menampilkan citra hasil ekualisasi histogram pada subplot ketiga, memberikan judul "Citra Output HE". Menampilkan histogram citra hasil ekualisasi histogram pada subplot keempat, memberikan judul "Histogram Output HE Method".

ax[4].imshow(image_cs, cmap=plt.cm.gray)
ax[4].set_title("Citra Output CS")
ax[5].hist(image_cs.ravel(), bins=256)
ax[5].set_title('Histogram Output CS Method')#Menampilkan citra hasil kontras stretching pada subplot kelima, memberikan judul "Citra Output CS". Menampilkan histogram citra hasil kontras stretching pada subplot keenam, memberikan judul "Histogram Output CS Method".

ax[6].imshow(image_clahe, cmap=plt.cm.gray)
ax[6].set_title("Citra Grayscale CLAHE")
ax[7].hist(image_clahe.ravel(), bins=256)
ax[7].set_title('Histogram Output CLAHE Method')#Menampilkan citra hasil CLAHE pada subplot ketujuh, memberikan judul "Citra Grayscale CLAHE". Menampilkan histogram citra hasil CLAHE pada subplot kedelapan, memberikan judul "Histogram Output CLAHE Method".

ax[8].imshow(output1, cmap=plt.cm.gray)
ax[8].set_title("Citra Grayscale Perkalian Konstanta")
ax[9].hist(output1.ravel(), bins=256)
ax[9].set_title('Histogram Output Perkalian Konstanta Method')#Menampilkan citra hasil perkalian konstanta pada subplot kesembilan, memberikan judul "Citra Grayscale Perkalian Konstanta". Menampilkan histogram citra hasil perkalian konstanta pada subplot kesepuluh, memberikan judul "Histogram Output Perkalian Konstanta Method".

fig.tight_layout()
plt.show()#Mengatur tata letak subplot agar sesuai dan menampilkan keseluruhan plot.