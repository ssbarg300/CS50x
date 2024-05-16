# Generates a QR code
# https://github.com/lincolnloop/python-qrcode

import os
import qrcode

# Generate QR code
img = qrcode.make("https://www.facebook.com/hasbargati")

# Save as file
img.save("qr.png", "PNG")

# Open file
os.system("open qr.png")
