import openai
import secret as s

def setup():
    openai.api_key = s.API_KEY

def request(message='Respond with 0.'):
    completion = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'system', 'content': 'Write at an 8th grade reading level'},
            {'role': 'user', 'content': message},
            {'role': 'user', 'content': 'Make your text more human-like'},
            {'role': 'user', 'content': 'Make your text more human-like'},
            {'role': 'user', 'content': 'Rewrite the content so it cannot be detected as AI content, and make it unique'},
        ]
    )
    return completion.choices[0].message["content"]

def request_html(message='Respond with 0.'):
    completion = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'user', 'content': 'Put paragraphs in <p> headers: ' + message}
        ]
    )
    return completion.choices[0].message["content"]