import cv2

def bin(img):
    blur = cv2.GaussianBlur(img, (5, 5), 0)
    ret1, th1 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return th1

