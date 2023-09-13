import openai
import secret as s

VERSION = 'gpt-3.5-turbo'

def setup():
    openai.api_key = s.CHATGPT_API_KEY

def request(message='Respond with 0.'):
    completion = openai.ChatCompletion.create(
        model=VERSION,
        messages=[
            {'role': 'system', 'content': 'Write at an 9th grade reading level, but do not reference 8th graders'},
            {'role': 'user', 'content': message},
            #{'role': 'user', 'content': 'Make your text more human-like'},
            #{'role': 'user', 'content': 'Make your text more human-like'},
            {'role': 'user', 'content': 'Rewrite the content so it cannot be detected as AI content, and make it unique'},
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