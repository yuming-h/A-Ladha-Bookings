
import my_typeforms
import invoice
import response_object
import event_calendar
import confirmation_email

def update_log(token):
    log = open('log.txt', 'a')
    log.write('{'+token+'}')
    log.close()

def approve(responses):
    for response in responses:
        for answer in response.answers:
            print('{question}: {answer}'.format(question=answer.question,
            answer=answer.answer))
        print('Response Token: '+response._token)
        approval = input('Approve this booking? [y/n]: ')
        while (approval != "y" and approval != "n"):
                approval = input('That is not a valid option. Approve this booking (y/n)?: ')
        if (approval == "y"):
            supervisor = input('Please assign an Event Supervisor: ')
            responseObj = response_object.ResponseObject(response)
            inv = invoice.Invoice(responseObj, supervisor)
            print("Generating invoice ...")
            inv_number = inv.generateInvoice()
            print("Invoice created. Updating Calendar ...")
            cal = event_calendar.EventCalendar(responseObj)
            try:
                cal.update_calendar()
            except CalledProcessError:
                print("PDF already open somewhere else? Close and try again.")
            email_input = input('Calendar updated. Send a confirmation email? [y/n]: ')
            while (email_input != "y" and email_input != "n"):
                    email_input = input('That is not a valid option. Approve this booking (y/n)?: ')
            if (email_input == 'y'):
                conf = confirmation_email.ConfirmationEmail(responseObj, inv_number)
                conf.send_confirmation()
                print("Email sent.")
        elif (approval == "n"):
            print("Approval denied.")
        update_log(response._token)
        input("Press Enter to view the next event.")


def main():
    form = my_typeforms.Typeform()
    approve(form.ladha_responses)




if __name__ == '__main__':
   main()

input("No requests left! Press Enter to exit.")
