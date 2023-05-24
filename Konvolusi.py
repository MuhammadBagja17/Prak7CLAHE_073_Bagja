# Mengimpor library yang diperlukan
import matplotlib.pyplot as plt
import numpy as np
import cv2

# Membaca citra menggunakan OpenCV
citra1 = cv2.imread("image/marvel.jpg")
print(citra1.shape)

# Menampilkan citra menggunakan Matplotlib
plt.imshow(citra1, cmap='gray')
plt.show()

# Membuat kernel untuk filter yang akan digunakan
kernel = np.array([[-1, 0, -1], 
                   [0, 4, 0], 
                   [-1, 0, -1]])

# Mengaplikasikan filter ke citra menggunakan fungsi filter2D dari OpenCV
citraOutput = cv2.filter2D(citra1, -1, kernel)

# Menampilkan citra asli dan citra hasil pemrosesan
fig, axes = plt.subplots(1, 2, figsize=(12, 12))
ax = axes.ravel()

ax[0].imshow(citra1, cmap='gray')
ax[0].set_title("Citra Input")
ax[1].imshow(citraOutput, cmap='gray')
ax[1].set_title("Citra Output")

plt.show()