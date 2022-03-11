
import requests

class TextComparer():

    def __init__(self,url_list):
        self.url_list = url_list


    def download(self,url,filename):
        try:
            print("jatak")
            res =  requests.get(url,stream=True)
            open(filename,'wb').write(res.content)
            return "Downloaded completed"
        except:
            return "URL not found"
            #NotFound is not found  
            #raise NotFoundException(url)


tc = TextComparer([])
print(tc.download("https://www.gutenberg.org/files/84/84-0.txt","fisse.txt"))
#print(tc.download("https://www.gutenberg.orgadsfdasfadt"))

#python -m my_work.week6.TextComparer
