#"Download datasettet fra dette link.
from ast import NotIn
from os import PRIO_USER
from posixpath import split
from traceback import print_tb
from urllib import request
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

#url = https://www.kaggle.com/sanjeetsinghnaik/top-1000-highest-grossing-movies 



#1. Find the top 10 highest grossing Disney movies measured by world sales
dts = pd.read_csv('Data1.csv')
disney = dts.loc[dts['Distributor'] == 'Walt Disney Studios Motion Pictures']

disneySorted = disney.sort_values(by=['World Sales (in $)'],ascending=False)
#Get Bitches
#print(disneySorted[:10])


#2. Create a pie chart that shows the distribution of Licenses (PG, R, M and so on)

licenses = dts['License'].unique()

ratingCount = []
ratingLabel = []
for x in licenses:
    ratingCount.append(len(dts.loc[dts['License'] == x]))
    ratingLabel.append(x)


#plt.pie(ratingCount, labels = ratingLabel)
#plt.show()

#3. Get the percentage of PG rated movies between 2001 and 2015


all_PG_movies = dts.loc[dts['License'] == 'PG']
new = all_PG_movies["Release Date"].str.split(",", n=1)

#all_PG_movies = all_PG_movies.squeeze() not sure what squeeze does.
#Makes DataFrame to a list

list_of_PG_movies = all_PG_movies.values.tolist()

PG_movies_in_2001_2015 = 0
for year in range(2001,2016):
    year = str(year)
    movies_pr_year = 0
    for movies in list_of_PG_movies:
        if year in movies[4]:
            PG_movies_in_2001_2015 += 1
            movies_pr_year += 1
        procent_of_movies_pr_year = (movies_pr_year/len(all_PG_movies)) * 100
    #print(procent_of_movies_pr_year)

procent_of_movies = (PG_movies_in_2001_2015/len(all_PG_movies)) * 100
#print(procent_of_movies)

#4. Calculate the average of world sales for each genre and visualize the data with a bar chart. (Hint: use groupBy)


all_movie_list = dts.values.tolist()
each_genre = []

for movie in all_movie_list:
    tmp_genre = movie[8].split(',')

    for genre in tmp_genre:
        clean_genre = re.sub(r"[\[\]\']","",genre)
        clean_genre = clean_genre.strip()

        if len(each_genre)>0 and clean_genre in list(list(zip(*each_genre))[0]):
            index = list(list(zip(*each_genre))[0]).index(clean_genre)
            each_genre[index][1].append(movie[7])
        else:
            each_genre.append([clean_genre,[movie[7]]])
        
#print(each_genre)

avg_sale_per_genre = []

for genre in each_genre:
    
    Sum = sum(genre[1])
    avg = Sum/len(genre[1])
    avg_sale_per_genre.append((genre[0],int(avg)))

plt.figure(figsize=(35, 10))
plt.xticks(rotation='vertical')
plt.bar(list(list(zip(*avg_sale_per_genre))[0]),list(list(zip(*avg_sale_per_genre))[1]),align='center', width=0.5)
plt.show()
