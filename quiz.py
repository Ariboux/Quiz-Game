import requests
import json
import random
import time

url = "https://opentdb.com/api.php?amount=10&category=9&difficulty=medium"

response = requests.get(url)
data = json.loads(response.text)


for i in range(10):
    print(data['results'][i]['question'])
    results = tuple(data['results'][i]['correct_answer'])
    results += tuple([data['results'][i]['incorrect_answers']])
    results = list(results)
    random.shuffle(results)
    print(results)
    print('\n')
    time.sleep(1)