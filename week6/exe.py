import pandas as pd 

#url = 'https://api.statbank.dk/v1/tables'
#dst = pd.read_json(url)
#dst.to_csv('dk-stat-all-tables.csv', encoding='utf-8', index=False)
#dst[:20]


#With data aggregation and data visualization answer the following questions:
#What is the change in pct of divorced danes from 2008 to 2020?
url = "https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&CIVILSTAND=F%2CTOT&Tid=2008K1%2C2008K2%2C2008K3%2C2008K4%2C2009K1%2C2009K2%2C2009K3%2C2009K4%2C2010K1%2C2010K2%2C2010K3%2C2010K4%2C2011K1%2C2011K2%2C2011K3%2C2011K4%2C2012K1%2C2012K2%2C2012K3%2C2012K4%2C2013K1%2C2013K2%2C2013K3%2C2013K4%2C2014K1%2C2014K2%2C2014K3%2C2014K4%2C2015K1%2C2015K2%2C2015K3%2C2015K4%2C2016K1%2C2016K2%2C2016K3%2C2016K4%2C2017K1%2C2017K2%2C2017K3%2C2017K4%2C2018K1%2C2018K2%2C2018K3%2C2018K4%2C2019K1%2C2019K2%2C2019K3%2C2019K4%2C2020K1%2C2020K2%2C2020K3%2C2020K4"

dst = pd.read_csv(url)
dst.to_csv('dk-stat-all-tables.csv', encoding='utf-8', index=False)
#print(dst[:20])

#Which of the 5 biggest cities has the highest percentage of 'Never Married' in 2020?

url = "https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&CIVILSTAND=U%2CTOT&Tid=2020K1&OMR%C3%85DE=101%2C085%2C607%2C350%2C265"
dst = pd.read_csv(url)
dst.to_csv('dk-stat-all-tables.csv', encoding='utf-8', index=False)

print(dst[:20])


#Show a bar chart of changes in marrital status in Copenhagen from 2008 till now
#Show 2 plots in same figure: 'Married' and 'Never Married' for all ages in DK in 2020 (Hint: x axis is age from 0-125, y axis is how many people in the 2 categories). Add lengend to show names on graphs