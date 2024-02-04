import requests
import json
import random
import time
from html import unescape  # Import unescape to decode HTML entities

url = "https://opentdb.com/api.php?amount=10&category=9&difficulty=medium"

response = requests.get(url)
data = json.loads(response.text)


for i in range(10):
    question = unescape(data['results'][i]['question'])  # Decode HTML entities
    print(question)

    # Combine correct and incorrect answers into a single list
    correct_answer = [unescape(data['results'][i]['correct_answer'])]
    answers = [unescape(data['results'][i]['correct_answer'])]
    answers += [unescape(answer) for answer in data['results'][i]['incorrect_answers']]
    random.shuffle(answers)
    
    
    
    print("here are the possible answers", answers)
    response = input("what is your choice ? ")
    
    if (correct_answer[0] == response):
        print("good job, the answer is correct !! ")
        print(correct_answer[0])
    else :
        print("WRONG, the right answer was : ")
        print(correct_answer[0])

    
    print('\n')
    time.sleep(1)