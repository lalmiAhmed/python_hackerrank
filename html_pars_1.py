N=int(input())
from html.parser import HTMLParser
class myhtml(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :",tag)
        if attrs:
            for item in attrs:
                print("->",item[0],">",item[1])
    def handle_endtag(self, tag):
        print("End   :",tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :",tag)
        if attrs:
            for item in attrs:
                print("->",item[0],">",item[1])
parser = myhtml()
for _ in range(N):
    parser.feed(input())