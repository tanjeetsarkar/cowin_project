import requests
from datetime import date
from datetime import timedelta


class CowinMessage(object):
    def __init__(self,pincode):
        self.pin = pincode
        self.date1 = self.get_date()
        self.url = self.create_url()
        self.header = {'User-Agent':'PostmanRuntime/7.28.0'}
        self.output_string =''
        self.initial_string = "Vaccination Availability for pin "+ self.pin+ " on "+ self.date1+ " : \n"
        self.raw_json = self.get_json_raw()

    def get_json_raw(self):
        response = requests.get(self.url, headers = self.header)
        if response.status_code == 200:
            raw_json = response.json()
            return raw_json
        return False


    def parse_raw_json(self):
        self.output_string += self.initial_string
        if self.raw_json:
            for centers in self.raw_json['centers']:
                self.output_string += "Hospital Name: "+ centers['name']+ "\n"
                for sessions in centers['sessions']:
                    self.output_string+="Availability: "+ str(sessions['available_capacity']) + "\n"
                    self.output_string+= "Vaccine: "+ sessions['vaccine'] + "\n"
                    self.output_string += "Min Age Limit: " + str(sessions['min_age_limit'])+ "\n"
            if self.output_string == self.initial_string:
                return False
            return self.output_string


    def get_date(self):
        delay = timedelta(days=1)
        today = date.today()
        tomorrow = today + delay
        date_format = tomorrow.strftime("%d-%m-%Y")
        return date_format


    # def get_pincode(self):
    #     pin = '743145'
    #     return pin


    def create_url(self):
        required_date = self.get_date()
        required_url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=' +self.pin \
                       +'&date=' + required_date
        return required_url

# a= CowinMessage('847211')
# print(a.parse_raw_json())
# b= CowinMessage('743193')
# print(b.parse_raw_json())