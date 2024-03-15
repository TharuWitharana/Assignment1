import cv2
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------Load original image as a grayscale image--------------------------------------
im = cv2.imread("sample.jpeg")[:,:,0]  
plt.gray()
plt.imshow(im)
plt.title("Original Image")
plt.show()

# ------------------------------Plot intensity level reduced images into a one figure------------------------------
f, axarr = plt.subplots(2, 4)   # Setting 2 rows and 4 columns

levels = 256                    # No of gray levels which assigned to an variable

for i in range(2):
    for j in range(4):

        im_mod = np.array(((im // (256//levels)) * (256//levels)), dtype=np.uint8)
        
        axarr[i,j].imshow(im_mod)
        axarr[i, j].set_title('{} intensity levels'.format(int(levels)))
        
        levels //= 2            # Reducing gray levels in 2**n where n is from 8 to 1 at each iteration

plt.tight_layout()              # Adjusting subplots to fit into the figure area
plt.show()                      # Display all the plots

