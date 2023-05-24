# memanggil modul yang diperlukan
import cv2
import numpy as np
from matplotlib import pyplot as plt

#bgr
img = cv2.imread('image/kucing.jpeg')

#rgb
kucing = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
kernel = np.ones((3,3),np.float32)/25
print(kernel)

kucing_filter = cv2.filter2D(img,-1,kernel)

# tampilkan gambar awal tanpa filter
plt.imshow(img)
plt.show()

fig, axes = plt.subplots(1, 2, figsize=(8, 8))
ax = axes.ravel() #Membuat subplots dengan ukuran 5x2 (total 10 subplot) dan mengatur ukuran figur menjadi 20x20.

ax[0].imshow(kucing_filter, cmap=plt.cm.gray)
ax[0].set_title("Citra Input")
ax[1].hist(kucing_filter.ravel(), bins=256)
ax[1].set_title('Histogram Input')# Menampilkan citra asli pada subplot pertama, memberikan judul "Citra Input"dan"Hisyogram Input"
# lakukan filtering

plt.imshow(kucing_filter)
plt.show()

# salt and pepper

# perbesar ukuran hasil plotting jika diperlukan
plt.rcParams["figure.figsize"] = (7,7)

# plot pertama, gambar asli
plt.subplot(221)#Memposisikan citra di poisisi kolom 1 dan baris 1
plt.imshow(kucing)
plt.title('Original')
plt.xticks([])
plt.yticks([])

# kedua, hasil filter
plt.subplot(222)#Memposisikan citra di poisisi kolom 2 dan baris 1
plt.imshow(kucing_filter)
plt.title('Averaging')
plt.xticks([])
plt.yticks([])

plt.subplot (223)#Memposisikan citra di poisisi kolom 1 dan baris 2
plt.hist(kucing.flatten(), 256, [0, 256])#menampilkan historgram dari kucing
plt.xlim([0, 256]) 
plt.title('Histogram Gambar Asli')

plt.subplot (224)#Memposisikan citra di poisisi kolom 2 dan baris 2
plt.hist(kucing_filter.flatten(), 256, [0, 256])#menampilkan historgram dari kucing_filter
plt.xlim([0, 256]) 
plt.title('Histogram Gambar Filter')


# Plot!
plt.show()

kucing_blur = cv2.blur(img,(5,5))

# ini adalah cara lain untuk membuat sebuah kernel, 
# yaitu dengan menggunakan np.matrix
# kali ini, ukuran matriksnya 3 x 3
kernel = np.matrix([
          [1, 1, 1],
          [1, 2, 1],
          [1, 1, 1]         
          ])/25
print(kernel)

# buat lagi filteringnya
kucing_filter = cv2.filter2D(img,-1,kernel)

# tampilkan
plt.subplot(221)
plt.imshow(kucing_blur)
plt.title('Kucing blur')
plt.xticks([])
plt.yticks([])

plt.subplot(222)
plt.imshow(kucing_filter)
plt.title('Kucing Filter')
plt.xticks([])
plt.yticks([])

plt.subplot(223)
plt.hist(kucing_blur.flatten(), 256, [0, 256])
plt.title('Kucing Filter')

plt.subplot(224)
plt.hist(kucing_filter.flatten(), 256, [0, 256])
plt.title('Kucing Filter')

plt.tight_layout()
plt.show()