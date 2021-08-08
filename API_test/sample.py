from googletrans import Translator
import arxiv
import os
import requests
import datetime

end_day=datetime.date.today() 
start_day=end_day-datetime.timedelta(days=3)  

search = arxiv.Search(query =f'(cat:cs.AI OR cat:cs.LG OR cat.cs.CR OR cat.cs.DC) AND submittedDate:[{start_day.year:4}{start_day.month:02}{start_day.day:02} TO {end_day.year:4}{end_day.month:02}{end_day.day:02}]',
                      sort_by = arxiv.SortCriterion.SubmittedDate,
                      max_results = float('inf'),
)

paper = next(search.results())

url = paper.pdf_url
title = paper.title
summary_en = paper.summary

tr = Translator()
summary_ja = tr.translate(text=summary_en.replace('\n',''), src="en", dest="ja").text

token = os.environ['SLACK_TOKEN_PAPER_RESEARCH'] # read an environment variable
channel_name = 'announce'
message = title + '\n' + url + '\n```' + summary_ja + '```'

response = requests.post('https://slack.com/api/chat.postMessage', data={'token': token, 'channel': channel_name, 'text':message})