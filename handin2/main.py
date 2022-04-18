from tracemalloc import stop
import bs4
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url2020 = "https://www.rottentomatoes.com/top/bestofrt/?year=2020"

url2010 = "https://www.rottentomatoes.com/top/bestofrt/?year=2010"


def get_info(url):
    url = url2010

    profile = webdriver.FirefoxProfile()
    profile.set_preference("general.useragent.override", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0")
    
    # headless is needed here because we do not have a GUI version of firefox
    options = Options()
    options.headless = True
    # driver = webdriver.Firefox(options=options, executable_path=r'/tmp/geckodriver')
    browser = webdriver.Firefox(options=options)

     # browser = webdriver.Firefox()
    browser.get(url)
    browser.implicitly_wait(3)

    #main_container = browser.find_element_by_id('top_movies_main')
    #print(main_container)

    full_table = browser.find_elements_by_xpath('//*[@id="top_movies_main"]/div/table/tbody/tr')

    tmp_table = []
    tmp_table.append(full_table[0])
    tmp_table.append(full_table[1])
    full_table = tmp_table

    links = []
    movies = []

    for link in full_table:
        atag = link.find_element_by_tag_name('a')
        link = atag.get_attribute('href')
        links.append(link)
    
    print(len(links))

    for link in links:
        browser.get(link)
        browser.implicitly_wait(3)

        name = link.split('/')[-1]
        print(name)
        genre = browser.find_element_by_xpath('//*[@id="mainColumn"]/section[3]/div/div/ul/li[2]/div[2]').text
        print(genre)
        rating = browser.find_element_by_xpath('//*[@id="mainColumn"]/section[3]/div/div/ul/li[1]/div[2]').text
        print(rating)
        runtime = browser.find_elements_by_tag_name('time')
        print(runtime[2].get_attribute("innerHTML").strip())

        #score = browser.find_element_by_class_name('percentage').text
        score = browser.find_element_by_xpath('//*[@id="topSection"]/div[1]/score-board//div/div[2]/div[1]/div/score-icon-critic//div/span[2]')

        print(score)

        movies.append(name,genre,rating)

    return movies
   

get_info(url2010)

#	- det er top 100 film fra et givent år

#- Scrape navn, genre, runtime, tomatometer score og audience score på filmene fra årstallet 2020 og 1990
#	- Hvis en film har flere genre så tilhører den alle de forskellige genre grupper

#- Vis den gennemsnitlige audience score for hver genre i 2020 og 2010, i den samme barchart

#- Find den genre hvor der er størst forskel fra audience score og tomatometer score i 2010
#	- har det ændret sig i 2020?
#	- hvis ja
#		- vis en barchart af de forskellige genre

#- Hvad er den gennemsnitlige runtime for genren 'drama' i 2010 og 2020?"






