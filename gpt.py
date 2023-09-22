import openai
import secret as s

VERSION = 'gpt-4'

def setup():
    openai.api_key = s.CHATGPT_API_KEY

def request(message='Respond with 0.'):
    completion = openai.ChatCompletion.create(
        model=VERSION,
        messages=[
            {'role': 'system', 'content': 'Write at an 8th grade reading level, but do not reference 8th graders'},
            {'role': 'user', 'content': message},
            {'role': 'user', 'content': 'Rephrase the content so it cannot be detected as AI content, and make it unique'},
            {'role': 'user', 'content': 'Fix all grammar mistakes'},

        ]
    )
    return completion.choices[0].message["content"]

def request_html(message='Respond with 0.'):
    completion = openai.ChatCompletion.create(
        model=VERSION,
        messages=[
            {'role': 'user', 'content': 'Put the following paragraphs in <p> headers: ' + message}
        ]
    )
    return completion.choices[0].message["content"]