#YASHWANTH_SAI_BATHINI
import numpy as np
from skimage import io, exposure
import matplotlib.pyplot as plt
#Load the image
bho_image = io.imread('BHO.jpg')
#Split the image into its color channels
red_channel = bho_image[:, :, 0]
green_channel = bho_image[:, :, 1]
blue_channel = bho_image[:, :, 2]
#Apply histogram equalization to each color channel
red_eq = exposure.equalize_hist(red_channel)
green_eq = exposure.equalize_hist(green_channel)
blue_eq = exposure.equalize_hist(blue_channel)
#Merge the equalized channels back into an image
bho_eq = np.stack((red_eq, green_eq, blue_eq), axis=-1)
#Display original and enhanced images
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))
axes[0].imshow(bho_image)
axes[0].set_title('Original Image')
axes[0].axis('off')
axes[1].imshow(bho_eq)
axes[1].set_title('Histogram Equalized Image')
axes[1].axis('off')
plt.tight_layout()
plt.show()
