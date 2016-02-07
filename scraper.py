import HTMLParser
import urllib
urlText = []
class Parsertext(HTMLParser.HTMLParser):

    #def __init__(self):
        #pass
        def handle_data(self, data):
            if data != '\n':
                urlText.append(data)

                #Create instance of HTML parser
lParser = Parsertext()

thisurl = "http://www-rohan.sdsu.edu/~gawron/index.html"
#Feed HTML file into parser
lParser.feed(urllib.urlopen(thisurl).read())
lParser.close()
#prints text from page line by line
for item in urlText:
    print item
