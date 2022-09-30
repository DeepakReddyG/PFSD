import qrcode
data = "2100031817-DeepakReddyG"
qr = qrcode.QRCode(version=1,box_size=10,border=1)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color='red',back_color='white') 
img.save('KLU.png')
