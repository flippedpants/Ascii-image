import cv2
import numpy as np
import colorama
from colorama import Fore

colorama.init()

def captureImage():
    print("When the preview appears press the key 'c' on your keybord to capture the image")

    capture = cv2.VideoCapture(0)

    while True:
        ret, frame = capture.read()
        frame = cv2.flip(frame, 1)

        cv2.imshow("Preview", frame)
        h,w = frame.shape[:2]

        key = cv2.waitKey(1)
        
        if key == ord('c'):
            capture.release()
            cv2.destroyAllWindows()
            
            resized_frame = resize(frame)
            
            return resized_frame

def makeBrightnessMatrix(img):
    h, w = img.shape[:2]
    bright = np.zeros((h,w))
    for x in range(h):
        for y in range(w):
            (b,g,r) = img[x][y].astype(np.int32)
            bright[x,y] = 0.114 * b + 0.587 * g + 0.299 * r
    return bright

def printAscii(bright):
    chars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    h, w = bright.shape[:2]
    choice = input("Do you want the image in badass matrix-green color?? (y/n): ")

    green_text = (choice.lower() == 'y')

    for x in range(h):
        for y in range(w):
            val = int(bright[x, y] // 3.93)
            if green_text:
                print(Fore.GREEN + chars[val], end="")
            else:
                print(chars[val], end="")
        print()

# def resize(img):
#     h,w = img.shape[:2]

#     if (w<700):
#         scale_factor = 1
#     elif (w >= 700 and w <= 1400):
#         scale_factor = 0.6
#     elif (w > 1400 and w<= 2000):
#         scale_factor = 0.4
#     else:
#         scale_factor = 0.25

#     new_width = int(w*scale_factor)
#     aspect_ratio = h/w
#     new_height = int(aspect_ratio * new_width * 0.6)
#     resized_img = cv2.resize(img , (new_width, new_height))

#     return resized_img

def resize(img, term_rows=220, term_cols=940):
    h, w = img.shape[:2]

    # ASCII characters are ~1.9 times taller than wide → correction factor
    ascii_factor = 0.55

    # Terminal max dimensions
    max_w = term_cols
    max_h = int(term_rows / ascii_factor)

    # Compute scale so image fits
    scale_w = max_w / w
    scale_h = max_h / h
    scale = min(scale_w, scale_h)

    # Do NOT upscale small images
    if scale > 1:
        scale = 1

    new_w = int(w * scale)
    new_h = int(h * scale * ascii_factor)

    resized = cv2.resize(img, (new_w, new_h))
    return resized


def main():

    print("Do you want to capture image from webcam?? (y/n): ")
    choice = input().lower()

    while choice not in ['y', 'n']:
        print("Invalid input. Please enter 'y' or 'n': ")
        choice = input().lower()
    
    if choice == 'y':
        resized_frame = captureImage()
        bright = makeBrightnessMatrix(resized_frame)
        printAscii(bright)
    else:
        path = input("Enter the path of the image: ")
        try:
            img = cv2.imread(path)
            if img is None:
                raise ValueError("Image not found or unable to load.")
            resized_image = resize(img)
            bright = makeBrightnessMatrix(resized_image)
            printAscii(bright)
        except Exception as e:
            print(f"Error: {e}. Please check the file path and try again.")

if __name__ == "__main__":
    main()