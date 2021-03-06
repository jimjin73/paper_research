from googletrans import Translator
import arxiv
import sys
import requests
import datetime

def sendQuetyToArXiv():
    end_day=datetime.date.today() 
    start_day=end_day-datetime.timedelta(days=4) # TODO : change
    # TODO : read files to create query
    search = arxiv.Search(query =f'(cat:cs.AI OR cat:cs.LG OR cat.cs.CR OR cat.cs.DC) AND submittedDate:[{start_day.year:4}{start_day.month:02}{start_day.day:02} TO {end_day.year:4}{end_day.month:02}{end_day.day:02}]',
                        sort_by = arxiv.SortCriterion.SubmittedDate,
                        max_results = float('inf'),
    )
    return search.results()

def sendQueryToSlack(TOKEN, post_info):
    channel_name = 'announce' # included in post_info?
    message = post_info['title'] + '\n' +\
              post_info['first_author'] + ' et al.\n' +\
              post_info['url'] + '\n```' +\
              post_info['summary'] + '```'
    return requests.post('https://slack.com/api/chat.postMessage',\
                        data={'token': TOKEN, 'channel': channel_name, 'text':message})

def main(argv):
    MAX_NUM_OF_PAPERS = 5
    # TODO : check response
    paper_iterater = sendQuetyToArXiv()
    tr = Translator()
    # TODO : define MAX_NUM_OF_PAPERS
    for i, paper in enumerate(paper_iterater):
        if i >= MAX_NUM_OF_PAPERS:
            print(f'There are more than {MAX_NUM_OF_PAPERS} new papers.')
            break
        print(f'> {paper.title}')
        # TODO : check response
        summary_ja = tr.translate(text=paper.summary.replace('\n',''), src="en", dest="ja").text
        post_info = {
            'url':paper.pdf_url,
            'title':paper.title,
            'summary':summary_ja,
            'first_author':str(paper.authors[0])
        }
        # TODO : check response
        response = sendQueryToSlack(argv[1], post_info)
        
if __name__=='__main__':
    main(sys.argv)