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

#for baris=2 : tinggi-1
#    for kolom=2 : lebar-1
#        minPiksel = min([F(baris-1, kolom-1) F(baris-1, kolom) F(baris, kolom+1) ...
#            F(baris, kolom-1) F(baris, kolom+1) F(baris+1, kolom-1)  ...
#            F(baris+1, kolom) F(baris+1, kolom+1)]);
#        
#        maksPiksel = max([F(baris-1, kolom-1) F(baris-1, kolom) F(baris, kolom+1)    ...
#            F(baris, kolom-1) F(baris, kolom+1) F(baris+1, kolom-1)  ...
#            F(baris+1, kolom) F(baris+1, kolom+1)]);    
#            
#        if F(baris, kolom) < minPiksel
#           G(baris, kolom) = minPiksel;
#        else
#            if F(baris, kolom) > maksPiksel
#                G(baris, kolom) = maksPiksel;
#            else
#                G(baris, kolom) = F(baris, kolom);
#            end
#        end    
#    end
#end

copyCitra1 = citra1.copy()
copyCitra2 = citra2.copy()#Menggunakan fungsi copy() untuk membuat salinan dari citra citra1 dan citra2 ke variabel copyCitra1 dan copyCitra2.

m1,n1 = copyCitra1.shape
output1 = np.empty([m1, n1])

m2,n2 = copyCitra2.shape
output2 = np.empty([m2, n2])#Mendapatkan dimensi (jumlah baris dan kolom) citra copyCitra1 dan copyCitra2 menggunakan atribut shape. Membuat array kosong output1 dan output2 dengan dimensi yang sama dengan citra yang sesuai.

print('Shape copy citra 1 : ', copyCitra1.shape)
print('Shape output citra 1 : ', output1.shape)
print('m1 : ',m1)
print('n1 : ',n1)
print()

print('Shape copy citra 2 : ', copyCitra2.shape)
print('Shape output citra 3 : ', output2.shape)
print('m2 : ',m2)
print('n2 : ',n2)
print()
#Menampilkan dimensi dari copyCitra1, output1, copyCitra2, dan output2 menggunakan fungsi print(). Output ini memberikan informasi tentang jumlah baris dan kolom dari masing-masing citra dan output.

# Mengiterasi melalui setiap baris citra 1
for baris in range(0, m1-1):
    # Mengiterasi melalui setiap kolom citra 1
    for kolom in range(0, n1-1):
        
        a1 = baris
        b1 = kolom
        
        # Mendapatkan nilai piksel sekitar
        arr = np.array([copyCitra1[a1-1, b1-1], copyCitra1[a1-1, b1], copyCitra1[a1, b1+1], \
            copyCitra1[a1, b1-1], copyCitra1[a1, b1+1], copyCitra1[a1+1, b1-1],  \
            copyCitra1[a1+1, b1], copyCitra1[a1+1, b1+1]])
        
        # Menentukan nilai piksel minimum dan maksimum
        minPiksel = np.amin(arr);        
        maksPiksel = np.amax(arr);    
            
        # Memperbarui piksel output1 sesuai dengan aturan filter
        if copyCitra1[baris, kolom] < minPiksel :
            output1[baris, kolom] = minPiksel
        else :
            if copyCitra1[baris, kolom] > maksPiksel :
                output1[baris, kolom] = maksPiksel
            else :
                output1[baris, kolom] = copyCitra1[baris, kolom]

# Mengiterasi melalui setiap baris citra 2
for baris1 in range(0, m2-1):
    # Mengiterasi melalui setiap kolom citra 2
    for kolom1 in range(0, n2-1):
        
        a1 = baris1
        b1 = kolom1
        
        # Mendapatkan nilai piksel sekitar
        arr = np.array([copyCitra2[a1-1, b1-1], copyCitra2[a1-1, b1], copyCitra2[a1, b1+1], \
            copyCitra2[a1, b1-1], copyCitra2[a1, b1+1], copyCitra2[a1+1, b1-1],  \
            copyCitra2[a1+1, b1], copyCitra2[a1+1, b1+1]])
        
        # Menentukan nilai piksel minimum dan maksimum
        minPiksel = np.amin(arr);        
        maksPiksel = np.amax(arr);    
            
        # Memperbarui piksel output2 sesuai dengan aturan filter
        if copyCitra2[baris1, kolom1] < minPiksel :
            output2[baris1, kolom1] = minPiksel
        else :
            if copyCitra2[baris1, kolom1] > maksPiksel :
                output2[baris1, kolom1] = maksPiksel
            else :
                output2[baris1, kolom1] = copyCitra2[baris1, kolom1]

fig, axes = plt.subplots(2, 2, figsize=(10, 10))
ax = axes.ravel()

ax[0].imshow(citra1, cmap = 'gray')
ax[0].set_title("Input Citra 1")

ax[1].imshow(citra2, cmap = 'gray')
ax[1].set_title("Input Citra 2")

ax[2].imshow(output1, cmap = 'gray')
ax[2].set_title("Output Citra 1")

ax[3].imshow(output2, cmap = 'gray')
ax[3].set_title("Output Citra 2")

plt.show()#Membuat subplots dengan ukuran 2x2 (total 4 subplot) dan mengatur ukuran figur menjadi 10x10. Menampilkan citra pertama (citra1) pada subplot pertama, citra kedua (citra2) pada subplot kedua, output1 pada subplot ketiga, dan output2 pada subplot keempat. Setiap subplot diberi judul yang sesuai. Menampilkan keseluruhan plot.