import qrcode

data = "Devops"

img = qrcode.make(data)

img.save("/home/wmt/Pictures/Example/1.png")