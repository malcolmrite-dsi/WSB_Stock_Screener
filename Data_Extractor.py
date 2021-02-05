
#Importing the Libraries
import praw
import pandas as pd
import datetime as dt

#Initialising the credentials for the API
reddit = praw.Reddit(client_id='1h1Pkh53dcBSLA', \
                     client_secret='Lm4-BO2A5GpHoYnzEUEMMLOoH1TpIw', \
                     user_agent='Reddit_Stock by u/Get_Rich_Bot', \
                     username='Get_Rich_Bot', \
                     password='B+4H-5yww=<QJUV')

#Testing if the authorisation worked
print(reddit.read_only)

# assume you have a reddit instance bound to variable `reddit`
#Setting the subreddit to wallstreetbets
subreddit = reddit.subreddit("wallstreetbets")

#Validate that the subreddit extractor is working
print(subreddit.display_name)
print(subreddit.title)