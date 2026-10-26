import cv2 
import numpy as np
#import imutils
#import easyocr
#from matplotlib import pyplot as pl


"""photo = np.zeros((400, 400, 3), dtype='uint8')#soozdat photo
#photo[100:150 , 200:250] = 119, 201, 105 #BGR 
cv2.rectangle(photo, (200, 200), (100, 100), (255,0,0), thickness=3)
cv2.line(photo, (0, photo.shape[0]//2), (100, photo.shape[0]//2), (0,255,0), thickness=5)
cv2.circle(photo, (photo.shape[1]//2, photo.shape[0]//2),50, (0,0,255), thickness=7)
cv2.putText(photo,'I love you', (100,150), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,0), 1)
print(photo.shape)
cv2.imshow('Photo', photo)
cv2.waitKey(0)"""


"""img = cv2.imread('im.jpg')#photo
cv2.imshow('Dido', img)
cv2.waitKey(0)"""


"""cap = cv2.VideoCapture(0)#webcam
cap.set(3, 500)
cap.set(4, 300)

while True:
    s, img = cap.read()
    cv2.imshow('dido', img)

    if cv2.waitKey(10) & 0xFF == ord('q') :
        break"""


"""img = cv2.imread("im.jpg")
img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))#obvodka
img = cv2.GaussianBlur(img, (9,9), 0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.Canny(img, 150, 150)
k = np.ones((5,5), np.uint8)
img = cv2.dilate(img, k, iterations=1)

img = cv2.erode(img, k, iterations=1)

cv2.imshow('dido', img)
#[0:100, 0:150]
#print(img.shape)

cv2.waitKey(0)"""

"""cap = cv2.VideoCapture('j.mp4')

while True:
    success, img = cap.read()
    img = cv2.GaussianBlur(img, (9,9), 0)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.Canny(img, 40, 40)
    k = np.ones((5,5), np.uint8)
    img = cv2.dilate(img, k, iterations=1)

    img = cv2.erode(img, k, iterations=1)
    cv2.imshow('dido', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break"""

"""img = cv2.imread('im.jpg')
#img = cv2.flip(img, 1)
def r(img_e, an):
    h, w = img.shape[:2]
    p = (w // 2, h // 2)
    m = cv2.getRotationMatrix2D(p, an, 1)
    return cv2.warpAffine(img_e, m, (w,h))

#img = r(img, 90)

def t(img_e, x, y):
    m= np.float32([[1,0,x],[0,1,y]])
    return cv2.warpAffine(img_e, m, (img_e.shape[1], img_e.shape[0]))
img = t(img, 30,200)

cv2.imshow('dido', img)
cv2.waitKey(0)"""


"""img = cv2.imread('im.jpg')
new_img = np.zeros(img.shape,dtype='uint8')

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img, (5,5),0)
img = cv2.Canny(img, 100, 140)
con, h = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(new_img, con, -1, (0, 111, 140), 1)
cv2.imshow('dido', img)
cv2.waitKey(0)"""


"""img = cv2.imread('im.jpg')

img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
img = cv2.cvtColor(img, cv2.COLOR_LAB2BGR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
r, g, b = cv2.split(img)
img = cv2.merge([b,g,r])

cv2.imshow('dido', img)
cv2.waitKey(0)"""

"""p = cv2.imread('im.jpg')
img = np.zeros(p.shape[:2], dtype='uint8')
c = cv2.circle(img.copy(), (200, 300), 90, 255, -1)
s = cv2.rectangle(img.copy(), (25,25), (250,350), 255, -1)
img =  cv2.bitwise_and(p,p,mask=c)
#img =  cv2.bitwise_or(c,s)
#img =  cv2.bitwise_xor(c,s)
#img =  cv2.bitwise_not(c,s)

cv2.imshow('dido', img)
cv2.waitKey(0)"""


"""img = cv2.imread('people_2.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
f = cv2.CascadeClassifier('C:/Users/Int_1/Desktop/work/faces.xml')
r = f.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

for (x, y, w, h) in r:
    cv2.rectangle(img, (x, y), (x + w, y +h), (0,0,255), thickness=2)

cv2.imshow('didar', img)
cv2.waitKey(0)"""


"""img = cv2.imread('car.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

f = cv2.bilateralFilter(gray, 11, 15, 15)
e = cv2.Canny(f, 30, 200)

cn = cv2.findContours(e.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cn = imutils.grab_contours(cn)
cn = sorted(cn, key=cv2.contourArea, reverse=True)

p = None
for c in cn:
    ap = cv2.approxPolyDP(c, 10, True)
    if len(ap) == 4:
        p = ap
        break  

m = np.zeros(gray.shape, np.uint8)
n_img = cv2.drawContours(m, [p], 0, 255, -1)
b = cv2.bitwise_and(img, img, mask=m)

(x, y) = np.where(m == 255)
(x1, y1) = (np.min(x), np.min(y))
(x2, y2) = (np.max(x), np.max(y))
cr = gray[x1:x2, y1:y2]

t = easyocr.Reader(['en'])
t = t.readtext(cr)
print(t)
r = t[0][-2]
fin = cv2.putText(img, r, (x1-200, y2 + 160), cv2.FONT_HERSHEY_DUPLEX, 3, (0,0,255), 2)
fin = cv2.rectangle(img, (x1,x2), (y1,y2), (0,255,0), 2)

pl.imshow(cv2.cvtColor(fin , cv2.COLOR_BGR2RGB)) #b, cr
pl.show()"""



'''for i in range(3):
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        print(f"Камера {i} доступна")
        ret, frame = cap.read()
        if ret:
            cv2.imshow(f"Camera {i}", frame)
            cv2.waitKey(0)
        cap.release()
cv2.destroyAllWindows()'''
