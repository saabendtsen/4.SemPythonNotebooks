
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import multiprocessing
import requests

class TextComparer():

    def __init__(self,url_list):
        self.url_list = url_list
        self.files = []


    def download(self,url,filename=None):
        res =  requests.get(url,stream=True)
        if(res.status_code == 404): 
            raise NotFoundExecption(url)
        else:
            if(filename==None):
                list = url.split('/')
                name = list[-1]
            else:
                name = filename
            path = f"my_work/week6/files/{name}"
            open(path,'wb').write(res.content)
            self.files.append(path)
            return "Downloaded completed"
           
    def multi_download(self):
        with ThreadPoolExecutor(len(self.url_list)) as exe:
            for url in self.url_list:
                print(url)
                exe.submit(self.download(url))

    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        while self.index < len(self.files):
            res = self.files[self.index]
            self.index += 1
            return res
        raise StopIteration

    def urllist_generator(self):
        for el in self.files:
            yield el
             
    def avg_vowels(self,text):
        vowels = "AaEeIiOoUu"
        words = text.split()
        
        counter = 0
        for word in words:
            for Char in word:
                if(Char in vowels):
                    counter += 1
        return counter/len(words)

    def get_avg_multiproc(self):
        with ProcessPoolExecutor(multiprocessing.cpu_count()) as exe:
            r = exe.map(self.open_file_and_Get_avg,self.files)
        return list(r)


    def get_avg_vowels(self):
        res = []
        for file in self.files:
            res.append(self.open_file_and_Get_avg(file))
        return res

    def open_file_and_Get_avg(self,filename):
        with open(filename,'r') as textFile:
            text = textFile.read()
            avg_vowel = self.avg_vowels(text)
            return(filename,avg_vowel)


urls = []
urls.append("https://www.gutenberg.org/files/84/84-0.txt")
urls.append("https://www.gutenberg.org/files/1342/1342-0.txt")
urls.append("https://www.gutenberg.org/files/11/11-0.txt")
urls.append("https://www.gutenberg.org/cache/epub/64317/pg64317.txt")
urls.append("https://www.gutenberg.org/files/5199/5199-0.txt")
urls.append("https://www.gutenberg.org/files/2542/2542-0.txt")
urls.append("https://www.gutenberg.org/files/98/98-0.txt")
urls.append("https://www.gutenberg.org/cache/epub/174/pg174.txt")
urls.append("https://www.gutenberg.org/files/1661/1661-0.txt")
urls.append("https://www.gutenberg.org/cache/epub/25344/pg25344.txt")
urls.append("https://www.gutenberg.org/cache/epub/26184/pg26184.txt")
urls.append("https://www.gutenberg.org/files/1260/1260-0.txt")
urls.append("https://www.gutenberg.org/files/1400/1400-0.txt")
urls.append("https://www.gutenberg.org/files/1952/1952-0.txt")
urls.append("https://www.gutenberg.org/files/345/345-0.txt")


tc = TextComparer(urls)
#print(tc.download("https://www.gutenberg.org/files/84/84-0.txt","fisse.txt"))

#print(tc.download("https://www.gutenberg.org"))
print(tc.multi_download())
#tc.get_avg_vowels()

testfiles = [
    "my_work/week6/files/11-0.txt",
    "my_work/week6/files/84-0.txt"
]

#print(tc.get_avg_vowels())
print(tc.get_avg_multiproc())

class NotFoundExecption(Exception):
    def __init__(self,url):
        self.url = url
        super().__init__(f"{self.url} responded with 404")

#python -m my_work.week6.TextComparer
