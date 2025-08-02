import smtplib
from email.message import EmailMessage
import mimetypes
import os

# Set up the email details
msg = EmailMessage()
msg['Subject'] = 'Daily Report 📊'
msg['From'] = 'your_email@gmail.com'  # Use your actual Gmail
msg['To'] = 'receiver_email@example.com'       # Recipient

msg.set_content(
    'Hello,\n\nYour daily report is attached.\n\n- Nova Coder Bot\n\nSubscribe to the channel! 🚀'
)

# Attach the file (BMW.jpg)
file_path = 'BMW.jpg'
if os.path.exists(file_path):
    with open(file_path, 'rb') as f:
        file_data = f.read()
        mime_type, _ = mimetypes.guess_type(file_path)
        maintype, subtype = mime_type.split('/')
        msg.add_attachment(file_data, maintype=maintype, subtype=subtype, filename=os.path.basename(file_path))
else:
    print("File not found:", file_path)

# Send the email using Gmail SMTP
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login('your_email@gmail.com', 'your_app_password')  # Use Gmail App Password
    smtp.send_message(msg)

print("email send successfully!!")
