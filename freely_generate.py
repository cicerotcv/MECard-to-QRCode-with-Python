# -*- coding: UTF-8 -*- 
"""Script para gerar QR Codes em png"""

import qrcode
import qrcode.image.svg

fn = input(">>>> Nome do arquivo:\t")

if fn == "exemplo":
    CONTENT = "QR Code exemplar"
else:
    CONTENT = input(">>>> Digite o conteúdo a ser inserido")

qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data('{}'.format(CONTENT))
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save('{}_freely.png'.format(fn), "PNG")
