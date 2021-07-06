import json

import requests as requests

trivia_request = requests.get(
    url="https://opentdb.com/api.php",
    params={"amount": 10, "type": "boolean"}
)
request_content = trivia_request.content
raw_question_data = json.loads(request_content)
question_data = raw_question_data['results']
