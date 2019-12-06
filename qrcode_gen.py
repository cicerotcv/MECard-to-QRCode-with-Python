# -*- coding: UTF-8 -*- 
"""Script para gerar QR Codes em png"""

import qrcode
import qrcode.image.svg
import time

class persona():
    def __init__(self, name="Forrest Gump", phone="+123 555 0135", email="forrestgump@forrest.sa"):
        self.name = name
        self.phone = phone
        self.email = email
    def dictionarizer(self):
        return {
            "Nome":self.name,
            "Telefone": self.phone,
            "Email":self.email,
            }

fn = input(">>>> Nome do arquivo:\t")

if fn == "exemplo":
    data = persona()
else:
    N = input(">>>> Nome:\t\t")
    TEL = input(">>>> Telefone:\t")
    EMAIL = input(">>>> Email:\t\t")
    data = persona(name=N, phone=TEL, email=EMAIL)
    

print("\nNome:\t{0}\nTelefone:\t{1}\nEmail:\t{2}\n".format(data.name, data.phone, data.email))

content = "MECARD:N:{0};TEL:{1};EMAIL:{2};;".format(data.name, data.phone, data.email)

qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)


qr.add_data('{}'.format(content))
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save('{}_gen.png'.format(fn), "PNG")
