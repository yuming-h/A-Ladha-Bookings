
import my_typeforms
import invoice

def generateInvoice(response):
    pass

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
            print(ok)
            sendEmail(reponse, generateInvoice(response))
            updateCalendar(reponse)
            generateInvoice(response)
        elif (approval == "n"):
            print(ok)
            sendRejectedEmail


def main():
    form = my_typeforms.Typeform()
    approve(form.ladha_responses)
    approve(form.porch_responses)




if __name__ == '__main__':

   main()

print("asdaasd")
input("Press enter to exit ;)")
