"""Script para gerar QR Codes em png"""

import qrcode
import qrcode.image.svg

fn = input(">>>> Nome do arquivo:\t")
if fn == "exemplo":
    N = "Forrest Gump"
    TEL = "+123 555 0135"
    EMAIL = "forrestgump@forrest.sa"
else:
    N = input(">>>> Nome:\t")
    TEL = input(">>>> Telefone:\t")
    EMAIL = input(">>>> Email:\t")
    

content = """MECARD:N:{0};TEL:{1};EMAIL:{2};;""".format(N,TEL, EMAIL)

qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data('{}'.format(content))
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save('{}.png'.format(fn), "PNG")
