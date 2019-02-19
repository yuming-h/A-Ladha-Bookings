import requests

# takes in responses and removes returns new list with unseen responses
def trim(data):
    log = open('log.txt', 'r+')
    # todo = open("todo.txt", "a+")
    ret = []
    log_string = log.read()
    for response in data['items']:
        if response['token'] not in log_string:
            ret.append(response)
    log.close()
    return ret

url = 'https://api.typeform.com/forms/E3lV6J/responses?since=2018-09-01T00%3A00%3A00'

head = {'authorization': 'bearer %TOKEN%'}

resp = requests.get(url=url, headers=head)
data = resp.json()

class Typeform:
    def __init__(self):
        self.ladha_responses = trim(data)
