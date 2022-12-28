# Author: Preet Dabhi
# Purpose : dabhi.py is used to analyze a social network dataset
# To run from terminal window:   python3 dabhi.py 

import pandas as pd
import matplotlib.pyplot as plt
import csv 
from tabulate import tabulate

# reading the csv file using pandas
df = pd.read_csv('Pew_survey.csv')

testage=[]
testinternetusage=[]
# iterating through the csv file to store the age and internet usage.
with open('Pew_Survey.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        testage.append(row[23])
        testinternetusage.append(row[1])
# sorting the array for better visualization
testage.sort()
testinternetusage.sort()
bins = 5

#countinf each of the unique values of each column 
internetuage = df['intfreq'].value_counts()
socialmeidausage =df['snsint2'].value_counts()
cellorother =df['q20'].value_counts()

twCnt=df['web1a'].value_counts()
inCnt=df['web1b'].value_counts()
fbCnt=df['web1c'].value_counts()
scCnt=df['web1d'].value_counts()
ytCnt=df['web1e'].value_counts()
waCnt=df['web1f'].value_counts()
piCnt=df['web1g'].value_counts()
liCnt=df['web1h'].value_counts()
reCnt=df['web1i'].value_counts()

twusage=df['sns2a'].value_counts()
inusage=df['sns2b'].value_counts()
fbusage=df['sns2c'].value_counts()
scusage=df['sns2d'].value_counts()
ytusage=df['sns2e'].value_counts()

device1b=df['device1b'].value_counts()
device1c=df['device1c'].value_counts()
device1d=df['device1d'].value_counts()
cregion=df['cregion'].value_counts()
sex=df['sex'].value_counts()
age=df['age'].value_counts()
marital = df['marital'].value_counts()

educ2 =df['educ2'].value_counts()
emplnw =df['emplnw'].value_counts()
inc =df['inc'].value_counts()
party =df['party'].value_counts()
partyln =df['partyln'].value_counts()

# histogram plot of how often one uses the internet
plt.hist(testinternetusage,bins = bins, edgecolor = 'black')
plt.title("how often do you use the internet? 1 being most frequent and 9 being the lowest")
plt.show()

# printing the data in tabular form
a = [ ["Almost constantly", internetuage[2]],
     ["Several times a day", internetuage[1]],
     ["About once a day", internetuage[3]],
     ["Several times a week", internetuage[4]],
     ["Less often", internetuage[5]],
     ["Dont know", internetuage[8]],
     ["Refused", internetuage[9]]]

print(tabulate(a, headers=["Internet Usage", "Count"]))

test = pd.DataFrame({'Use':['Almost constantly', 'Several times a day ','About once a day','Several times a week','Less often','Dont know','Refused'], 'val':[internetuage[2], internetuage[1],internetuage[3],internetuage[4],internetuage[5],internetuage[8],internetuage[9]]})
test.plot.bar(x='Use', y='val', rot=0)
plt.show()

# printing the data in tabular form
b = [ ["Y", socialmeidausage[1]],
     ["N", socialmeidausage[2]]]
print("-------------------")
print(tabulate(b, headers=["UseSocial", "Count"]))

test3 =pd.DataFrame({'UseSocial':['Y','N'], 'val':[socialmeidausage[1],socialmeidausage[2]]})
test3.plot.bar(x='UseSocial', y='val', rot=0)
plt.show()

# printing the data in tabular form
c = [ ["Male", sex[1]],
     ["Female", sex[2]]]
print("-------------------")
print(tabulate(c, headers=["Gender", "Count"]))

# bar plotting of gender
test1 = pd.DataFrame({'Sex':['M', 'F'], 'val':[sex[1], sex[2]]})
test1.plot.bar(x='Sex', y='val', rot=0)
plt.show()

# printing the data in tabular form
d = [ ["Twitter", twCnt[2],twCnt[1]],
     ["Instagram", inCnt[2],inCnt[1]],
     ["Facebook", fbCnt[1],fbCnt[2]],
     ["SnapChat", scCnt[2],scCnt[1]],
     ["YouTube", ytCnt[1],ytCnt[2]],
     ["WhatsApp", waCnt[2],waCnt[1]],
     ["Pintrest", piCnt[2],piCnt[1]],
     ["LinkedIn", liCnt[2],liCnt[1]],
     ["Reddit", reCnt[2],reCnt[1]]]
print("-------------------")
print(tabulate(d, headers=["Platform", "Yes","No"]))

# plotting a pie chart of number of Pleople Using Social Media
OSN_names = [ 'Twitter','Instagram', 'Facebook', 'SnapChat','YouTube','WhatsApp','Pintrest', 'LinkedIn', 'Reddit']
OSN_numbers =[twCnt[1], inCnt[1], fbCnt[1], scCnt[1], ytCnt[1], waCnt[1], piCnt[1] ,liCnt[1],reCnt[1]]

plt.pie(OSN_numbers, labels=OSN_names)
plt.title('Pleople Using Social Media')
plt.show()

# printing the data in tabular form
e = [ 
     ["Several times a day", twusage[0]],
     ["About once a day", twusage[1]],
     ["A few times a week", twusage[2]],
     ["Every few weeks", twusage[3]],
     ["Less often", twusage[4]],
     ["Dont know", twusage[5]],
     ["Refused", twusage[6]]]
print("-------------------")
print(tabulate(e, headers=["how often do you use Twitter?", "Count"]))


# plotting a pie chart of number of how often do you use Twitter?
Twitter_names = [ 'Several times a day','About once a day ', 'A few times a week ', 'Every few weeks ','Less often','Dont know','Refused']
Twtter_numbers =[twusage[0], twusage[1], twusage[2], twusage[3], twusage[4], twusage[5], twusage[6]]

plt.pie(Twtter_numbers, labels=Twitter_names)
plt.title('how often do you use Twitter?')
plt.show()

# printing the data in tabular form
f = [ 
     ["Several times a day", inusage[0]],
     ["About once a day", inusage[1]],
     ["A few times a week", inusage[2]],
     ["Every few weeks", inusage[3]],
     ["Less often", inusage[4]],
     ["Dont know", inusage[5]]]
print("-------------------")
print(tabulate(f, headers=["how often do you use Instagram?", "Count"]))

# plotting a pie chart of number of how often do you use Instagram?
Instagram_names = [ 'Several times a day','About once a day ', 'A few times a week ', 'Every few weeks ','Less often','Dont know']
Instagram_numbers =[inusage[0], inusage[1], inusage[2], inusage[3], inusage[4], inusage[5]]

plt.pie(Instagram_numbers, labels=Instagram_names)
plt.title('how often do you use Instagram?')
plt.show()

# printing the data in tabular form
g = [ 
     ["Several times a day", fbusage[0]],
     ["About once a day", fbusage[1]],
     ["A few times a week", fbusage[2]],
     ["Every few weeks", fbusage[3]],
     ["Less often", fbusage[4]],
     ["Dont know", fbusage[5]],
      ["Refused", fbusage[6]]]
print("-------------------")
print(tabulate(g, headers=["how often do you use Facebook?", "Count"]))

# plotting a pie chart of number of how often do you use Facebook?
Facebook_names = [ 'Several times a day','About once a day ', 'A few times a week ', 'Every few weeks ','Less often','Dont know','Refused']
Facebook_numbers =[fbusage[0], fbusage[1], fbusage[2], fbusage[3], fbusage[4], fbusage[5], fbusage[6]]

plt.pie(Facebook_numbers, labels=Facebook_names)
plt.title('how often do you use Facebook?')
plt.show()

# printing the data in tabular form
h = [ 
     ["Several times a day", scusage[0]],
     ["About once a day", scusage[1]],
     ["A few times a week", scusage[2]],
     ["Every few weeks", scusage[3]],
     ["Less often", scusage[4]],
     ["Dont know", scusage[5]]]
print("-------------------")
print(tabulate(h, headers=["how often do you use Snapchat?", "Count"]))

# plotting a pie chart of number of how often do you use Snapchat?
Snapchat_names = [ 'Several times a day','About once a day ', 'A few times a week ', 'Every few weeks ','Less often','Dont know']
Snapchat_numbers =[scusage[0], scusage[1], scusage[2], scusage[3], scusage[4], scusage[5]]

plt.pie(Snapchat_numbers, labels=Snapchat_names)
plt.title('how often do you use Snapchat?')
plt.show()

# printing the data in tabular form
i = [ 
     ["Several times a day", ytusage[0]],
     ["About once a day", ytusage[1]],
     ["A few times a week", ytusage[2]],
     ["Every few weeks", ytusage[3]],
     ["Less often", ytusage[4]],
     ["Dont know", ytusage[5]],
      ["Refused", ytusage[6]]]
print("-------------------")
print(tabulate(i, headers=["how often do you use YouTube?", "Count"]))

# plotting a pie chart of number of how often do you use YouTube?
YouTube_names = [ 'Several times a day','About once a day ', 'A few times a week ', 'Every few weeks ','Less often','Dont know','Refused']
YouTube_numbers =[ytusage[0], ytusage[1], ytusage[2], ytusage[3], ytusage[4], ytusage[5], ytusage[6]]

plt.pie(YouTube_numbers, labels=YouTube_names)
plt.title('how often do you use YouTube?')
plt.show()

# printing the data in tabular form
j = [ 
     ["Less than $10,000 ", inc[1]],
     ["10 to under $20,000 ", inc[2]],
     ["20 to under $30,000", inc[3]],
     ["30 to under $40,000", inc[4]],
     ["40 to under $50,000 ", inc[5]],
     ["50 to under $75,000  ", inc[6]],
      ["75 to under $100,000 ", inc[7]],
      ["100 to under $150,000  ", inc[8]],
      ["$150,000 or more  ", inc[9]],
      ["Don't know", inc[98]],
      ["Refused", inc[99]]]
print("-------------------")
print(tabulate(j, headers=["Total 2018 family income before taxes", "Count"]))

#plotting a bar graph of Total 2018 family income before taxes
inc.plot.bar(stacked=True)
plt.title('Total 2018 family income before taxes')
plt.show()

# plotting the age distribution through histogram
plt.hist(testage,bins = bins, edgecolor = 'black')
plt.title("Age distribution histogram")
plt.show()