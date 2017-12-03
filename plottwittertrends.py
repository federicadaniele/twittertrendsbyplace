from mpl_toolkits.basemap import Basemap
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
import csv

# Open csv file with coordinates, statistics you want to plot by location:
with open('finalplot22112017.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=",")
    your_list = list(spamreader)
    result = np.array(your_list).astype("float")
    
# Generate array per each variable:
# generate arrays:
lats =[]
lons =[]
popo =[]
ranking =[]
disagre =[]
devi =[]
woei =[]

for i in result:
    woei.append(i[1])
    lats.append(i[2])
    lons.append(i[3])
    popo.append(i[4])
    ranking.append(i[0])
    disagre.append(i[5])

disagreement = 0
if disagreement == 0:
    stat = ranking
elif disagreement == 1:
    stat = disagre
# print how many cities:
print(stat)
# print stat:
print(len(stat))
# print quartiles of stat:
print(np.percentile(stat,25))
print(np.percentile(stat,50))
print(np.percentile(stat,75))

# Draw map:
plt.figure(figsize=(12,6))
map = Basemap(llcrnrlon = -140,llcrnrlat = 18,urcrnrlon = -60,urcrnrlat = 55,resolution='i')
map.readshapefile('cb_2016_us_state_5m', 'cb_2016_us_state_5m')
map.fillcontinents(color='#ddaa66',alpha = 0.5)
map.drawcoastlines()

if disagreement == 0:
    colorVotes = plt.get_cmap('Greens')
elif disagreement == 1:
    colorVotes = plt.get_cmap('Blues')

# Vector of city names:
city = ['Albuquerque','Atlanta','Baltimore','Birmingham','Boston','Charlotte','Chicago','Columbus','Denver','Detroit',\
        'Houston','Indianapolis','Jacksonville','Las Vegas','Los Angeles','Louisville','Memphis','Milwaukee','Minneapolis',\
        'New Orleans','New York City','Oklahoma City','Omaha','Philadelphia','Phoenix','Portland','Seattle','Virginia Beach']

lats1 = []
lats2 = []
lats3 = []
lats4 = []

lons1 = []
lons2 = []
lons3 = []
lons4 = []

stat1 = []
stat2 = []
stat3 = []
stat4 = []

city1 = []
city2 = []
city3 = []
city4 = []

for i in range(1,len(lons)+1):
    n = i-1
    if popo[n]<np.percentile(popo,25):
        lons1.append(lons[n])
        lats1.append(lats[n])
        stat1.append(stat[n])
        city1.append(city[n])
    elif popo[n]>=np.percentile(popo,25) and popo[n]<np.percentile(popo,50):
        lons2.append(lons[n])
        lats2.append(lats[n])
        stat2.append(stat[n])
        city2.append(city[n])
    elif popo[n]>=np.percentile(popo,50) and popo[n]<np.percentile(popo,75):
        lons3.append(lons[n])
        lats3.append(lats[n])
        stat3.append(stat[n])
        city3.append(city[n])
    else:
        lons4.append(lons[n])
        lats4.append(lats[n])
        stat4.append(stat[n])  
        city4.append(city[n])   

check1 = 1
check2 = 1
check3 = 1
check4 = 1

for i in range(1,len(lons1)+1):
    n = i-1
    x, y = map(lons1[n], lats1[n])    
    plt.text(x, y,city1[n],fontsize=9,fontweight='bold',
        ha='left',va='bottom',color='k')
    
    if stat1[n]<np.percentile(stat,25):
        colorr = colorVotes(4/4)
        if check1 == 1:
            map.plot(x, y, marker='.',color=colorr,markersize=20,label="High Rank")
            check1 = 0
        elif check1 == 0:
            map.plot(x, y, marker='.',color=colorr,markersize=20)
            
    elif stat1[n]>=np.percentile(stat,25) and stat1[n]<np.percentile(stat,50):
        colorr = colorVotes(3/4)
        
        if check2 == 1:
            map.plot(x, y, marker='.',color=colorr,markersize=20,label="High/Mid Rank")
            check2 = 0
        elif check2 == 0:
            map.plot(x, y, marker='.',color=colorr,markersize=20)
            
    elif stat1[n]>=np.percentile(stat,50) and stat1[n]<np.percentile(stat,75):
        colorr = colorVotes(2/4)
        
        if check3 == 1:
            map.plot(x, y, marker='.',color=colorr,markersize=20,label="Low/Mid Rank")   
            check3 = 0
        elif check3 == 0:
            map.plot(x, y, marker='.',color=colorr,markersize=20)
        
    elif stat1[n]>=np.percentile(stat,75):
        colorr = colorVotes(1/4)
        
        if check4 == 1:
            map.plot(x, y, marker='.',color=colorr,markersize=20,label="Low Rank")   
            check4 = 0
        elif check4 == 0:
            map.plot(x, y, marker='.',color=colorr,markersize=20)

for i in range(1,len(lons2)+1):
    n = i-1
    x, y = map(lons2[n], lats2[n])    
    plt.text(x, y,city2[n],fontsize=9,fontweight='bold',
        ha='left',va='bottom',color='k')
        
    if stat2[n]<np.percentile(stat,25):
        colorr = colorVotes(4/4)  
        if check1 == 1:
            map.plot(x, y, marker='.',color=colorr,markersize=30,label="High Rank")
            check1 = 0
        elif check1 == 0:
            map.plot(x, y, marker='.',color=colorr,markersize=30)
            
    elif stat2[n]>=np.percentile(stat,25) and stat2[n]<np.percentile(stat,50):
        colorr = colorVotes(3/4)
        
        if check2 == 1:
            map.plot(x, y, marker='.',color=colorr,markersize=30,label="High/Mid Rank")
            check2 = 0
        elif check2 == 0:
            map.plot(x, y, marker='.',color=colorr,markersize=30)
            
    elif stat2[n]>=np.percentile(stat,50) and stat2[n]<np.percentile(stat,75):
        colorr = colorVotes(2/4)
        
        if check3 == 1:
            map.plot(x, y, marker='.',color=colorr,markersize=30,label="Low/Mid Rank")   
            check3 = 0
        elif check3 == 0:
            map.plot(x, y, marker='.',color=colorr,markersize=30)
        
    elif stat2[n]>=np.percentile(stat,75):
        colorr = colorVotes(1/4)
        
        if check4 == 1:
            map.plot(x, y, marker='.',color=colorr,markersize=30,label="Low Rank")   
            check4 = 0
        elif check4 == 0:
            map.plot(x, y, marker='.',color=colorr,markersize=30)

for i in range(1,len(lons3)+1):
    n = i-1
    x, y = map(lons3[n], lats3[n])    
    plt.text(x, y,city3[n],fontsize=9,fontweight='bold',
        ha='left',va='bottom',color='k')

    if stat3[n]<np.percentile(stat,25):
        colorr = colorVotes(4/4)
        
        if check1 == 1:
            map.plot(x, y, marker='.',color=colorr,markersize=40,label="High Rank")
            check1 = 0
        elif check1 == 0:
            map.plot(x, y, marker='.',color=colorr,markersize=40)
            
    elif stat3[n]>=np.percentile(stat,25) and stat3[n]<np.percentile(stat,50):
        colorr = colorVotes(3/4)
        
        if check2 == 1:
            map.plot(x, y, marker='.',color=colorr,markersize=40,label="High/Mid Rank")
            check2 = 0
        elif check2 == 0:
            map.plot(x, y, marker='.',color=colorr,markersize=40)
            
    elif stat3[n]>=np.percentile(stat,50) and stat3[n]<np.percentile(stat,75):
        colorr = colorVotes(2/4)
        
        if check3 == 1:
            map.plot(x, y, marker='.',color=colorr,markersize=40,label="Low/Mid Rank")   
            check3 = 0
        elif check3 == 0:
            map.plot(x, y, marker='.',color=colorr,markersize=40)
        
    elif stat2[n]>=np.percentile(stat,75):
        colorr = colorVotes(1/4)
        
        if check4 == 1:
            map.plot(x, y, marker='.',color=colorr,markersize=40,label="Low Rank")   
            check4 = 0
        elif check4 == 0:
            map.plot(x, y, marker='.',color=colorr,markersize=40)
            
for i in range(1,len(lons4)+1):
    n = i-1
    x, y = map(lons4[n], lats4[n])    
    plt.text(x, y,city4[n],fontsize=9,fontweight='bold',
        ha='left',va='bottom',color='k')
    
    if stat4[n]<np.percentile(stat,25):
        colorr = colorVotes(4/4)
        
        if check1 == 1:
            map.plot(x, y, marker='.',color=colorr,markersize=50,label="High Disagreement")   
            check1 = 0
        elif check1 == 0:
            map.plot(x, y, marker='.',color=colorr,markersize=50)
            
    elif stat4[n]>=np.percentile(stat,25) and stat4[n]<np.percentile(stat,50):
        colorr = colorVotes(3/4)
        
        if check2 == 1:
            map.plot(x, y, marker='.',color=colorr,markersize=50,label="High/Mid Disagreement")   
            check2 = 0
        elif check2 == 0:
            map.plot(x, y, marker='.',color=colorr,markersize=50)
            
    elif stat4[n]>=np.percentile(stat,50) and stat4[n]<np.percentile(stat,75):
        colorr = colorVotes(2/4)
        
        if check3 == 1:
            map.plot(x, y, marker='.',color=colorr,markersize=50,label="Low/Mid Disagreement")   
            check3 = 0
        elif check3 == 0:
            map.plot(x, y, marker='.',color=colorr,markersize=50)
        
    elif stat4[n]>=np.percentile(stat,75):
        colorr = colorVotes(1/4)
        
        if check4 == 1:
            map.plot(x, y, marker='.',color=colorr,markersize=50,label="Low Disagreement")   
            check4 = 0
        elif check4 == 0:
            map.plot(x, y, marker='.',color=colorr,markersize=50)
            
lgnd = plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=3, mode="expand", borderaxespad=0.)
lgnd.legendHandles[0]._legmarker.set_markersize(6)
lgnd.legendHandles[1]._legmarker.set_markersize(6)
lgnd.legendHandles[2]._legmarker.set_markersize(6)
lgnd.legendHandles[3]._legmarker.set_markersize(6)

# Save figure:
if disagreement == 0:
    plt.savefig('fig_ranking.png')
elif disagreement == 1:
    plt.savefig('fig_disagre.png')
plt.show()
    