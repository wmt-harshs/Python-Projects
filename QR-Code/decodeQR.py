import cv2

gmi = cv2.QRCodeDetector()
revel,point,s_qr = gmi.detectAndDecode(cv2.imread("/home/wmt/Pictures/Example/2.png"))
print(revel)

