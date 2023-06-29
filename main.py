import cv2
import pyqrcode
from pyzbar.pyzbar import decode
import time
import webbrowser

# create a QR code
link = 'www.youtube.com'
url = pyqrcode.create(link)
url.png('youtubeqrcode.png')


# # read the QRCode from the folder(IMAGES)
# image = cv2.imread('youtubeqrcode.png')
# for code in decode(image):
#     print(code.type)
#     print(code.data.decode('utf-8'))

# read and scanning tht QR code from the webcam
cam = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()
while True:
    _,img=cam.read()
    data,one, _=detector.detectAndDecode(img)
    if data:
        a=data
        break
    cv2.imshow('QRCode',img)
    if cv2.waitKey(1)==ord('q'):
        break
b=webbrowser.open(str(a))
cam.release(a)
cv2.destroyAllWindows()

# cam = cv2.VideoCapture(0)
# # detector = cv2.QRCodeDetector()
# cam.set(3,640)
# cam.set(4,480)
# camera = True
# while camera == True:
#     success, frame = cam.read()
#
#     for i in decode(frame):
#         print(i.type)
#         print(i.code.data.decode('utf-8'))
#         time.sleep(6)
#
#     cv2.imshow("QRCode",frame)
#     cv2.waitKey(1)
#
# print('Completed')