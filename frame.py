import cv2
from PIL import Image

i=0
count=0

def length(path):
    cap = cv2.VideoCapture(path)
    len= int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    return len

def frames(i,count,y,h,x,w,path):
    cap = cv2.VideoCapture(path)
    cap.set(cv2.CAP_PROP_POS_MSEC, i)
    # cap.set(cv2.CAP_PROP_POS_MSEC, 0)

    ret, frame = cap.read()
    img = frame[y:y + h, x:x + w] #cut image
    # rotate_img = rotate(img, 180) #rotate img if need
    cv2.imwrite("%d.jpg" % count, img)


def first_frame(path):
    cap = cv2.VideoCapture(path)
    cap.set(cv2.CAP_PROP_POS_MSEC, 0)
    ret, frame = cap.read()
    cv2.imwrite("first_frame.jpg", frame)

def bright(brightness, count):
    source = Image.open("/Users/viktor/PycharmProjects/binarization_ocy/%d.jpg" % count)
    result = Image.new('RGB', source.size)
    for x in range(source.size[0]):
        for y in range(source.size[1]):
            r, g, b = source.getpixel((x, y))
            red = int(r * brightness)
            red = min(255, max(0, red))
            green = int(g * brightness)
            green = min(255, max(0, green))
            blue = int(b * brightness)
            blue = min(255, max(0, blue))
            result.putpixel((x, y), (red, green, blue))
    result.save("%d.jpg" %count)
