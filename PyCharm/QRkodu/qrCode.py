import pyqrcode

url = input("URL GİRİNİZ: ")

qr_code = pyqrcode.create(url)
qr_code.svg('qrcode.svg',scale=5)