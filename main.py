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
            
            resized_frame = cv2.resize(frame, (500, 150))
            h, w = resized_frame.shape[:2]
            
            return resized_frame

def makeBrightnessMatrix(img):
    h, w = img.shape[:2]
    bright = np.zeros((h,w))
    for x in range(h):
        for y in range(w):
            (b,g,r) = img[x][y].astype(np.int32)
            bright[x,y] = (b+g+r)/3 
    return bright

def printAscii(bright):
    chars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    h, w = bright.shape
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
            resized_image = cv2.resize(img, (200, 150))
            bright = makeBrightnessMatrix(resized_image)
            printAscii(bright)
        except Exception as e:
            print(f"Error: {e}. Please check the file path and try again.")

if __name__ == "__main__":
    main()