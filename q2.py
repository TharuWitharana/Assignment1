import cv2
import matplotlib.pyplot as plt

# -----------------------------------Load the image----------------------------------------
im = cv2.imread("sample.jpeg")

# ------------------------------Set up 3 images into 1 figure------------------------------
f, axarr = plt.subplots(1, 3)  

# ------------------------------Appliying spartial avaraging-------------------------------
kernels = [(3, 3), (10, 10), (20, 20)]
titles = ['3x3 kernel', '10x10 kernel', '20x20 kernel']

for i, (kernel, title) in enumerate(zip(kernels, titles)):

    blurred = cv2.blur(im, kernel)                              # Apply the blur using the current kernel size
    
    axarr[i].imshow(cv2.cvtColor(blurred, cv2.COLOR_BGR2RGB))   # Display the blurred image
    axarr[i].set_title(title)

plt.tight_layout()                                              # Adjusting subplots to fit into the figure area
plt.show()                                                      # Display the plot
