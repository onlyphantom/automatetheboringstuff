import smtplib, os

em = os.environ.get('MAIL_USERNAME')
pw = os.environ.get('MAIL_PASSWORD')

# TLS (Transport Layer Security, 587) vs SSL (Secure Sockets Layer, 465)
with smtplib.SMTP('smtp.gmail.com', 587) as smtpObj:
    print(type(smtpObj))
    smtpObj.starttls()

    try:
        encry_conn = smtpObj.login(em, pw)
        assert encry_conn[0] == 235
    except smtplib.SMTPAuthenticationError:
        print("Username and Password not accepted.")

    smtpObj.sendmail('automation@algorit.ma', ['samuel@algorit.ma'], "Subject: Automation script Version 2.\nAn email was sent using this automation script.\n\nTesting (samuel).")
