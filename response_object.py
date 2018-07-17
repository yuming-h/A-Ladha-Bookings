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
        self.name = ""
        self.org = ""
        self.phone_number = ""
        self.email = ""
        self.booking_type = ""
        self.areas = []
        self.equip = []
        self.year = 0
        self.month = 0
        self.date = 0
        self.starthour = 0
        self.startmin = 0
        self.endhour = 0
        self.endmin = 0
        self.event_name = ""
        self.attendees = 0
        self.staff = 0
        self.sol = False
        self.start_datetime = None
        self.end_datetime = None
        self.date = ""

        for answer in response.answers:
            if answer.question == "Name of Organization":
                self.org = answer.answer
            if answer.question == "Name of Event Organizer":
                self.name == answer.answer
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
                self.staff == int(answer.answer)
            if answer.question == "Will alcohol be served?":
                self.sol == bool(int(answer.answer))
        self.start_datetime = datetime.datetime(self.year, self.month, self.date, hour=self.starthour, minute=self.startmin)
        if self.endhour < 7:
            self.end_datetime = datetime.datetime(self.year, self.month, self.date + 1, hour=self.endhour, minute=self.endmin)
        else:
            self.end_datetime = datetime.datetime(self.year, self.month, self.date, hour=self.endhour, minute=self.endmin)
