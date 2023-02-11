import requests
from datetime import datetime 
import pandas as pd
import time
import os
from dotenv import load_dotenv
load_dotenv()

class Birthday:
    def __init__(self):
        url = 'http://127.0.0.1:5000/birthday'
        self.date = datetime.today().strftime("%-m%d")
        self.result = requests.get(url).json()
    
    def check_birthday(self):
        for i in range(len(self.result)):
            if str(self.result[i]['birthday'])==str(self.date):
                return self.result[i]['name']
    
    def line_notify(self):
        person = self.check_birthday()
        line_notify_token = os.getenv('TOKEN1')
        line_notify_api = 'https://notify-api.line.me/api/notify'
        headers = {'Authorization': f'Bearer {line_notify_token}'}
        message = '今日の誕生日は'+ str(person) + 'さんです'
        data = {'message': f'message: {message}'}
        requests.post(line_notify_api, headers = headers,data = data)

    def notify(self):
        if self.check_birthday() != None:
            self.line_notify()
        else:
            print('nothing')






