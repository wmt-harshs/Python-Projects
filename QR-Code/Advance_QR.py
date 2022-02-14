import qrcode

data = "Devops"

qr = qrcode.QRCode(box_size=15,version=1,border=7)

qr.add_data(data)

qr.make(fit=True)

img=qr.make_image(fill_color = 'blue', back_color = 'white')

img.save("/home/wmt/Pictures/Example/2.png")
