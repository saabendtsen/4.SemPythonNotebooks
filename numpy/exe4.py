import numpy as np
import matplotlib.pyplot as plt

filename = '../../data/befkbhalderstatkode.csv'


#Open the file './data/befkbhalderstatkode.csv'
#Turn the csv file into a numpy ndarray with np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)
dd = np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)
#Using this data:
neighb = {1: 'Indre By', 2: 'Østerbro', 3: 'Nørrebro', 4: 'Vesterbro/Kgs. Enghave', 
        5: 'Valby', 6: 'Vanløse', 7: 'Brønshøj-Husum', 8: 'Bispebjerg', 9: 'Amager Øst', 
       10: 'Amager Vest', 99: 'Udenfor'}
#Find out how many people lived in each of the 11 areas in 2015

def getPopDataOrSum(BYDEL):
    mask = (dd[:,0] == 2015) & (dd[:,1] == BYDEL)
    return np.sum(dd[mask][:,4])
   

sums={}

for k,v in neighb.items():
    sums[v] = getPopDataOrSum(k)

#Make a bar plot to show the size of each city area from the smallest to the largest in 2015

sort_sums = dict(sorted(sums.items(), key=lambda item: item[1]))
#plt.bar(sort_sums.keys(),sort_sums.values())
#print(sort_sums)


#Create a boolean mask to find out how many people above 65 years lived in Copenhagen in 2015

mask_older_65 = (dd[:,0] == 2015) & (dd[:,2] > 65) 

#print(np.sum(dd[mask_older_65][:,4]))

#How many of those were from the other nordic countries (not dk). Hint: see notebook: "04 Numpy"

mask_other_denmark = (dd[:,0] == 2015) & (dd[:,2] > 65) & (dd[:,3] != 5100)

#print(np.sum(dd[mask_other_denmark][:,4]))

#Make a line plot showing the changes of number of people in vesterbro and østerbro from 1992 to 2015

mask_oester_vester = (dd[:,0] >= 1992) & (dd[:,0] <= 2015) & (dd[:,1] == 2) | (dd[:,1] == 4)

#print(dd[mask_oester_vester])
#print(list(range(1992,2016)))

#print(np.sum(dd[mask_oester_vester][:,4]))
vesterbro_sums = {}
østerbro_sums = {} 

def getAreaSum(BYDEL,ASTAL):
    mask = (dd[:,0] == ASTAL) & (dd[:,1] == BYDEL)
    return np.sum(dd[mask][:,4])

vesterbro_area = 4

osterbro_area = 2

for n in range(1992,2016):
    vesterbro_sums[n] = getAreaSum(vesterbro_area,n)

for n in range(1992,2016):
    østerbro_sums[n] = getAreaSum(osterbro_area,n)


print(vesterbro_sums.values())

#print(list(dd[mask_oester_vester][:,0]), list(np.sums(dd[mask_oester_vester][:,4])))

