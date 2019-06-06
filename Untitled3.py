
# coding: utf-8

# In[4]:

#--> Importing Libraries
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as mlt
import seaborn as sns


#--> read Matches file
matches=pd.read_csv(r"C:\Users\matches.csv") 
#--> print only the first 5 rows
matches.head(5) 



#--> finding the number of matches played in total
print ("Total number of matches played:", len(matches))
#--> Location of Matches, name of teams that played and the name of unique umpires
print(' \n Location for all matches: \n',matches['city'].unique(), ' \n \n Teams :',matches['team1'].unique(), '\n \nTotal umpires ',matches['umpire1'].unique()) 



# In[5]:

#--> Cleaning:remove the column with no data or consists of NaN
del matches['umpire3'] 

#--> Matches file after removing umpire3 column
matches.head(4) 


# In[6]:

#--> 
a= matches['player_of_match'].value_counts()
b= a.idxmax()

print(' Who has the highest man of the match awards', b)

c= matches['winner'].value_counts()
d=c.idxmax()
print(' Which team has won the most?\n', d)


# In[7]:

#--> 
x=matches.iloc[[matches['win_by_runs'].idxmax()]]
print('It was in', x['season'].item(),',','when the biggest score difference was', x['win_by_runs'].item(), ',', 'between', x['team1'].item(), '&', x['team2'].item(),'.' , 
      ' ','The match was won by:', x['winner'].item())


# In[8]:

#--> The graph will show the decision of fielding or batting if a team wins the toss. 
sns.countplot(y='season',hue='toss_decision',data=matches)
mlt.show()


# In[9]:


#--> The graph shows the team that won the most tosses
u=matches['toss_winner'].value_counts().plot.bar()
for l in u.patches:
    u.annotate(format(l.get_height()), (l.get_x()+0.15, l.get_height()+1))
mlt.show()


# In[10]:

#--> Probability that the toss winner will win the match
z=matches[matches['toss_winner']==matches['winner']]
slices=[len(z),(len(matches)-len(z))]
labels=['Yes','No']
mlt.pie(slices,labels=labels,autopct='%1.2f%%')
fig = mlt.gcf()
mlt.show()


# In[11]:

#--> Most popular grounds to play
ls = matches['venue'].value_counts().plot.bar(width=.8)
ls.set_xlabel('Grounds')
ls.set_ylabel('count')
mlt.show()


# In[12]:

#--> The Graph shows the top 5 most Man of the match winners
pp = matches['player_of_match'].value_counts().head(5).plot.bar( color='B')  
pp.set_xlabel('') 
pp.set_ylabel('Total')
for p in pp.patches:
    pp.annotate(format(p.get_height()), (p.get_x()+0.15, p.get_height()+0.25))
mlt.show()

