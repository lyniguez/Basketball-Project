
# coding: utf-8

# In[1]:

# from urllib.request import urlopen, Request, URLError
import os
import json
import pandas as pd
import numpy as np
import requests
import collections
import time
import matplotlib.pyplot as plt


# In[2]:

# store nba_teams in a list by their unique team_id

nba_teams = [1610612737,1610612738,1610612751,1610612766,1610612741,1610612739,1610612742,1610612743,1610612765,
             1610612744,1610612745,1610612754,1610612746,1610612747,1610612763,1610612748,1610612749,1610612750,
             1610612740,1610612752,1610612760,1610612753,1610612755,1610612756,1610612757,1610612758,1610612759,
             1610612761,1610612762,1610612764]


# In[5]:

# create for loop to request TeamSportsVU Data from api.probasketball.api

for nba_team in nba_teams:
    
    url_1='http://api.probasketballapi.com/sportsvu/team'
    api_key='H5Mif6zr1Nmjt9A8XgEcF4DVB0SsPKxQ'

    payload = {'api_key': api_key, 'team_id': nba_team}
    r = requests.post(url_1, data=payload)
    
    # print (r.text)
    # store and save data into a json file
    # * original data request taken on Dec 13 2017


# In[6]:

# read final_team_svu.json data into pandas
final_svu_df = pd.read_json("final_team_svu.json")


# In[7]:

final_svu_df.shape


# In[8]:

final_svu_df.head()


# In[9]:

final_svu_df.tail()


# In[11]:

# team name: team_id key:value pairs
team_dictionary = {'Atlanta Hawks':1610612737,
'Boston Celtics':1610612738,
'Brooklyn Nets':1610612751,
'Charlotte Hornets':1610612766,
'Chicago Bulls':1610612741,
'Cleveland Cavaliers':1610612739,
'Dallas Mavericks':1610612742,
'Denver Nuggets':1610612743,
'Detroit Pistons':1610612765,
'Golden State Warriors':1610612744,
'Houston Rockets':1610612745,
'Indiana Pacers':1610612754,
'Los Angeles Clippers':1610612746,
'Los Angeles Lakers':1610612747,
'Memphis Grizzlies':1610612763,
'Miami Heat':1610612748,
'Milwaukee Bucks':1610612749,
'Minnesota Timberwolves':1610612750,
'New Orleans Pelicans':1610612740,
'New York Knicks':1610612752,
'Oklahoma City Thunder':1610612760,
'Orlando Magic':1610612753,
'Philadelphia 76ers':1610612755,
'Phoenix Suns':1610612756,
'Portland Trail Blazers':1610612757,
'Sacramento Kings':1610612758,
'San Antonio Spurs':1610612759,
'Toronto Raptors':1610612761,
'Utah Jazz':1610612762,
'Washington Wizards':1610612764}


# In[12]:

# create function to assign team name based on team_id
def team_label (row):
    if row ['team_id'] == 1610612737:
        return "Hawks"
    if row ['team_id'] == 1610612738:
        return "Celtics"
    if row ['team_id'] == 1610612751:
        return "Nets"
    if row ['team_id'] == 1610612766:
        return "Hornets"
    if row ['team_id'] == 1610612739:
        return "Cavaliers"
    if row ['team_id'] == 1610612742:
        return "Mavericks"
    if row ['team_id'] == 1610612743:
        return "Nuggets"
    if row ['team_id'] == 1610612765:
        return "Pistons"
    if row ['team_id'] == 1610612744:
        return "Warriors"
    if row ['team_id'] == 1610612745:
        return "Rockets"
    if row ['team_id'] == 1610612754:
        return "Pacers"
    if row ['team_id'] == 1610612746:
        return "Clippers"
    if row ['team_id'] == 1610612747:
        return "Lakers"
    if row ['team_id'] == 1610612763:
        return "Grizzlies"
    if row ['team_id'] == 1610612748:
        return "Heat"
    if row ['team_id'] == 1610612749:
        return "Bucks"
    if row ['team_id'] == 1610612750:
        return "Timberwolves"
    if row ['team_id'] == 1610612740:
        return "Pelicans"
    if row ['team_id'] == 1610612752:
        return "Knicks"
    if row ['team_id'] == 1610612760:
        return "Thunder"
    if row ['team_id'] == 1610612753:
        return "Magic"
    if row ['team_id'] == 1610612755:
        return "76ers"
    if row ['team_id'] == 1610612756:
        return "Suns"
    if row ['team_id'] == 1610612757:
        return "Trail Blazers"
    if row ['team_id'] == 1610612758:
        return "Kings"
    if row ['team_id'] == 1610612759:
        return "Spurs"
    if row ['team_id'] == 1610612761:
        return "Raptors"
    if row ['team_id'] == 1610612762:
        return "Jazz"
    if row ['team_id'] == 1610612764:
        return "Wizards"


# In[13]:

# test function to see if team_labels were applied to columns
# final_svu_df.apply (lambda row: team_label (row), axis=1)


# In[14]:

# create new "team" column and apply function to populate column values w/ team names
final_svu_df['team'] = final_svu_df.apply (lambda row: team_label (row), axis=1)


# In[15]:

final_svu_df.head()


# In[16]:

final_svu_df.tail()


# In[17]:

# save Data Frame to csv
final_svu_df.to_csv("final_svu_teams.csv")


# In[18]:

# test filter to make sure unique team name was added correctly
lakers_filter = final_svu_df[final_svu_df['team']== 'Lakers']
lakers_filter.head()


# In[ ]:



