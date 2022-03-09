from modules import webget

class TextComparer():

    def __init__(self,url_list):
        self.url_list = url_list


    def download(url,filename):
        try:
            webget.download(url,filename)
        except:
            return "URL not found"


tc = TextComparer([])
tc.download("https://www.gutenberg.org/files/84/84-0.txt")
#python -m my_work.week6.TextComparer