import smtplib

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Mail(object):
    def __init__(self, email_config):
        self.email = email_config["email"]
        self.password = email_config["password"]
        self.server = email_config["server"]
        self.port = email_config["port"]
        print(f"Logging to {self.server}:{self.port}")
        session = smtplib.SMTP(self.server, self.port)
        print(f"Calling ehlo")
        session.starttls()
        print(f"Calling login")
        session.login(self.email, self.password)
        self.session = session

    def send_message(self, subject, to, body, filename):
        # Create a multipart message and set headers
        message = MIMEMultipart()
        message["From"] = self.email
        message["To"] = to
        message["Subject"] = subject
        message["Bcc"] = ""
        # Add body to email
        message.attach(MIMEText(body, "plain"))
        print(f"tot: {to}")
        print(f"subject: {subject}")
        print(f"body: {body}")

        if filename is not None:
            # Open PDF file in binary mode
            with open(filename, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
            # Encode file in ASCII characters to send by email
            encoders.encode_base64(part)
            # Add header as key/value pair to attachment part
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {filename}",)
            # Add attachment to message and convert message to string
            message.attach(part)

        # Send e-mail
        print(f"Sending e-mail...")
        self.session.sendmail(self.email, to, message.as_string())

if __name__ == "__main__":
    req = {
        "email": "deepuprajapti5@gmail.com",
        "subject": "new e-mail from python",
        "body": "This is from dp",
    }

    email_config = {
        "server": "smtp.aol.com",
        "port": 587,
        "username": "bhagwaan9990@aol.com",
        "password": 'Checking@99',
        "email": "bhagwaan9990@aol.com",
    }
    m = Mail(email_config)
    if "pdf_file" in req:
        m.send_message(req["subject"], req["email"], req["body"], req["pdf_file"])
    else:
        m.send_message(req["subject"], req["email"], req["body"], None)
