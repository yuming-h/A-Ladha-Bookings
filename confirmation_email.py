import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


class ConfirmationEmail:

    def __init__(self, responseObj, inv_number):
        self.response = responseObj
        self.number = inv_number

    def send_confirmation(self):
        my_email = 'bmanager.bookings@sus.ubc.ca'
        PASSWORD = '98B#j5kxsusp'
        send_to = self.response.email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(my_email, PASSWORD)
        event_date = self.response.start_datetime

        msg = MIMEMultipart()
        msg['From'] = my_email
        msg['To'] = send_to
        msg['Subject'] = 'Abdul Ladha Science Student Centre Bookings Confirmation #'+ str(self.number)

        sol_body = """\
            <div class="gmail_default">Hi,</div>
            <div class="gmail_default">
            <div class="gmail_default">
            <div class="gmail_default"><span style="font-family: arial, helvetica, sans-serif;"><br class="m_2402527658822516095gmail-m_7253113899711740381gmail-m_-1633789672313093095gmail-Apple-interchange-newline" />Thank you for booking the ALSSC!&nbsp;Please find your attached invoice and booking summary. Your event is booked for&nbsp;the following date:&nbsp;</span></div>
            <div class="gmail_default"><span style="font-family: arial, helvetica, sans-serif;">&nbsp;</span></div>
            <div class="gmail_default">
            <div class="gmail_default"><strong>Invoice #"""+str(self.number)+' '+self.response.event_name+""" --&nbsp;</strong><strong>"""+str(event_date.month)+'-'+str(event_date.day)+'-'+str(event_date.year)+' '+self.response.starttime + ' - ' + self.response.endtime+"""</strong></div>
            <div><strong>&nbsp;</strong></div>
            </div>
            <div class="gmail_default">
            <div class="gmail_default">
            <div class="gmail_default">
            <div class="gmail_default">
            <p>Please note that the booking time includes setup and cleanup&nbsp;as managed by your organization,&nbsp;and all furniture and equipment must be returned to their original locations.<span style="color: #000000;">&nbsp;</span><span style="color: #000000;"><em>If the cleanup is not done properly, the deposit will be charged and you may risk losing booking privileges at the ALSSC in the future.</em></span>&nbsp;There will be an Event Supervisor present during the duration of your booking should you have any questions, concerns, or technical issues.&nbsp;</p>
            <p>&nbsp;</p>
            <p>In this email, I have attached the&nbsp;Premises&nbsp;Use and Services Agreement&nbsp;and&nbsp;Rental Terms and Conditions&nbsp;documents, which need to be signed and&nbsp;scanned&nbsp;back to me 2 weeks prior to the event date,&nbsp;via&nbsp;email. Your booking qualifies as an&nbsp;<strong>"""+self.response.booking_type+"""&nbsp;</strong>and the total rental fee is outlined in the attached invoice&nbsp;(excluding the Deposit).&nbsp;The building damage fee will be charged should any damages be made after the event.&nbsp;</p>
            <div>&nbsp;</div>
            </div>
            </div>
            </div>
            </div>
            </div>
            <div class="gmail_default">&nbsp;</div>
            <div class="gmail_default">
            <div>
            <div><strong><span style="color: #ff0000; font-family: arial, helvetica, sans-serif;">IMPORTANT INFORMATION FOR THE SPECIAL OCCASION LICENSE:</span></strong></div>
            <div>
            <div>
            <p class="m_2402527658822516095gmail-m_7253113899711740381gmail-m_-1633789672313093095gmail-m_1505282859486111962gmail-m_-4647395455452944211gmail-m_6066663527837815582m_1729839037095273898gmail-m_5787985094730057643gmail-MsoNormal"><span style="font-family: arial, helvetica, sans-serif;">As you will be serving alcohol at this event, you will be required to apply for a Special Occasion License (SOL). The following forms are attached in this email:</span></p>
            <ol>
            <li><span style="font-family: arial, helvetica, sans-serif;">ALSSC SOL -&nbsp;<em>Permission to Hold a Licensed Event</em></span></li>
            <li><span style="font-family: arial, helvetica, sans-serif;">UBC Scheduling Services -&nbsp;<em>Request for University permission to hold a function where alcohol will be served</em></span></li>
            <li><span style="font-family: arial, helvetica, sans-serif;">UBC Scheduling Services -&nbsp;<em>Event Safety and Emergency Response Plan</em>&nbsp;(The floor plans are attached as you will need them for this form if your event has more than 100 attendees.)</span></li>
            <li><span style="font-family: arial, helvetica, sans-serif;">Faculty of Science -&nbsp;<em>Organizer's Plan for an Event where Alcohol will be Served</em></span></li>
            </ol>
            </div>
            <div>
            <p class="m_2402527658822516095gmail-m_7253113899711740381gmail-m_-1633789672313093095gmail-m_1505282859486111962gmail-m_-4647395455452944211gmail-m_6066663527837815582m_1729839037095273898gmail-m_5787985094730057643gmail-MsoNormal"><span style="font-family: arial, helvetica, sans-serif;">Please be advised that, according to&nbsp;<strong>Appendix A: Security Regulations&nbsp;</strong>of the Building Regulations,&nbsp;a professional, private security company must be hired for the licensed event if there are 50 attendees or above. You are responsible for contacting Maluco Security Services, which has a contract with the Science Undergraduate Society, to arrange for security during this event; I have attached the document that outlines the costs and terms and conditions.&nbsp;</span></p>
            <p class="m_2402527658822516095gmail-m_7253113899711740381gmail-m_-1633789672313093095gmail-m_1505282859486111962gmail-m_-4647395455452944211gmail-m_6066663527837815582m_1729839037095273898gmail-m_5787985094730057643gmail-MsoNormal"><span style="font-family: arial, helvetica, sans-serif;">&nbsp;</span></p>
            <p class="m_2402527658822516095gmail-m_7253113899711740381gmail-m_-1633789672313093095gmail-m_1505282859486111962gmail-m_-4647395455452944211gmail-m_6066663527837815582m_1729839037095273898gmail-m_5787985094730057643gmail-MsoNormal"><span style="font-family: arial, helvetica, sans-serif;">A friendly reminder that the ALSSC&rsquo;s building capacity for special events is&nbsp;<strong>133 persons</strong>, including security personnel (applies to the second and third floors); this is prescribed by the Fire Marshall and must be followed. The Dean of Science&rsquo;s Office also requires implementation of a plan for serving ONE alcoholic drink per person per hour at your event. Suggestions to enforce this policy include (A) a ticketing system or (B) bracelet system (time of drink served written on the bracelet). If this event to open to all ages, then the mezzanine (3​​F)&nbsp;<u>must</u>&nbsp;be for 19+ only, while the Main Floor (2F) will be open to all ages.&nbsp;</span></p>
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

        reg_body = """\
            <div class="gmail_default">Hi,</div>
            <div class="gmail_default">
            <div class="gmail_default">
            <div class="gmail_default"><span style="font-family: arial, helvetica, sans-serif;"><br class="m_2402527658822516095gmail-m_7253113899711740381gmail-m_-1633789672313093095gmail-Apple-interchange-newline" />Thank you for booking the ALSSC!&nbsp;Please find your attached invoice and booking summary. Your event is booked for&nbsp;the following date:&nbsp;</span></div>
            <div class="gmail_default"><span style="font-family: arial, helvetica, sans-serif;">&nbsp;</span></div>
            <div class="gmail_default">
            <div class="gmail_default"><strong>Invoice #"""+str(self.number)+' '+self.response.event_name+""" --&nbsp;</strong><strong>"""+str(event_date.month)+'-'+str(event_date.day)+'-'+str(event_date.year)+' '+self.response.starttime + ' - ' + self.response.endtime+"""</strong></div>
            <div><strong>&nbsp;</strong></div>
            </div>
            <div class="gmail_default">
            <div class="gmail_default">
            <div class="gmail_default">
            <div class="gmail_default">
            <p>Please note that the booking time includes setup and cleanup&nbsp;as managed by your organization,&nbsp;and all furniture and equipment must be returned to their original locations.<span style="color: #000000;">&nbsp;</span><span style="color: #000000;"><em>If the cleanup is not done properly, a $100.00 deposit will be charged and you may risk losing booking privileges at the ALSSC in the future.</em></span>&nbsp;There will be an Event Supervisor present during the duration of your booking should you have any questions, concerns, or technical issues.&nbsp;</p>
            <p>&nbsp;</p>
            <p>In this email, I have attached the&nbsp;Premises&nbsp;Use and Services Agreement&nbsp;and&nbsp;Rental Terms and Conditions&nbsp;documents, which need to be signed and&nbsp;scanned&nbsp;back to me 2 weeks prior to the event date,&nbsp;via&nbsp;email. Your booking qualifies as an&nbsp;<strong>"""+self.response.booking_type+"""&nbsp;</strong>and the total rental fee is outlined in the attached invoice&nbsp;(excluding the Deposit).&nbsp;The building damage fee will be charged should any damages be made after the event.&nbsp;</p>
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

        booking_contract = 'booking_package/ALSSC Booking Contract.pdf'
        booking_contract_attachment = open(booking_contract, 'rb')
        booking_contract_part = MIMEBase('application', 'octet-stream')
        booking_contract_part.set_payload(booking_contract_attachment.read())
        encoders.encode_base64(booking_contract_part)
        booking_contract_part.add_header('Content-Disposition','attachment;filename= '+booking_contract)

        terms = 'booking_package/ALSSC Rental Terms Conditions.pdf'
        terms_attachment = open(terms, 'rb')
        terms_part = MIMEBase('application', 'octet-stream')
        terms_part.set_payload(terms_attachment.read())
        encoders.encode_base64(terms_part)
        terms_part.add_header('Content-Disposition','attachment;filename= '+terms)

        sol_permission = 'booking_package/SOL/A) ALSSC SOL Permission Form.pdf'
        sol_permission_attachment = open(sol_permission, 'rb')
        sol_permission_part = MIMEBase('application', 'octet-stream')
        sol_permission_part.set_payload(sol_permission_attachment.read())
        encoders.encode_base64(sol_permission_part)
        sol_permission_part.add_header('Content-Disposition','attachment;filename= '+sol_permission)

        sol_floor_plan = 'booking_package/SOL/ALSSC Complete Floor Plan.pdf'
        sol_floor_plan_attachment = open(sol_floor_plan, 'rb')
        sol_floor_plan_part = MIMEBase('application', 'octet-stream')
        sol_floor_plan_part.set_payload(sol_floor_plan_attachment.read())
        encoders.encode_base64(sol_floor_plan_part)
        sol_floor_plan_part.add_header('Content-Disposition','attachment;filename= '+sol_floor_plan)

        sol_app_procedure = 'booking_package/SOL/ALSSC SOL Application Procedure.pdf'
        sol_app_procedure_attachment = open(sol_app_procedure, 'rb')
        sol_app_procedure_part = MIMEBase('application', 'octet-stream')
        sol_app_procedure_part.set_payload(sol_app_procedure_attachment.read())
        encoders.encode_base64(sol_app_procedure_part)
        sol_app_procedure_part.add_header('Content-Disposition','attachment;filename= '+sol_app_procedure)

        sol_handbook = 'booking_package/SOL/ALSSC SOL Handbook.pdf'
        sol_handbook_attachment = open(sol_handbook, 'rb')
        sol_handbook_part = MIMEBase('application', 'octet-stream')
        sol_handbook_part.set_payload(sol_handbook_attachment.read())
        encoders.encode_base64(sol_handbook_part)
        sol_handbook_part.add_header('Content-Disposition','attachment;filename= '+sol_handbook)

        sol_req = 'booking_package/SOL/B) UBC SOL Request Form.pdf'
        sol_req_attachment = open(sol_req, 'rb')
        sol_req_part = MIMEBase('application', 'octet-stream')
        sol_req_part.set_payload(sol_req_attachment.read())
        encoders.encode_base64(sol_req_part)
        sol_req_part.add_header('Content-Disposition','attachment;filename= '+sol_req)

        sol_safety = 'booking_package/SOL/C) UBC SOL Safety and Emergency Response Plan.pdf'
        sol_safety_attachment = open(sol_safety, 'rb')
        sol_safety_part = MIMEBase('application', 'octet-stream')
        sol_safety_part.set_payload(sol_safety_attachment.read())
        encoders.encode_base64(sol_safety_part)
        sol_safety_part.add_header('Content-Disposition','attachment;filename= '+sol_safety)

        sol_plan = 'booking_package/SOL/D) ALSSC SOL Organizer Plan.pdf'
        sol_plan_attachment = open(sol_plan, 'rb')
        sol_plan_part = MIMEBase('application', 'octet-stream')
        sol_plan_part.set_payload(sol_plan_attachment.read())
        encoders.encode_base64(sol_plan_part)
        sol_plan_part.add_header('Content-Disposition','attachment;filename= '+sol_plan)

        sol_cleaning = 'booking_package/SOL/UBC Cleaning Expectations.pdf'
        sol_cleaning_attachment = open(sol_cleaning, 'rb')
        sol_cleaning_part = MIMEBase('application', 'octet-stream')
        sol_cleaning_part.set_payload(sol_cleaning_attachment.read())
        encoders.encode_base64(sol_cleaning_part)
        sol_cleaning_part.add_header('Content-Disposition','attachment;filename= '+sol_cleaning)


        msg.attach(inv_part)
        msg.attach(booking_contract_part)
        msg.attach(terms_part)

        if self.response.sol:
            msg.attach(MIMEText(sol_body, 'html'))
            msg.attach(sol_permission_part)
            msg.attach(sol_floor_plan_part)
            msg.attach(sol_app_procedure_part)
            msg.attach(sol_handbook_part)
            msg.attach(sol_req_part)
            msg.attach(sol_safety_part)
            msg.attach(sol_plan_part)
            msg.attach(sol_cleaning_part)
        else:
            msg.attach(MIMEText(reg_body, 'html'))
        text = msg.as_string()

        server.sendmail(my_email, send_to, text)

        server.quit()
