import numpy as np 
import matplotlib.pyplot as plt 

image = np.array([
    [
        [255, 0, 0],
        [0, 255, 0]
    ],
    [
        [0, 0, 255],
        [255, 255, 0]
    ]
])


R = image[:, :, 0]
V = image[:, :, 1]
B = image[:, :, 2]

print(f"Rouge : \n {R} \nVert : \n {V} \nBleu : {B}  ")
