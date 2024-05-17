import cv2

#Read image and it's formatted to grayscale.
img = cv2.imread('basics/assets/logo.png', 0)
cv2.imshow('Gray scale image',img)
cv2.waitKey(0) #0 waits infinitely until we press a key to close the window. 
cv2.destroyAllWindows()

#Read image without any formatting.
img = cv2.imread('basics/assets/logo.png', -1)
cv2.imshow('Normal image',img)
cv2.waitKey(0) #0 waits infinitely until we press a key to close the window. 
cv2.destroyAllWindows()

#Image resize
img = cv2.imread('basics/assets/logo.png', -1)
img = cv2.resize(img, (32, 32))
cv2.imshow('Resized image',img)
cv2.waitKey(0) #0 waits infinitely until we press a key to close the window. 
cv2.destroyAllWindows()

#Image resize by proportions
img = cv2.imread('basics/assets/logo.png', -1)
img = cv2.resize(img, (0, 0), fx=2, fy=0.5)
cv2.imshow('Resized image',img)
cv2.waitKey(0) #0 waits infinitely until we press a key to close the window. 
cv2.destroyAllWindows()

#Image rotate
img = cv2.imread('basics/assets/logo.png', -1)
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('Rotated image',img)
cv2.waitKey(0) #0 waits infinitely until we press a key to close the window. 
cv2.destroyAllWindows()

