# -*- coding: UTF-8 -*- 
"""Script para gerar QR Codes em png"""


import qrcode
from os import listdir, system

fn = input(">>>> Nome do arquivo:\t")

if fn == "exemplo":
    CONTENT = "QR Code exemplar"
else:
    CONTENT = input(">>>> Digite o conteúdo a ser inserido:\n")

qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

if "output" not in listdir():
    system("mkdir output")

qr.add_data('{}'.format(CONTENT))
qr.make(fit=True)
img = qr.make_image(fill_color="red", back_color="black")
img.save('./output/{}_freely.png'.format(fn), "PNG")
