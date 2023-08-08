import gpt
import images
import scrape
# TODO
# DONE Create multiple articles
# DO Add images support
# Add anti-AI API (maybe not)
# DO Add competitor analysis
# DO Add AI detection API

if __name__ == '__main__':

    # images.get_image()
    t = scrape.get_raw_text('vitamin d dog overdosea')
    print(t)
    # print(scrape.get_common_words(t))
    exit()
    gpt.setup()
    MAIN_TOPICS = ['Why is Vitamin D Required?', 'Why Vitamin D Gets Low', 'Vitamin D Dog Overdose',
                    'Can Too Much Vitamin D Cause Skin Issues?', 'What Diseases Cause High Vitamin D?',]
    TOPICS = [
        [
            'Evidence',
            'Recommended Amounts',
            'Food Sources',
            'Ultraviolet Light',
*            'Signs of Deficiency',
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
            'How can I Prevent Vitamin D Deficiency?',
        ],
        [
            'Symptoms',
            'Causes',
            'Diagnosis',
            'Treatment',
            'After Treatment',
        ],
        [
            'Side Effects',
            'Treatment',
            'Prevention',
        ],
        [
            'Diseases',
            'Causes',
            'Diagnosis',
            'Treatment',
            'Prevention',
            'Contact Your Doctor'
        ]
    ]
    WORD_COUNTS = [300, 300, 200, 250, 200]
    FILE_LOCATION = 'pages\\vitamind\\'

    #print(gpt.request(message='Give me 10 subtopics less than 10 words about ' + MAIN_TOPICS[len(MAIN_TOPICS) - 1]
    #                            + '. Format it like this |title|'))
    #a = input('Press Enter to Continue:')

    for topic in range(len(MAIN_TOPICS)):
        PERCENT_COMPLETE = 0
        TEXT = ''
        TEXT_RAW = ''
        TMP = ''
        HEAD = '<!DOCTYPE html>\n<html>\n<head>\n<title>' + MAIN_TOPICS[topic] + r'</title>' + '\n<meta name=\"description\" content=\"'

        f = open(FILE_LOCATION + MAIN_TOPICS[topic].replace(' ', '').replace('?', '') + '.html', 'w')
        r = open('rawtext\\' + MAIN_TOPICS[topic].replace(' ', '').replace('?', '') + '.txt', 'w')
        for i in range(int(len(TOPICS[topic]))):

            PERCENT_COMPLETE += 1
            print('Article ' + str(topic + 1) + ': ' + str(int(PERCENT_COMPLETE / len(TOPICS[topic]) * 100)) + '%')

            if i == 0:
                TEXT += '<h1>' + MAIN_TOPICS[topic] + '</h1>\n<hr class="hrtitle">\n'
                INTRO = gpt.request(
                    message='Write 100 words introducing an article about ' + MAIN_TOPICS[topic]) + 'without giving any details'
                TEXT += '<p>' + INTRO + '/p>'
                HEAD += INTRO + '\">\n<link rel="stylesheet" href="..\\styles.css">\n<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat">\n</head>'

                TEXT += '\n<br>\n<h2>' + TOPICS[topic][i] + '</h2>\n<hr>\n<br>\n'
                TMP = gpt.request(
                    message='Write ' + str(WORD_COUNTS[topic]) + ' words about ' + MAIN_TOPICS[topic] + ' ' + TOPICS[topic][i] + "try not to use the phrase 'in conclusion', ")
                TEXT += gpt.request_html(TMP)
                TEXT_RAW += TMP
            else:
                TEXT += '\n<br>\n<h2>' + TOPICS[topic][i] + '</h2>\n<hr class="hrtitle">\n'
                TMP = gpt.request(
                message='Write ' + str(WORD_COUNTS[topic]) + ' words about ' + TOPICS[topic][i] + "try not to use the phrase 'in conclusion', "
                                                                "and write as if it is continuing off another paragraph "
                                                                "about" + MAIN_TOPICS[topic] + ' ' + TOPICS[topic][i - 1])
                TEXT += gpt.request_html(TMP)
                TEXT_RAW += TMP
            
        TEXT += '\n<br>\n<hr>\n'
        TMP = gpt.request(
            message='Write 100 words concluding an article about ' + MAIN_TOPICS[topic] + 'without giving any details')
        TEXT += gpt.request_html(TMP)
        TEXT_RAW += TMP
        NAV = open('NavBar.html', 'r').read()
        SIDER = '\n<br>\n<div class="child2">\n<br><br>\n<h2>More</h2>\n<hr class="hrtitle">\n<p>LINK</p>\n<hr>\n</div>\n<hr>\n'

        TEXT = HEAD + '\n<body>\n' + NAV + '\n<div class="container">\n<article class="child1">\n' + TEXT + '\n</article>' + SIDER + '</div>\n</body>\n</html>'

        f.write(TEXT)
        r.write(TEXT_RAW)