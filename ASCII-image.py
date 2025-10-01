import cv2
import numpy as np

img = cv2.imread('spiderman.jpg')
cv2.imshow('spiderman',img)
cv2.waitKey(0)

print(img.shape)

h, w = img.shape[:2]
print(f'height {h} and width {w}')

# ratio = 500 / w
# large = (500 , int(ratio*h))
# resize = cv2.resize(img, large)

# # print(img.shape)
# # cv2.imshow('resized', resize)

bright = np.zeros((h,w))
for x in range(h):
    for y in range(w):
        (b,g,r) = img[x][y].astype(np.int32)
        bright[x,y] = (b+g+r)/3 

# print(img)

chars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
length = len(chars)

for x in range(h):
    for y in range(w):
        val = int(bright[x,y] // 3.93)
        print(chars[val], end="")
    print()
