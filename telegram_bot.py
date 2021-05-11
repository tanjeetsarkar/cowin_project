import requests
from cowin_test import CowinMessage
from auth_secret import Authentications
import Pincodes


def sendCowinMessage(pin):
    auth = Authentications()
    bot_chat_id = auth.get_chat_id()
    bot_token = auth.get_bot_token()
    a=CowinMessage(pin)
    bot_message = a.parse_raw_json()
    if bot_message:
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chat_id + \
                    '&parse_mode=Markdown&text=' + bot_message
        response = requests.get(send_text)
        return response.json()
    else:
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chat_id + \
                    '&parse_mode=Markdown&text=' + ' No Vaccine availability in PINCODE: ' +pin
        response = requests.get(send_text)
        return response.json()



if __name__ == "__main__":
    a = Pincodes.pincodes()
    for pins in a:
        output = sendCowinMessage(pins)
        if output:
            print(output)
