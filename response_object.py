import datetime


"""
    booking_type is one of:
      - sus        (SUS internal)
      - sci_club   (Science Club)
      - sci_int    (Science Students' Interest)
      - stu_int    (Students' Interest)
      - ext        (External Organization)

    areas is a list of:
      - 1F
      - 2F
      - 3F
      - MR (Meeting rooms)

    equip is a list of:
      - audio
      - mic
      - proj
      - spkrs

"""



class ResponseObject:


    def __init__(self, response):
        answers = response['answers']
        self.name = ""
        self.title = ""
        self.org = ""
        self.phone_number = ""
        self.email = ""
        self.booking_type = ""
        self.areas = []
        self.equip = []
        self.full_date = ''
        self.year = 0
        self.month = 0
        self.date = 0
        self.starttime = ''
        self.starthour = 0
        self.startmin = 0
        self.endtime = ''
        self.endhour = 0
        self.endmin = 0
        self.event_name = ""
        self.attendees = 0
        self.staff = 0
        self.sol = False
        self.start_datetime = None
        self.end_datetime = None


        for answer in answers:
            if answer['field']['id'] == "16489567":
                self.org = answer['text']
            if answer['field']['id'] == "16489580":
                self.name = answer['text']
            if answer['field']['id'] == "16506203":
                self.title = answer['text']
            if answer['field']['id'] == "16489683":
                self.phone_number = answer['text']
            if answer['field']['id'] == "16489769":
                self.email = answer['email']
            if answer['field']['id'] == "17103544":
                self.booking_type = answer['choice']['label']
            if answer['field']['id'] == "16489972":
                for x in answer['choices']['labels']:
                    self.areas.append(x)
            if answer['field']['id'] == "16490114":
                for x in answer['choices']['labels']:
                    self.equip.append(x)
            if answer['field']['id'] == "16490853":
                self.full_date = answer['date'][0:10]
                self.year = int(answer['date'][0:4])
                self.month = int(answer['date'][5:7])
                self.date = int(answer['date'][8:10])
            if answer['field']['id'] == "16491900":
                self.starttime = answer['text']
                if answer['text'][1] == ":":
                    try:
                        self.starthour = int(answer['text'][0])
                        self.startmin = int(answer['text'][2:])
                    except ValueError:
                        print("Invalid time given. Input is:" + answer['text'])
                        s_hour = input('Manually enter the hour: ')
                        s_min = input('Manually enter the minute: ')
                        self.starthour = int(s_hour)
                        self.startmin = int(s_min)
                else:
                    try:
                        self.starthour = int(answer['text'][0:2])
                        self.startmin = int(answer['text'][3:])
                    except ValueError:
                        print("Invalid time given. Input is:" + answer['text'])
                        s_hour = input('Manually enter the hour: ')
                        s_min = input('Manually enter the minute: ')
                        self.starthour = int(s_hour)
                        self.startmin = int(s_min)
            if answer['field']['id'] == "vxYT8dUKQZaO":
                self.endtime = answer['text']
                if answer['text'][1] == ":":
                    try:
                        self.endhour = int(answer['text'][0]) % 24
                        self.endmin = int(answer['text'][2:])
                    except ValueError:
                        print("Invalid time given. Input is:" + answer['text'])
                        s_hour = input('Manually enter the hour: ')
                        s_min = input('Manually enter the minute: ')
                        self.endhour = int(s_hour)
                        self.endtmin = int(s_min)
                else:
                    try:
                        self.endhour = int(answer['text'][0:2]) % 24
                        self.endmin = int(answer['text'][3:])
                    except ValueError:
                        print("Invalid time given. Input is:" + answer['text'])
                        s_hour = input('Manually enter the hour: ')
                        s_min = input('Manually enter the minute: ')
                        self.endhour = int(s_hour)
                        self.endmin = int(s_min)
            if answer['field']['id'] == "16491912":
                self.event_name = answer['text']
            if answer['field']['id'] == "16492707":
                self.attendees = answer['number']
            if answer['field']['id'] == "16492713":
                self.staff = answer['number']
            if answer['field']['id'] == "16492737":
                self.sol = answer['boolean']
            if answer['field']['id'] == "16506203":
                self.title = answer['text']
        self.start_datetime = datetime.datetime(self.year, self.month, self.date, hour=self.starthour, minute=self.startmin)
        if self.endhour < 7:
            self.end_datetime = datetime.datetime(self.year, self.month, self.date + 1, hour=self.endhour, minute=self.endmin)
        else:
            self.end_datetime = datetime.datetime(self.year, self.month, self.date, hour=self.endhour, minute=self.endmin)


        self.qa =	{
            "Name of Organization": self.org,
            "Name of Event Organizer": self.name,
            "Title/Position of Event Organizer": self.title,
            "Phone Number": self.phone_number,
            "Email Address": self.email,
            "Booking Type": self.booking_type,
            "Desired Booking Areas": self.areas,
            "A/V Equipment Required": self.equip,
            "Preferred Booking Date": self.full_date,
            "Start Time (including setup and cleanup)": self.starttime,
            "Finish Time (including setup and cleanup)": self.endtime,
            "Event Name": self.event_name,
            "Expected number of participants and attendees": self.attendees,
            "Number of event staff": self.staff,
            "Will alcohol be served?": self.sol,
        }


"""
        for answer in response.answers:
            if answer.question == "Name of Organization":
                self.org = answer.answer
            if answer.question == "Name of Event Organizer":
                self.name = answer.answer
            if answer.question == "Title/Position of Event Organizer":
                self.title = answer.answer
            if answer.question == "Phone Number":
                self.phone_number = answer.answer
            if answer.question == "Email Address":
                self.email = answer.answer
            if answer.question == "Booking Type":
                self.booking_type = answer.answer
            if answer.question == "Desired Booking Areas":
                self.areas.append(answer.answer)
            if answer.question == "A/V Equipment Required":
                self.equip.append(answer.answer)
            if answer.question == "Preferred Booking Date":
                self.year = int(answer.answer[0:4])
                self.month = int(answer.answer[5:7])
                self.date = int(answer.answer[8:])
            if answer.question == "Start Time (including setup and cleanup)":
                self.starttime = answer.answer
                if answer.answer[1] == ":":
                    try:
                        self.starthour = int(answer.answer[0])
                        self.startmin = int(answer.answer[2:])
                    except ValueError:
                        print("Invalid time given. Input is:" + answer.answer)
                        s_hour = input('Manually enter the hour: ')
                        s_min = input('Manually enter the minute: ')
                        self.starthour = int(s_hour)
                        self.startmin = int(s_min)
                else:
                    try:
                        self.starthour = int(answer.answer[0:2])
                        self.startmin = int(answer.answer[3:])
                    except ValueError:
                        print("Invalid time given. Input is:" + answer.answer)
                        s_hour = input('Manually enter the hour: ')
                        s_min = input('Manually enter the minute: ')
                        self.starthour = int(s_hour)
                        self.startmin = int(s_min)
            if answer.question == "Finish Time (including setup and cleanup)":
                self.endtime = answer.answer
                if answer.answer[1] == ":":
                    self.endhour = int(answer.answer[0])
                    self.endmin = int(answer.answer[2:])
                else:
                    self.endhour = int(answer.answer[0:2])
                    self.endmin = int(answer.answer[3:])
            if answer.question == "Event Name":
                self.event_name = answer.answer
            if answer.question == "Expected number of participants and attendees":
                self.attendees = answer.answer
            if answer.question == "Number of event staff":
                self.staff = int(answer.answer)
            if answer.question == "Will alcohol be served?":
                self.sol = bool(int(answer.answer))
        self.start_datetime = datetime.datetime(self.year, self.month, self.date, hour=self.starthour, minute=self.startmin)
        if self.endhour < 7:
            self.end_datetime = datetime.datetime(self.year, self.month, self.date + 1, hour=self.endhour, minute=self.endmin)
        else:
            self.end_datetime = datetime.datetime(self.year, self.month, self.date, hour=self.endhour, minute=self.endmin)
"""
