import matplotlib.pyplot as plt
plt.figure(figsize=(15,5))

# scikit-image
plt.subplot(131)
from skimage import io
img=io.imread('lena.jpg',as_gray=True)
plt.title('skimage',fontsize=20)
plt.imshow(img)

# opencv
plt.subplot(132)
import cv2
img=cv2.imread('lena.jpg',cv2.IMREAD_GRAYSCALE)
plt.title('opencv',fontsize=20)
plt.imshow(img)

# pillow
plt.subplot(133)
from PIL import Image
import numpy as np
img = Image.open('lena.jpg').convert('L')
plt.title('PIL',fontsize=20)
plt.imshow(arr)

plt.show()
