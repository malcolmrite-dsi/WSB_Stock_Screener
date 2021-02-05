
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
#For Reference: https://praw.readthedocs.io/en/latest/getting_started/quick_start.html
print(reddit.read_only)

# assume you have a reddit instance bound to variable `reddit`
#Setting the subreddit to wallstreetbets
subreddit = reddit.subreddit("wallstreetbets")

#Validate that the subreddit extractor is working
print(subreddit.display_name)
print(subreddit.title)
print(reddit.user.me())

#Getting example submissions from the subreddit
for submission in subreddit.top(limit=15):
    print(submission.title)  # Output: the submission's title
    print(submission.score)  # Output: the submission's score
    print(submission.id)     # Output: the submission's ID
    print(submission.url)    # Output: the URL the submission points to
                             # or the submission's URL if it's a self post

#Create a dictionary to store the data   
                             
topics_dict = { "title":[], \
                "score":[], \
                "id":[], \
                "url":[], \
                "comms_num": [], \
                "created": [], \
                "body":[]}

#Extractt
top_subreddit = subreddit.top(limit=500)


for submission in top_subreddit:
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["url"].append(submission.url)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["created"].append(submission.created)
    topics_dict["body"].append(submission.selftext)
    



