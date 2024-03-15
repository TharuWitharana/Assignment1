import cv2
import matplotlib.pyplot as plt

# -----------------------------------------Loading the image-------------------------------------------
im = cv2.imread("sample.jpeg")

rows, cols = im.shape[:2]                                   # Get the dimensions of the image

# -----------------------------------Rotating for 45 degrees----------------------------------------
M_45 = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)
dst_45 = cv2.warpAffine(im, M_45, (cols, rows))

# -----------------------------------Rotating for 90 degrees----------------------------------------
M_90 = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)
dst_90 = cv2.warpAffine(im, M_90, (cols, rows))

# ----------------------------Plotting rotated images in one figure---------------------------------
f, axarr = plt.subplots(1, 2)

axarr[0].imshow(cv2.cvtColor(dst_45, cv2.COLOR_BGR2RGB))    # 45 degrees rotated image
axarr[0].set_title('45 deg rotation')

axarr[1].imshow(cv2.cvtColor(dst_90, cv2.COLOR_BGR2RGB))    # 90 degrees rotated image
axarr[1].set_title('90 deg rotation')

plt.tight_layout()                                          # Adjusting subplots
plt.show()                                                  # Show the plot

