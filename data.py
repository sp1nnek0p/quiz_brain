import requests
import json

def get_questions(url):
  jsondata = json.loads(requests.get(url).text)
  # print(jsondata['results'])
  return jsondata['results']


url = 'https://opentdb.com/api.php?amount=10&category=15&type=multiple'
question_data = get_questions(url)