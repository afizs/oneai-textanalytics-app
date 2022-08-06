# Edit this One AI API call using our studio at https://studio.oneai.com/?pipeline=j2Yiyk


import requests
from pprint import pprint
from config import api_key

url = "https://api.oneai.com/api/v0/pipeline"


def oneai_pipeline(text):
  headers = {
    "api-key": api_key, 
    "content-type": "application/json"
  }
  payload = {
    "input": text,
    "input_type": "article",
    "steps": [
          {
            "skill": "summarize",
            "params": {
            "auto_length": True,
            "max_length": 100,
            "min_length": 5
            }
          },
        
      ]
  }
  r = requests.post(url, json=payload, headers=headers)
  data = r.json()
  return data['output'][0]['text']