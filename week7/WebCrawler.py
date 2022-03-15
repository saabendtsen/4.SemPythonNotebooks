import bs4
import requests

url = 'https://www.cphbusiness.dk'

r = requests.get(url)
r.raise_for_status()

soup = bs4.BeautifulSoup(r.text, 'html.parser')



for link in soup.find_all('a'):
    if link.get('href') and link.get('href').startswith('https'):
        print(link.get('href'))
        open(f"links/cphbusiness.txt",'a').write(link.get('href')+"\n")
        
        #Inderlink
        
        ri = requests.get(link.get('href'))
        ri.raise_for_status()
        soupi = bs4.BeautifulSoup(ri.text, 'html.parser')
        for linki in soupi.find_all('a'):
            if linki.get('href') and linki.get('href').startswith('https'):
                print(linki.get('href'))
                open(f"links/cphbusiness.txt",'a').write("\t"+linki.get('href')+"\n")
