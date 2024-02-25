import smtplib

gmail_user = 'w699767@gmail.com'  # Replace with your Gmail address
gmail_password = 'ngff oqoo kwst vpem'  # Replace with your app-specific password or Gmail password

sent_from = gmail_user
to = ['w699767@gmail.com']  # Replace with the recipient's email address
subject = 'SMTP Email Test'
body = 'This is a test email sent from Python.'

email_text = f"""\
From: {sent_from}
To: {", ".join(to)}
Subject: {subject}

{body}
"""

try:
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)  # Using SMTP_SSL with port 465
    smtp_server.ehlo()
    smtp_server.login(gmail_user, gmail_password)
    smtp_server.sendmail(sent_from, to, email_text)
    smtp_server.close()
    print("Email sent successfully!")
except Exception as e:
    print(f"Error sending email: {e}")