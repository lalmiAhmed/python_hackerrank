N=int(input())
from html.parser import HTMLParser
class myhtml(HTMLParser):
    def handle_comment(self, data):
        print("comment: ", data)
        # for cmnt in data:
        #     print("Comment  :", cmnt)
    def handle_data(self, data):
        print("Data     :", data)




parser = myhtml()
for _ in range(N):
    parser.feed(input())