import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('coins.JPG',0)
img2 = img.copy()
template = cv2.imread('1euro.JPG',0)
img3 = template.copy()
w, h = template.shape[::-1]

# Apply template Matching
res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
cv2.rectangle(img,top_left, bottom_right, (0,255,255), 50)

plt.subplot(221),plt.imshow(img2)
plt.title('Original Picture')
plt.subplot(222),plt.imshow(img3)
plt.title('Template')
plt.subplot(223),plt.imshow(img)
plt.title('Detect 1 euro coin')
plt.suptitle('Template matching using TM_CCOEFF method')

plt.show()
