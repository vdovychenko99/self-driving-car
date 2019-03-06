import urllib
import urllib.request
import cv2
import numpy as np

url = 'http://192.168.1.12:8080/shot.jpg'



def streem(y,h,x,w):
    imgResp = urllib.request.urlopen(url)
    imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
    img = cv2.imdecode(imgNp, 0)
    frame = img[y:y + h, x:x + w] #cut image
    return frame

def streem1():
    imgResp = urllib.request.urlopen(url)
    imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
    img = cv2.imdecode(imgNp, -1)
    print("1")

    cv2.imwrite("firstttt_frame.jpg", img)
