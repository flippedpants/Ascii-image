import cv2
import numpy as np
import colorama
from colorama import Fore

colorama.init()

img = cv2.imread('spiderman.jpeg')

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
        bright[x,y] = 0.21*r + 0.72*g + 0.07*b


chars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
length = len(chars)

choice = input("Do you want the image in badass matrix-green color?? (y/n): ")

green_text = (choice.lower() == 'y')

for x in range(h):
    for y in range(w):
        val = int(bright[x,y] // 3.93)
        if(green_text):
            print(Fore.GREEN +  chars[val], end="")
        else:
            print(chars[val], end="")
    print()