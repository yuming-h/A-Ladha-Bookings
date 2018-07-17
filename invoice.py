import os
from pylatex import Document, PageStyle, Head, Foot, Section, Subsection, Tabular, Math, TikZ, Axis, \
    Plot, Figure, Matrix, Alignat, StandAloneGraphic, MiniPage, Command
from pylatex.utils import italic, bold, NoEscape
import response_object
import datetime


def getInvNum():
    dir = os.path.join(os.path.dirname(__file__), 'Invoices\\nums.txt')
    inv_log = open(dir, "r+")
    ret = 0
    for line in inv_log:
        if (line != ''):
            ret = int(line)
    ret = ret + 1
    inv_log.write(str(ret) + "\n")
    return ret

def getBookingSpaces(areas):
    ret = ''
    for a in areas:
        ret = ret + a + ', '
    return ret[:-2]

def unit_cost(booking_type, areas):
    if booking_type in 'SUS Groups (Committees)':
        if 'Main Floor (2F)' in areas:
            return 0
        elif 'Mezzanine (3F)' in areas:
            return 0
        elif 'Front Porch' in areas:
            return 0
        else:
             return 0
    if booking_type in 'Science Departmental/Non-Departmental Club':
        if 'Main Floor (2F)' in areas:
            return 0
        elif 'Mezzanine (3F)' in areas:
            return 0
        elif 'Front Porch' in areas:
            return 0
        else:
            return 0
    if booking_type in 'Internal Organization (UBC - Science-Affiliated)':
        if 'Main Floor (2F)' in areas:
            return 0
        elif 'Mezzanine (3F)' in areas:
            return 0
        elif 'Front Porch' in areas:
            return 0
        else:
            return 0
    if booking_type in 'Internal Organization (UBC - Non-Science Affiliated)':
        if 'Main Floor (2F)' in areas:
            return 30
        elif 'Mezzanine (3F)' in areas:
            return 20
        elif 'Front Porch' in areas:
            return 15
        else:
            return 0
    else:
        if 'Main Floor (2F)' in areas:
            return 70
        elif 'Mezzanine (3F)' in areas:
            return 40
        elif 'Front Porch' in areas:
            return 40
        else:
            return 0

def quantity(start, finish):
    fin = finish.hour + (finish.minute / 60 )
    sta = start.hour + (start.minute / 60)
    return round(abs(fin - sta), 2)

def calculate_cost(unit_cost, quantity):
    return unit_cost * quantity

def av_cost(booking_type):
    if booking_type in 'SUS Groups (Committees)':
        return 0
    if booking_type in 'Science Departmental/Non-Departmental Club':
        return 0
    if booking_type in 'Internal Organization (UBC - Science-Affiliated)':
        return 0
    if booking_type in 'Internal Organization (UBC - Non-Science Affiliated)':
        return 20
    else:
        return 25

def spkr_cost(booking_type):
    if booking_type in 'SUS Groups (Committees)':
        return 0
    if booking_type in 'Science Departmental/Non-Departmental Club':
        return 20
    if booking_type in 'Internal Organization (UBC - Science-Affiliated)':
        return 30
    if booking_type in 'Internal Organization (UBC - Non-Science Affiliated)':
        return 30
    else:
        return 30

def extra_hours(end_datetime):
    calc = (end_datetime.hour + (end_datetime.minute / 60)) - 16
    return round(calc, 2)

class Invoice:

    def __init__(self, responseObj):
        self.response = responseObj

    def generateInvoice(self):
        image_filename = os.path.join(os.path.dirname(__file__), 'Invoices\sus_header.png')
        geometry_options = {"tmargin": "1cm", "lmargin": "1.5cm"}
        doc = Document(geometry_options=geometry_options)
        inv_number = getInvNum()
        now = datetime.datetime.now()
        event_date = self.response.start_datetime


        doc.append(Command('noindent'))
        with doc.create(Figure(position='h!')) as sus_pic:
            sus_pic.add_image(image_filename, width='550px')
        doc.append(Command('textbf', ' '))
        doc.append(Command('newline'))
        doc.append(Command('textbf', 'Abdul Ladha Science Student Centre Invoice No. '+str(inv_number)))
        doc.append(Command('newline'))
        doc.append(Command('textbf', 'Date issued: '))
        doc.append(str(now.month)+'-'+str(now.day)+'-'+str(now.year))
        doc.append(Command('newline'))
        doc.append(Command('textbf','Purpose: '))
        doc.append(self.response.event_name + " on " +
            str(event_date.month)+'-'+str(event_date.day)+'-'+str(event_date.year))
        doc.append(Command('newline'))
        doc.append(Command('textbf','Bill to: '))
        doc.append(self.response.name + ', '+ self.response.org)
        doc.append(Command('newline'))
        doc.append(Command('newline'))
        doc.append(Command('textbf', 'Booking Fees: ' + self.response.booking_type))
        doc.append(Command('newline'))
        with doc.create(Tabular('|r|c|c|l|')) as table:
            areas = getBookingSpaces(self.response.areas)
            uc = unit_cost(self.response.booking_type, self.response.areas)
            qn = quantity(self.response.start_datetime, self.response.end_datetime)
            booking_cost = calculate_cost(uc, qn)
            av = av_cost(self.response.booking_type)
            spkr = spkr_cost(self.response.booking_type)
            num_extra_hours = extra_hours(self.response.end_datetime)
            weekend_hours = wknd_hours(self.response)
            cost = 0


            table.add_hline()
            table.add_row(("Description", "Unit Price", "Quantity", "Amount"))
            table.add_hline()
            table.add_row(areas, uc, qn, booking_cost)
            table.add_hline()
            cost = cost + booking_cost
            if 'Audio System' in self.response.equip:
                table.add_row('Audio System', av, 1, av)
                table.add_hline()
                cost = cost + av
            if '550W Speakers' in self.response.equip:
                table.add_row('550W Speakers', spkr, 1, spkr)
                table.add_hline()
                cost = cost + spkr
            if self.response.end_datetime.hour >= 16:
                table.add_row('After 8PM Fees', 25, num_extra_hours, 25 * num_extra_hours)
                table.add_hline()
            if
            table.add_row('','','','Balance Due:', '$'+str(cost))
        doc.generate_pdf('test', clean_tex=False, compiler='pdflatex') # CHANGE NAME LATER

        return inv_number
