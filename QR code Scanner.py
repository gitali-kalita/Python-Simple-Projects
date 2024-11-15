import qrcode

# Taking UPI ID as input
upi_id = input("Enter your UPI ID: ")

# Defining the payment URL based on the UPI ID and the payment app
phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

# Create QR Codes for each payment app
phonepe_qr = qrcode.make(phonepe_url)
google_pay_qr = qrcode.make(google_pay_url)
paytm_qr = qrcode.make(paytm_url)

# Save the QR Codes to image file (optional)
phonepe_qr.save('phonepe_qr.png')
google_pay_qr.save('google_pay_qr.png')
paytm_qr.save('paytm_qr.png')

# Display the QR Codes (install PIL/Pillow Library)
phonepe_qr.show()
google_pay_qr.show()
paytm_qr.show()
