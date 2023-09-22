import gpt
import images
import scrape
# TODO
# DONE Create multiple articles
# DONE Add images support
# DONE Add competitor analysis
# DONE
# + Change Nav (Not SEO friendly)
# -- RELEASE -- (September)
# DO Add Google Analytics (IMPORTANT)
# DO Improve looks
# DO Add AI detection API
# DO Automatic header detection
# DO Automatic in-text reference
# DO Add table of contents html
if __name__ == '__main__':

    gpt.setup()

    FILE_LOCATION = 'pages\\motorcycle\\'
    FILE_LOCATION_RAW = 'rawtext\\motorcycle\\'
    FILE_LOCATION_HTML = 'rawhtml\\motorcycle\\'

    MAIN_TOPICS = ['Motorcycle No Chase Law States', 'Motorcycle Tire Dry Rot', 'Open Carry on a Motorcycle', 'Motorcycle Fat Rear Tire', 'Motorcycle Throttle Not Snapping Back: Causes and Fixes']
    
    COMP_LINKS = [
        [
            'https://www.apexriders.com/can-police-chase-motorcycles/#:~:text=States%20with%20No%20chase%20Law%20for%20Motorcycles&text=Alabama%20holds%20a%20unique%20position,no%20chase%20law%20for%20motorcycles.',
            'https://awajis.com/us/motorcycle-no-chase-law-states/',
        ],
        [
            'https://www.motosport.com/blog/how-to-prevent-tire-dry-rot',
            'https://motorbiketireshop.com/biker-news/are-cracks-on-motorcycle-tires-dangerous',
        ],
        [
            'https://www.motorcycle.com/features/riding-with-a-gun.html',
            'https://thefirearmfirm.com/can-you-carry-a-firearm-while-riding-a-motorcycle/',
        ],
        [
            'https://motorbiketireshop.com/biker-news/pros-and-cons-of-a-wide-back-motorcycle-tire',
            'https://happywrench.com/pros-and-cons-of-wide-back-motorcycle-tire/',
        ],
        [
            'https://blog.pro-x.com/how-to-adjust-and-replace-your-motorcycles-throttle-cable#:~:text=If%20the%20throttle%20does%20not,closed%20position%20quickly%20and%20easily.',
            'https://bigbikereviews.com/motorcycle-throttle-not-snapping-back/',
        ]
    ]
    
    TOPICS = [
        [
            'Which States Have No Chase Law for Motorcycles',
            'Initiation of Pursuit',
            'Termination of Pursuit',
            'Can Police Chase Motorcycle Riders Without Helmets?',
            'Is There a Speed Where Cops Won\'t Chase You?',
            'Can Motorcycles Outrun Cops?',
            'Can Cops Hit Motorcycles',
        ],
        [
            'How Much Tire Dry Rot is Too Much?',
            'How To Prevent Tire Rot: Avoid Sunlight Exposure',
            'How To Prevent Tire Rot: Take Tires for a Spin',
            'How To Prevent Tire Rot: Maintain Air Pressure',
            'How To Prevent Tire Rot: Clean Tires',
            'How To Prevent Tire Rot: Tire Storage',
        ],
        [
            'Can you Carry a Firearm on a Motorcycle?',
            'States WITH Laws Concerning Transportation of a Firearm',
            'States WITHOUT Laws Concerning Transportation of a Firearm',
            'CWFL and Other Permits',
            'Peacable Journey Act',
            'Cooperate with Police',
            'What To Do/Not To Do with the Firearm',
        ],
        [
            'Benefits: Traction, Smoothness',
            'Downsides: Maintenance, Performance, Fuel Consumption',
            'Things to Keep In Mind When Purchasing',
            'Frequently Asked Questions',
        ],
        [
            'Cause: Sticky Throttle Grip',
            'Fix: Sticky Throttle Grip'
            'Cause: Dirty Throttle Tube',
            'Fix: Dirty Throttle Tube',
            'Cause: Damaged Throttle Cable',
            'Fix: Damaged Throttle Cable',
            'Cause: Damaged Throttle Return Spring',
            'Fix: Damaged Throttle Return Spring',
            'Cause: Incorrect Cable Tension',
            'Fix: Incorrect Cable Tension',
            'Cause: Faulty Cable Housing',
            'Fix: Faulty Cable Housing',
            'Cause: Idle Speed Adjustment Screw Stuck',
            'Fix: Idle Speed Adjustment Screw Stuck',
        ]
    ]
    IMAGES = [
        [
            'Police Officer on Motorcycle',
            'Police Sirens',
            ' ',
            'Motorcycle rider with no helmet',
            'Person riding sport bike',
            'Motorcycle rider racing',
            'Police pit manuever',
        ],
        [
            'Motorcycle tire dry rot'
            'Tire dry rot',
            'Sun',
            'Person riding motorcycle',
            'Motorcycle tire pressure',
            'Motorcycle cleaned tires stock photo',
            'Classic garage door',
        ],
        [
            'Open carry of rifle',
            ' ',
            ' ',
            'CWFL Permit',
            ' ',
            'Police stopping motorcycle',
            ' ',
        ],
        [
            'Motorcycle wide rear tire',
            'Batman motorcycle',
            ' ',
            ' ',
        ],
        [
            ' ',
            'Throttle grip motorcycle',
            ' ',
            'Throttle tube',
            ' ',
            ' ',
            ' ',
            'Throttle return spring',
            ' ',
            'Throttle cable tension',
            ' ',
            ' ',
            ' ',
            'Idle Speed Adjustment Screw',
        ]
    ]


    for topic in range(len(MAIN_TOPICS)):
        PERCENT_COMPLETE = 0
        TEXT = ''
        TEXT_RAW = ''
        TMP = ''
        t = ''
        for i in range(len(COMP_LINKS[topic])):
            t += scrape.get_raw_text(COMP_LINKS[topic][i])
        data_for_gpt = 'Also, use the word '

        data = scrape.get_percent_words(t)
        for key in data:

            data_for_gpt += '"' + key + '" or synonyms, about ' + str(round(data[key], 1)) + '% of the time, '

        data_for_gpt += 'and "' + MAIN_TOPICS[topic] + '" or synonyms about 1% of the time, but make sure the usage of these words is natural.'

        SECTION_WORDCOUNT = int(scrape.get_wordcount(t) / len(COMP_LINKS[topic]) / len(TOPICS[topic]))
        print('WC ', SECTION_WORDCOUNT)
        HEAD = '<!DOCTYPE html>\n<html>\n<head>\n<title>' + MAIN_TOPICS[topic] + '</title>' + '\n<meta name=\"description\" content=\"'

        f = open(FILE_LOCATION + MAIN_TOPICS[topic].replace(' ', '').replace('?', '') + '.html', 'w')
        r = open(FILE_LOCATION_RAW + MAIN_TOPICS[topic].replace(' ', '').replace('?', '') + '.txt', 'w')
        h = open(FILE_LOCATION_HTML + MAIN_TOPICS[topic].replace(' ', '').replace('?', '') + '.txt', 'w')

        for i in range(int(len(TOPICS[topic]))):

            PERCENT_COMPLETE += 1
            print('Article ' + str(topic + 1) + ': ' + str(int(PERCENT_COMPLETE / len(TOPICS[topic]) * 100)) + '%')

            if i == 0:
                TEXT += '<h1>' + MAIN_TOPICS[topic] + '</h1>\n<hr class="hrtitle">\n'
                INTRO = gpt.request(
                    message='Write 100 words introducing an article about ' + MAIN_TOPICS[topic] + 'without giving any details, ' + data_for_gpt).replace('"', '')
                TEXT += '<p>' + INTRO + '</p>'
                HEAD += INTRO + '\">\n<link rel="stylesheet" href="../styles.css">\n<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat">\n</head>'

                TEXT += '\n<br>\n<h2>' + TOPICS[topic][i] + '</h2>\n<hr>\n<br>\n'
                TMP = gpt.request(
                    message='Write ' + str(SECTION_WORDCOUNT) + ' words about ' + TOPICS[topic][i] + ' and focus on this topic. This is a part of a larger article about ' + MAIN_TOPICS[topic] + '. Try not to use the phrase "in conclusion", ' + data_for_gpt)
                TEXT += gpt.request_html(TMP)
                TEXT_RAW += TMP
            #IS ELSE NEEDED (JUST REMOVE?)
            else:
                TEXT += '\n<br>\n<h2>' + TOPICS[topic][i] + '</h2>\n<hr class="hrtitle">\n'
                TMP = gpt.request(
                    message='Write ' + str(SECTION_WORDCOUNT) + ' words about ' + TOPICS[topic][i] + ' and focus on this topic. This is a part of a larger article about ' + MAIN_TOPICS[topic] + '. Try not to use the phrase "in conclusion", ' + data_for_gpt)
                TEXT += gpt.request_html(TMP)
                TEXT_RAW += TMP
            img =  images.get_image(desc=IMAGES[topic][i])
            if img != '0':
                TEXT += '\n<br><img src="../../images/' + img + '.jpg' + '" alt="' + img + '"><br><br>'
            
        TEXT += '\n<br>\n<hr>\n'
        TMP = gpt.request(
            message='Write 100 words concluding an article about ' + MAIN_TOPICS[topic] + 'without giving any details')
        TEXT += gpt.request_html(TMP)
        TEXT_RAW += TMP

        NAV = open('NavBar.html', 'r').read()
        SIDER = '\n<br>\n<div class="child2">\n<br><br>\n<h2>More</h2>\n<hr class="hrtitle">\n<p>LINK</p>\n<hr>\n</div>\n<hr>\n'
        ARTICLE =  '\n<article class="child1">\n' + TEXT + '\n</article>'

        TEXT = HEAD + '\n<body>\n' + NAV + '\n<div class="container">' + ARTICLE + SIDER + '</div>\n</body>\n</html>'

        f.write(TEXT)
        r.write(TEXT_RAW)
        h.write(ARTICLE)