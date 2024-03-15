import cv2
import numpy as np
import matplotlib.pyplot as plt

# -----------------------Defining the function for reduce the image spatial resolution----------------------
def reduce_spatial_resolution(img_path, block_size):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    (h, w) = img.shape
    
    h = (h // block_size) * block_size
    w = (w // block_size) * block_size
    img = img[:h, :w]
    
    modified_images = []
    for y in range(0, h, block_size):
        for x in range(0, w, block_size):
            block = img[y:y+block_size, x:x+block_size]
            avg_val = np.mean(block).astype(np.uint8)
            img[y:y+block_size, x:x+block_size] = np.full((block_size, block_size), avg_val)
    return img

# ---------------------Calling to the function for reduce the image spatial resolution----------------------
reduced_images = []
for block_size in [3, 5, 7]:
    reduced_res_img = reduce_spatial_resolution('sample.jpeg', block_size)
    reduced_images.append(reduced_res_img)

# -----------------------------------Plotting all images in one plot----------------------------------------
for i, block_size in enumerate([3, 5, 7]):
    plt.subplot(1, 3, i + 1)
    plt.imshow(reduced_images[i], cmap='gray')
    plt.title(f'{block_size}x{block_size} Reduced Spatial Resolution')
   
plt.tight_layout()                          # Adjusting subplots
plt.show()                                  # Show the plot


