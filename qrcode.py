import qrcode

features = qrcode.QRCode(version=1, box_size=20, border=2)
features.add_data("https://www.google.com/")
features.make(fit=True)

generate_image = features.make_image(fill_color="black", back_color="white")
generate_image.save('image.png')
