import matplotlib.pyplot as plt

# 4 ways to read image
plt.figure(figsize=(10,10))

# scikit-image
plt.subplot(221)
from skimage import io
img = io.imread('lena.jpg')
plt.title('skimage',fontsize=20)
plt.imshow(img)

# opencv
plt.subplot(222)
import cv2
img = cv2.imread('lena.jpg')
img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.title('opencv',fontsize=20)
plt.imshow(img1)

# pillow
plt.subplot(223)
from PIL import Image
img = Image.open('lena.jpg')
plt.title('PIL',fontsize=20)
plt.imshow(img)

# matplotlib
plt.subplot(224)
import matplotlib.image as mpimg
img = mpimg.imread('lena.jpg')
plt.title('matplotlib',fontsize=20)
plt.imshow(img)

plt.show()
