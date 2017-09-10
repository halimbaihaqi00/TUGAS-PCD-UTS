import cv2

image = cv2.imread('D:\UTS PCD\lawu.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('puncak lawu 2.jpg', gray)

