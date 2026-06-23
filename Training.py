import numpy as np

notes = np.array([
    [12, 15, 14],
    [18, 17, 19],
    [10, 11, 9],
    [16, 14, 13]
])


print(np.where( notes == 19, 20, notes ))
