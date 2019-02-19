
import my_typeforms
import invoice
import response_object
import event_calendar
import confirmation_email
import supervisor_email

def update_log(token):
    log = open('log.txt', 'a')
    log.write('{'+token+'}')
    log.close()

def approve(responses):
    for response in responses:
        responseObj = response_object.ResponseObject(response)
        for x in responseObj.qa:
            print(x+': '+str(responseObj.qa[x]))
        approval = input('Approve this booking? [y/n]: ')
        while (approval != "y" and approval != "n"):
            approval = input('That is not a valid option. Approve this booking? [y/n]: ')
        if (approval == "y"):
            supervisor = input('Please assign an Event Supervisor: ')
            print("Generating invoice ...")
            inv = invoice.Invoice(responseObj, supervisor)
            inv_number = inv.generateInvoice()
            if (supervisor != 'none' or supervisor != 'None'):
                sup_email_in = input('Send an email to a building supervisor? [y/n]: ')
                while (sup_email_in != "y" and sup_email_in != "n"):
                    sup_email_in = input('That is not a valid option. [y/n]: ')
                if (sup_email_in == 'y'):
                    email_in = input("Please enter the supervisor's email: ")
                    email_obj = supervisor_email.SupervisorEmail(responseObj, inv_number, supervisor, email_in)
                    email_obj.send_confirmation()
            print("Invoice #"+str(inv_number)+" created. Updating Calendar ...")
            cal = event_calendar.EventCalendar(responseObj, supervisor)
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
        update_log(response['token'])
        input("Press Enter to view the next event.")


def main():
    form = my_typeforms.Typeform()
    approve(form.ladha_responses)




if __name__ == '__main__':
   main()

input("No requests left! Press Enter to exit.")
