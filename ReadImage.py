# 4 ways to read image and grayscale image
import matplotlib.pyplot as plt

##### RGB image #####
plt.figure(figsize=(6,6))

# scikit-image
plt.subplot(221)
from skimage import io
img = io.imread('lena.jpg')
plt.title('skimage',fontsize=10)
plt.imshow(img)

# opencv
plt.subplot(222)
import cv2
bgr = cv2.imread('lena.jpg')
img = cv2.cvtColor(bgr,cv2.COLOR_BGR2RGB)
plt.title('opencv',fontsize=10)
plt.imshow(img)

# pillow
plt.subplot(223)
from PIL import Image
img = Image.open('lena.jpg')
plt.title('PIL',fontsize=10)
plt.imshow(img)

# matplotlib
plt.subplot(224)
import matplotlib.image as mpimg
img = mpimg.imread('lena.jpg')
plt.title('matplotlib',fontsize=10)
plt.imshow(img,cmap = plt.get_cmap('gray'))


##### grayscale image #####
plt.figure(figsize=(6,6))

# scikit-image
plt.subplot(221)
from skimage import io
img = io.imread('lena.jpg',as_gray=True)
plt.title('skimage',fontsize=10)
plt.imshow(img)

# opencv
plt.subplot(222)
import cv2
img = cv2.imread('lena.jpg',cv2.IMREAD_GRAYSCALE)
plt.title('opencv',fontsize=10)
plt.imshow(img)

# pillow
plt.subplot(223)
from PIL import Image
img = Image.open('lena.jpg').convert('L')
plt.title('PIL',fontsize=10)
plt.imshow(img)

# matplotlib
plt.subplot(224)
import matplotlib.image as mpimg
rgb = mpimg.imread('lena.jpg')
r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
img = 0.2989 * r + 0.5870 * g + 0.1140 * b
plt.title('matplotlib',fontsize=10)
plt.imshow(img)

plt.show()
