import requests
import pprint
import json

response = requests.get("https://api.semanticscholar.org/v1/paper/arXiv:2002.06440")
print(response.status_code)
txt = json.loads(response.text)
pprint.pprint(txt.keys())
