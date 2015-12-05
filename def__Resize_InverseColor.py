import cv2


image=cv2.imread('number11.png',0)

height,width = image.shape

img2 = image.copy()

for i in range(height):
    for j in range(width):
        img2[i,j] = (255-image[i,j])


cv2.imshow('image',img2)
cv2.waitKey(0)

res=cv2.resize(img2,(28,28),interpolation=cv2.INTER_CUBIC)

cv2.imshow('black',res)
cv2.waitKey(0)

cv2.imwrite("black.bmp", res)

