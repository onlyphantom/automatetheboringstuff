import os
import imapclient
import datetime
import pyzmail

em = os.environ.get('MAIL_USERNAME')
pw = os.environ.get('MAIL_PASSWORD')
emsince = datetime.date(2020, 3, 11)

imapO = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapO.login(em, pw)
imapO.select_folder('INBOX', readonly=True)

UIDs = imapO.search([u'SINCE', emsince])
# UIDs is a list: [838, 839, 840, 841, 842]
print(f'Email since: {emsince.strftime("%A %d. %B %Y")}:', UIDs)

rawLastEm = imapO.fetch(UIDs[-1], ['INTERNALDATE', 'FLAGS', 'BODY[]'])
print("Last Email Dated:", rawLastEm[UIDs[-1]][b'INTERNALDATE'])
print("Last Email Seen Status:", str(rawLastEm[UIDs[-1]][b'FLAGS'][0], 'utf-8'))

rawSecLastEm = imapO.fetch(UIDs[-2], ['INTERNALDATE', 'FLAGS', 'BODY[]'])
msg = pyzmail.PyzMessage.factory(rawSecLastEm[UIDs[-2]][b'BODY[]'])
print("Subject:", msg.get_subject())
print("Sender:", msg.get_addresses('from'), 
    "\nRecipient:", msg.get_addresses('to'),
    "\nCC:", msg.get_addresses('cc'),
    "\nBCC:", msg.get_addresses('bcc'),
    "\nNon-empty Text Message:", msg.text_part is not None 
    )
print("msg.text_part.get_payload().decode(msg.text_part.charset)")
html = msg.html_part.get_payload().decode(msg.html_part.charset)
print(html[:150] + '...')
imapO.logout()