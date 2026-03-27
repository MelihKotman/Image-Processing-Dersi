import cv2
import numpy as np

img = cv2.imread('images/lena.jpg')
rows, cols = img.shape[:2]

# Yatay Shear (sh_x = 0.3)
M_shear_x = np.float32([
  [1, 0.3, 0],
  [0, 1,   0]])
sheared_x = cv2.warpAffine(img,
    M_shear_x, (cols+100, rows))

# Dikey Shear (sh_y = 0.2)
M_shear_y = np.float32([
  [1,   0, 0],
  [0.2, 1, 0]])
sheared_y = cv2.warpAffine(img,
    M_shear_y, (cols, rows+100))

cv2.imshow("Yatay kaykilma", sheared_y)
cv2.waitKey(0)

cv2.imshow("Dikey kaykilma", sheared_x)
cv2.waitKey(0)


cv2.destroyAllWindows()