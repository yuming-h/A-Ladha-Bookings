import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


class SupervisorEmail:

    def __init__(self, responseObj, inv_number, sup_name, sup_email):
        self.response = responseObj
        self.number = inv_number
        self.sup_name = sup_name
        self.sup_email = sup_email

    def send_confirmation(self):
        my_email = 'bmanager.bookings@sus.ubc.ca'
        PASSWORD = '98B#j5kxsusp'
        send_to = self.sup_email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(my_email, PASSWORD)
        event_date = self.response.start_datetime

        msg = MIMEMultipart()
        msg['From'] = my_email
        msg['To'] = send_to
        msg['Subject'] = 'Building Supervisor Assignment #'+ str(self.number)



        body = """\
            <div class="gmail_default">Hi,</div>
            <div class="gmail_default">
            <div class="gmail_default">
            <div class="gmail_default"><span style="font-family: arial, helvetica, sans-serif;"><br class="m_2402527658822516095gmail-m_7253113899711740381gmail-m_-1633789672313093095gmail-Apple-interchange-newline" />You have been assigned to the supervision of the ALSSC for&nbsp;the following date:&nbsp;</span></div>
            <div class="gmail_default"><span style="font-family: arial, helvetica, sans-serif;">&nbsp;</span></div>
            <div class="gmail_default">
            <div class="gmail_default"><strong>Invoice #"""+str(self.number)+' '+self.response.event_name+""" --&nbsp;</strong><strong>"""+str(event_date.month)+'-'+str(event_date.day)+'-'+str(event_date.year)+' '+self.response.starttime + ' - ' + self.response.endtime+"""</strong></div>
            <div><strong>&nbsp;</strong></div>
            </div>
            <div class="gmail_default">
            <div class="gmail_default">
            <div class="gmail_default">
            <div class="gmail_default">
            <p>Please note that the booking time includes setup and cleanup&nbsp;&nbsp;and all furniture and equipment must be returned to their original locations.</p>
            <p>&nbsp;</p>
            <p>Please contact me if this email was sent by accident or if you can no longer make this date.</p>
            <div>&nbsp;</div>
            </div>
            </div>
            </div>
            </div>
            </div>
            <p>Best,</p>
            <p>YuMing He</p>
            <p><em>Building Manager, Bookings</em></p>
            <p><em>Science Undergraduate Society of UBC</em></p>
            </div>
            </div>
            """
        inv = 'Invoices/Invoice '+str(self.number)+'.pdf'
        inv_attachment = open(inv, 'rb')
        inv_part = MIMEBase('application', 'octet-stream')
        inv_part.set_payload(inv_attachment.read())
        encoders.encode_base64(inv_part)
        inv_part.add_header('Content-Disposition','attachment;filename= '+inv)

        msg.attach(inv_part)

        msg.attach(MIMEText(body, 'html'))
        text = msg.as_string()
        server.sendmail(my_email, send_to, text)

        server.quit()
