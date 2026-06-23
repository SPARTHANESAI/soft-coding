import numpy as np 
import matplotlib.pyplot as plt 

# Lecture de l'image
img = plt.imread('food1.jpg')
# Affichage du format de l'image
print(img.shape)
# Affichage du type de l'image
print(img.dtype)
# Application du filtre mirroir horizontal
image = img[:, ::-1, :]
# Application de la formule de luminance 
image_2D = 0.299*image[:, :, 0] + 0.587*image[:, :, 1] + 0.114*image[:, :, 2]
# Augmentation de la luminosité de 30%
image_2D_30 = np.clip(image_2D*1.3, 0, 255)
# Isolation du burger
burger_zoom = image_2D_30[150:421, 100:451]
# Affichage du rendu final 
plt.imshow(image)
plt.show()