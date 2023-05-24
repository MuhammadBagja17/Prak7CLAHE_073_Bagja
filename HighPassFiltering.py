# Highpass Filter

# sebenarnya kita tidak perlu melakukan filtering lagi. Cukup sekali saja 
# di bagian awal, selama notebook ini tetap terhubung
import cv2
import numpy as np
from matplotlib import pyplot as plt

# memanggil citra sebagai grayscale (argument 0)
img = cv2.imread('image/sodoku.png',0)

# menerapkan algoritma high-pass filtering:
# laplacian
laplacian = cv2.Laplacian(img,cv2.CV_64F)

# sobel dengan ukuran kernel 5
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

# Catatan:
# CV_64F pada contoh di atas menunjukkan nilai bit dari citra 
# yang dihasilkan serta tipe datanya (F = Float)

# perbesar ukuran hasil plotting 
plt.rcParams["figure.figsize"] = (20,20)

# menampilkan hasil filter
plt.subplot(2,2,1)
plt.imshow(img,cmap = 'gray')
plt.title('Original')
plt.xticks([])
plt.yticks([])
plt.subplot(2,2,2)
plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian')
plt.xticks([])
plt.yticks([])
plt.subplot(2,2,3)
plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X')
plt.xticks([])
plt.yticks([])
plt.subplot(2,2,4)
plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y')
plt.xticks([])
plt.yticks([])
plt.show()

plt.subplot(221)
plt.hist(img.flatten(), 256, [0, 256])
plt.title('Origunal')
plt.subplot(222)
plt.hist(laplacian.flatten(), 256, [0, 256])
plt.title('lapcian')
plt.subplot(223)
plt.hist(sobelx.flatten(), 256, [0, 256])
plt.title('Sobelx')
plt.subplot(224)
plt.hist(sobely.flatten(), 256, [0, 256])
plt.title('Sobely')

plt.tight_layout()
plt.show()

# memanggil citra sebagai grayscale (argument 0)
img = cv2.imread('image/baymax.jpg',0)

# memanggil fungsi Canny Edges dengan argument (citra, nilai_min, nilai_max)
edges = cv2.Canny(img,100,200)

plt.subplot(221)
plt.imshow(img,cmap = 'gray')
plt.title('Original Image')
plt.xticks([])
plt.yticks([])
plt.subplot(222)
plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image')
plt.xticks([])
plt.yticks([])

plt.subplot(223)
plt.hist(img.flatten(), 256, [0, 256])
plt.title('Kucing Filter')
plt.subplot(224)
plt.hist(edges.flatten(), 256, [0, 256])
plt.title('Kucing Filter')

plt.tight_layout()
plt.show()