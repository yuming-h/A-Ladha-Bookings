
import my_typeforms
import invoice
import response_object
import calendar

def sendApprovedEmail(response):
    pass

def sendRejectedEmail(reponse):
    pass

def approve(responses):
    for response in responses:
        for answer in response.answers:
            print('{question}: {answer}'.format(question=answer.question,
            answer=answer.answer))
        approval = input('Approve this booking (y/n)?: ')
        while (approval != "y" and approval != "n"):
                approval = input('That is not a valid option. Approve this booking (y/n)?: ')
        if (approval == "y"):
            supervisor = input('Please assign an Event Supervisor: ')
            responseObj = response_object.ResponseObject(response)
            inv = invoice.Invoice(responseObj, supervisor)
            print("Generating invoice ...")
            inv_number = inv.generateInvoice()
            print("Invoice created. Updating Calendar ...")
            cal = calendar.Calendar(response)
        #    invoice.generateInvoice()
        #    sendEmail(reponse, generateInvoice(response))
        #    updateCalendar(reponse)
        #    generateInvoice(response)
        elif (approval == "n"):
            print("ok")



def main():
    form = my_typeforms.Typeform()
    approve(form.ladha_responses)
    approve(form.porch_responses)




if __name__ == '__main__':
   main()

input("All done! Press Enter to exit.")
