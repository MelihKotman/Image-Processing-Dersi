import cv2

img = cv2.imread("images/belge.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, binary = cv2.threshold(
    img, 127, 255,
    cv2.THRESH_BINARY
)

cv2.imshow("Binary", binary)
cv2.waitKey(0)


_, otsu = cv2.threshold(
    gray, 0, 255,
    cv2.THRESH_BINARY + cv2.THRESH_OTSU
)

cv2.imshow("Otsu", otsu)
cv2.waitKey(0)

cv2.destroyAllWindows()