def modify_html(dir='', name=''):

    ARTICLE = open('rawhtml\\' + dir + name + '.txt', 'r').read()

    HEAD = '<!DOCTYPE html>\n<html>\n<head>\n<title>' + name + '</title>' + '\n<meta name=\"description\" content=\"'
    NAV = open('NavBar.html', 'r').read()
    SIDER = '\n<br>\n<div class="child2">\n<br><br>\n<h2>More</h2>\n<hr class="hrtitle">\n<p>LINK</p>\n<hr>\n</div>\n<hr>\n'
    TEXT = HEAD + '\n<body>\n' + NAV + ARTICLE + SIDER + '</div>\n</body>\n</html>'

    F_ARTICLE = open('rawhtml\\' + name + '.txt', 'w')
    F_ARTICLE.write(TEXT)

# CAN EXECUTE CODE BELOW
# ----------------------
# modify_html(dir='motorcycles\\', name='How To')
# ----------------------
# CAN EXECUTE CODE ABOVE
