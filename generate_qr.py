"""
Generate a scannable QR code for the live website URL.

Usage:
    pip install "qrcode[pil]"
    python generate_qr.py https://<your-username>.github.io/isha-proposal/
"""

import sys
import qrcode
from qrcode.constants import ERROR_CORRECT_H

def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_qr.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    qr = qrcode.QRCode(error_correction=ERROR_CORRECT_H, box_size=12, border=4)
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="#e63950", back_color="white").convert("RGB")
    out_path = "qr_code.png"
    img.save(out_path)
    print(f"Saved {out_path} for: {url}")

if __name__ == "__main__":
    main()
