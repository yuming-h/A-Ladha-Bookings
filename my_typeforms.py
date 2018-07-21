import typeform

# takes in responses and removes returns new list with unseen responses
def trim(responses):
    log = open('log.txt', 'r+')
    # todo = open("todo.txt", "a+")
    ret = []
    log_string = log.read()
    for response in responses:
        if response._token not in log_string:
            ret.append(response)
    return ret

typeform_key = '24433f694165fa836b142cfd7cf6e0506b37956a'
ladha_form_id = 'E3lV6J'
porch_form_id = 'PsJZ2k'

ladha_form = typeform.Form(api_key=typeform_key, form_id=ladha_form_id)
porch_form = typeform.Form(api_key=typeform_key, form_id=porch_form_id)

ladha_responses = ladha_form.get_responses()
porch_responses = porch_form.get_responses()

class Typeform:
    def __init__(self):
        self.ladha_responses = trim(ladha_responses)








#    for response in ladha_responses:
    #    for answer in response.answers:
    #        print('{question}: {answer}'.format(question=answer.question,
    #        answer=answer.answer))
