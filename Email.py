import os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage

#class correo():

def sendEmail(ruta, name):
    print('enviando email')
    # Send an HTML email with an embedded image and a plain text message for
    # email clients that don't want to display the HTML.
    # Define these once; use them twice!

    fromaddr = 'doorbellemail@gmail.com'
    toaddrs  = 'youremail@gmail.com'

    # Create the root message and fill in the from, to, and subject headers
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = 'Timbre inteligente'
    msgRoot['From'] = fromaddr
    msgRoot['To'] = toaddrs
    msgRoot.preamble = 'This is a multi-part message in MIME format.'

    # Encapsulate the plain and HTML versions of the message body in an
    # 'alternative' part, so message agents can decide which they want to display.
    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)

    msgText = MIMEText('Acaban de llamar a tu puerta')
    msgAlternative.attach(msgText)

    # We reference the image in the IMG SRC attribute by the ID we give it below
    msgText = MIMEText('<b>Acaban de llamar a tu puerta<br><img src="cid:image1">', 'html')
    msgAlternative.attach(msgText)

    # This example assumes the image is in the current directory
    fp = open(ruta + name, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

    # Define the image's ID as referenced above
    msgImage.add_header('Content-ID', '<image1>')
    msgRoot.attach(msgImage)

    # Send the email (this example assumes SMTP authentication is required)
    import smtplib
    username = 'doorbellemail@gmail.com'
    password = 'doorbell'
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msgRoot.as_string())
    server.quit()
    os.system('curl -d "devid=YOURIDDEVICE" http://api.pushingbox.com/pushingbox')
