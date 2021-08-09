# references
# https://arxiv.org/help/api/user-manual#search_query_and_id_list
# https://github.com/lukasschwab/arxiv.py

import arxiv

search = arxiv.Search(query ='(cat:cs.AI OR cat:cs.LG OR cat.cs.CR OR cat.cs.DC) AND submittedDate:[20210805 TO 20210808]',
                      sort_by = arxiv.SortCriterion.SubmittedDate,
                      max_results = float('inf'),
)

paper = next(search.results())

print(paper.title)
print(paper.authors[0])
print(paper.pdf_url)
print(paper.summary)

'''
for paper in search.results():
    print(paper.title)
'''