import time
import serial
from resolution import get_resolution
from stream import streem, streem1
from binar import bin
from vec import angle
from signal import sig
start_time = time.time()

path='/Users/viktor/PycharmProjects/binarization_ocy/firstttt_frame.jpg' #path to foirst frame
img = streem1()
resolution=get_resolution(path)
width=resolution[0]
height=resolution[1]
# y=int(height/2)
y=int(height/2)
x=0
count=0
i=0
yy=y/4
y0 =0
y1=y0+yy
y2=y1+yy
y3=y2+yy
y4=y-1
xdef=10   #the default vector
ydef=10



while True:
    img=streem(y,height,x,width)
    bin_image = bin(img)
    mas=angle(bin_image, y0, y1, y2, y3, y4, xdef, ydef, width, y, yy)
    a=sig(mas)
    ser = serial.Serial('/dev/cu.usbserial-143110', 9600)
    if a==0:
        ser.write(b'g')
    elif a==-1:
        ser.write(b'a')
    elif a==-2:
        ser.write(b's')
    elif a==1:
        ser.write(b'd')
    elif a==2:
        ser.write(b'q')
    else:
        ser.write(b'e')


