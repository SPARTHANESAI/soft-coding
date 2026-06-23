import numpy as np 
import matplotlib.pyplot as plt

img = plt.imread("img3.jpg")
print(f"structure de l'image : {img.shape}")

R = img[:, :, 0]
V = img[:, :, 1]
B = img[:, :, 2]

gris  = 0.299 * R + 0.587 * V + 0.116 * B
print(gris.shape)
plt.imshow(gris, cmap="gray")
plt.axis("off")
plt.show()