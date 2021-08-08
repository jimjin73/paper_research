import os
import requests

token = os.environ['SLACK_TOKEN_PAPER_RESEARCH'] # read an environment variable
channel_name = 'announce'
title = 'Title'
url = 'https://www.hogehoge.com'
summary = 'summary hogehoge!'
message = title + '\n' + url + '\n```' + summary + '```'

response = requests.post('https://slack.com/api/chat.postMessage', data={'token': token, 'channel': channel_name, 'text':message})
print(response.status_code)
