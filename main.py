import gpt

# TODO
# DONE Create multiple articles
# DO Add Grammarly/other Grammar API
# DO Add AI detection API

if __name__ == '__main__':
    gpt.setup()
    MAIN_TOPICS = ['Why is Vitamin D Required?', 'Why Vitamin D Gets Low']
    TOPICS = [
        [
            'Evidence',
            'Recommended Amounts',
            'Food Sources',
            'Ultraviolet Light',
            'Signs of Deficiency',
        ],
        [
            'What is Vitamin D Deficiency?',
            'Why is Vitamin D so Important?',
            'Who does Vitamin D Deficiency Affect?',
            'How Common is Vitamin D Deficiency?',
            'What Causes Vitamin D Deficiency?',
            'Weight Loss Surgeries and Vitamin D Deficiency',
            'How is Vitamin D Deficiency Diagnosed?',
            'How is Vitamin D Deficiency Treated??',
            'How can I Prevent Vitamin D Defiency?',
        ]
    ]
    WORD_COUNTS = [300, 300]
    FILE_LOCATION = 'pages/vitamind'

    try:
        print(gpt.request(message='Give me 10 subtopics less than 10 words about ' + MAIN_TOPICS[len(MAIN_TOPICS) - 1]
                                  + '. Format it like this |title|'))
        a = input('Press Enter to Continue:')

        for topic in range(len(MAIN_TOPICS)):
            TEXT = ''
            HEAD = '<!DOCTYPE html>\n<html>\n<head>\n<title>' + MAIN_TOPICS[topic] + r'</title>' + '\n<meta name=\"description\" content=\"'

            f = open(FILE_LOCATION + MAIN_TOPICS[topic].replace(' ', '') + '.html', 'w')
            TEXT += ''
            for i in range(int(len(TOPICS[topic]))):
                if i == 0:
                    TEXT += '<h1>' + MAIN_TOPICS[topic] + '</h1>\n\n'
                    INTRO = gpt.request(
                        message='Write 100 words introducing an article about ' + MAIN_TOPICS[topic]) + 'without giving any details'
                    TEXT += '<p>' + INTRO + '/p>'
                    HEAD += INTRO + '\">\n<link rel="stylesheet" href="styles.css">\n</head>'

                    TEXT += '\n<h2>' + TOPICS[topic][i] + '</h2>\n'
                    TEXT += gpt.request_html(gpt.request(
                        message='Write ' + str(WORD_COUNTS[topic]) + ' words about ' + MAIN_TOPICS[topic] + ' ' + TOPICS[topic][i] + "try not to use the phrase 'in conclusion', "))
                else:
                    TEXT += '\n<h2>' + TOPICS[topic][i] + '</h2>\n'
                    TEXT += gpt.request_html(gpt.request(
                    message='Write ' + str(WORD_COUNTS[topic]) + ' words about ' + TOPICS[topic][i] + "try not to use the phrase 'in conclusion', "
                                                                   "and write as if it is continuing off another paragraph "
                                                                   "about" + MAIN_TOPICS[topic] + ' ' + TOPICS[topic][i - 1]))
            TEXT += '\n<br>\n'
            TEXT += gpt.request_html(gpt.request(
                message='Write 100 words concluding an article about ' + MAIN_TOPICS[topic]) + 'without giving any details')
            TEXT = HEAD + '\n<body>\n' + TEXT + '\n</body>\n</html>'
            f.write(TEXT)
    except:
        print("Error occured.")
