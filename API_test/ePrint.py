# references
# https://www.iacr.org/cryptodb/data/api/
# https://eprint.iacr.org/
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

from bs4 import BeautifulSoup
import requests
import datetime

def edit_ePrint_html(html):
    html = html.replace('</em>\n','</em>\n</dt>')
    html = html.replace('</b>','</b></dd>')
    html = html.replace('</em>','</em></dd>')
    return html

def getSummaryFromDescription(html):
    target = '<b>Abstract: </b>'
    idx = html.find(target)
    return html[idx+len(target):].split('<p />')[0]

def getSubmissionDate(html):
    target = '<b>Date: </b>received '
    idx = html.find(target)
    submission_date_str = html[idx+len(target):].split('\n')[0].split(',')[0]
    return datetime.datetime.strptime(submission_date_str, '%d %b %Y')

days = 1
response = requests.get(f'https://eprint.iacr.org/eprint-bin/search.pl?last={days}')

raw_html = response.text
html = edit_ePrint_html(raw_html)

soup = BeautifulSoup(html, 'html.parser')
papers = soup.find_all('dt')
paper = papers[0]

title = paper.find_all('dd')[0].b.string
authors =  paper.find_all('dd')[1].em.string
description_url = 'https://eprint.iacr.org' + paper.find_all('a')[0].get('href')
pdf_url = 'https://eprint.iacr.org' + paper.find_all('a')[1].get('href')

print(title)
print(authors)
print(description_url)
print(pdf_url)

description_response = requests.get(description_url)
raw_description_html = description_response.text
summary = getSummaryFromDescription(raw_description_html)
submission_date = getSubmissionDate(raw_description_html)

print(summary)
print(submission_date)