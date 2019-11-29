import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import OP

mail_content = '''Hej,
Jeg kunne godt tænke mig en Praktikplads hos jer.
'''

# Din Email og kode ord og den som skal modtage din email
sender_address = OP.EMAIL_USER
sender_pass = OP.EMAIL_PASS
receiver_address = "Receiver-email" #the receiver email here
# Setup MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'Praktikplads'
# Subject lillen
#body og den fil du skal sende
message.attach(MIMEText(mail_content, 'Plain'))
attach_file_name = 'ansøning - cv - Mikkel Kronborg.pdf'
attach_file = open(attach_file_name, 'rb')
payload = MIMEBase('application', 'octate-stream')
payload.set_payload((attach_file).read())
encoders.encode_base64(payload)

payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
message.attach(payload)

session = smtplib.SMTP('smtp.gmail.com', 587)
session.ehlo()
session.starttls()
session.ehlo()
session.login(sender_address, sender_pass)
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()


print("Email send!")