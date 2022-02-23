import numpy as np



#load the csv file: befkbhalderstatkode.csv into a numpy ndarray
#How many german children of 0 years were there in Copenhagen in 2015?
#create a function that can take any combination of the 4 parameters:AAR,BYDEL,ALDER,STATKODE and return population data
#create a new function like previous so that it can sum values for all ages if age is not provided to the function
#further add functionality to sum values if citizenship or area was not provided to function.
#create a new function that can also give average values for each year if year whas not provided.
#create a function, that given year and nationality can return which area had the most of these nationals by that year. Test it by finding out which area had the most Moroccan people in both 1992 and 2015
#Find the Area(s) where fewest foreingers lived in Copenhagen in 1992 and 2015 respectively
#Find out what age most French people have in 2015





filename = '../../data/befkbhalderstatkode.csv'
#AAR,BYDEL,ALDER,STATKODE,PERSONER
dd = np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)

#tysk 0år,2015,
mask = (dd[:,0] == 2015) & (dd[:,2] == 0) & (dd[:,3] == 5180)

#print(np.sum(dd[mask][:,4]))

#create a function that can take any combination of the 4 parameters:AAR,BYDEL,ALDER,STATKODE and return population data
def getPopData(AAR,BYDEL,ALDER,STATKODE):
    mask = (dd[:,0] == AAR) & (dd[:,1] == BYDEL) &(dd[:,2] == ALDER) & (dd[:,3] == STATKODE)
    return dd[mask]

#print(getPopData(2004,3,18,5100))

#create a new function like previous so that it can sum values for all ages if age is not provided to the function
def getPopDataOrSum(AAR,BYDEL,STATKODE,ALDER = None):
    if ALDER:
        mask = (dd[:,0] == AAR) & (dd[:,1] == BYDEL) &(dd[:,2] == ALDER) & (dd[:,3] == STATKODE)
        return dd[mask]
    else:
        mask = (dd[:,0] == AAR) & (dd[:,1] == BYDEL) & (dd[:,3] == STATKODE)
        return np.sum(dd[mask][:,4])
#print(getPopDataOrSum(AAR=2004,BYDEL=3,STATKODE=5100))

def getPopDataOptinalParameter(AAR = None,BYDEL = None, STATKODE = None,ALDER = None):
    
    
    pAAr = (dd[:,0] == AAR) if AAR else True
    pBYDEL = (dd[:,1] == BYDEL) if BYDEL else True
    pALDER = (dd[:,2] == ALDER) if ALDER else True
    pSTATKODE = (dd[:,3] == STATKODE) if STATKODE else True

    mask = pAAr & pBYDEL & pALDER & pSTATKODE

    return dd[mask]


#print(getPopDataOptinalParameter(AAR=2004,BYDEL=3,STATKODE=5100))

#create a new function that can also give average values for each year if year whas not provided.

def get(AAR = None,BYDEL = None, STATKODE = None,ALDER = None):
    
    
    pAAr = (dd[:,0] == AAR) if AAR else True
    pBYDEL = (dd[:,1] == BYDEL) if BYDEL else True
    pALDER = (dd[:,2] == ALDER) if ALDER else True
    pSTATKODE = (dd[:,3] == STATKODE) if STATKODE else True

    mask = pAAr & pBYDEL & pALDER & pSTATKODE

    return dd[mask]


print(getPopDataOptinalParameter(AAR=2004,BYDEL=3,STATKODE=5100))