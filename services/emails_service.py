import json
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendCode(receiver_mail, code, firstname):
    port = 465  # For SSL
    file = open('creds.json')
    creds = json.load(file)
    password = creds["password"]  # getpass.getpass("Type your password : ")
    sender_mail = creds["email"]
    subject = "verification mail"

    message = MIMEMultipart("alternative")
    message['Subject'] = subject
    message['From'] = sender_mail
    message['To'] = receiver_mail
    message["Bcc"] = receiver_mail  # Recommended for mass emails

    # Create the plain-text and HTML version of your message

    plain_text = """\
    hi,
    this message is for test,
    to send contract ntification"""
    html = """\
    <html>
        <body style='color: black;'>
            <h1>Hello """ + firstname +""", here's a code</h1><br>
            <p>retype this code in its place and verify your email</p>
            <a href='#'>""" + str(code) + """</a>
            <p>    </p>
        </body>
    </html>
    """

    # Turn these into plain/html MIMEText objects

    part1 = MIMEText(plain_text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first

    message.attach(part1)
    message.attach(part2)

    # Create a secure SSL context
    context = ssl.create_default_context()

    print('sending email!')
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_mail, password)
        server.sendmail(sender_mail, receiver_mail, message.as_string())
        print('email sent, please check your spam!')


def send_double_factor_code(receiver_mail, code, firstname):
    port = 465  # For SSL
    file = open('creds.json')
    creds = json.load(file)
    password = creds["password"]  # getpass.getpass("Type your password : ")
    sender_mail = creds["email"]
    subject = "verification mail"

    message = MIMEMultipart("alternative")
    message['Subject'] = subject
    message['From'] = sender_mail
    message['To'] = receiver_mail
    message["Bcc"] = receiver_mail  # Recommended for mass emails

    # Create the plain-text and HTML version of your message

    plain_text = """\
    hi,
    this message is for test,
    to send contract ntification"""
    html = """\
    <html>
        <body style='color: black;'>
            <h1>Hello """ + firstname +""", here's a code</h1><br>
            <p>retype this code in its place for double verification login</p>
            <a href='#'>""" + str(code) + """</a>
            <p>    </p>
        </body>
    </html>
    """

    # Turn these into plain/html MIMEText objects

    part1 = MIMEText(plain_text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first

    message.attach(part1)
    message.attach(part2)

    # Create a secure SSL context
    context = ssl.create_default_context()

    print('sending email!')
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_mail, password)
        server.sendmail(sender_mail, receiver_mail, message.as_string())
        print('email sent, please check your spam!')
