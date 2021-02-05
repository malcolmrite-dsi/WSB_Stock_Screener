
#Importing the Libraries
import praw
import pandas as pd
import datetime as dt


class RedditExtractor():
    def authorise_extractor(twofactorcode):
        #Initialising the credentials for the API
        reddit = praw.Reddit(client_id='1h1Pkh53dcBSLA', \
                             client_secret='Lm4-BO2A5GpHoYnzEUEMMLOoH1TpIw', \
                             user_agent='Reddit_Stock by u/Get_Rich_Bot', \
                             username='Get_Rich_Bot', \
                             password= f'B+4H-5yww=<QJUV:{twofactorcode}')
        return reddit
    
    
    def test_extractor(self):
        #Testing if the authorisation worked
        #For Reference: https://praw.readthedocs.io/en/latest/getting_started/quick_start.html
        print(self.read_only)
        
        # assume you have a reddit instance bound to variable `reddit`
        #Setting the subreddit to wallstreetbets
        subreddit = self.subreddit("wallstreetbets")
        
        #Validate that the subreddit extractor is working
        print(subreddit.display_name)
        print(subreddit.title)
        print(self.user.me())
        
        #Getting example submissions from the subreddit
        for submission in subreddit.top(limit=15):
            print(submission.title)  # Output: the submission's title
            print(submission.score)  # Output: the submission's score
            print(submission.id)     # Output: the submission's ID
            print(submission.url)    # Output: the URL the submission points to
                                     # or the submission's URL if it's a self post
    
    #For Reference: https://www.storybench.org/how-to-scrape-reddit-with-python/
    def get_date(created):
            return dt.datetime.fromtimestamp(created)
        
    #Returns a dataframe of the top reddit posts from WSB
    def extract_top_data(self, posts):
        #Setting the subreddit to wallstreetbets
        subreddit = self.subreddit("wallstreetbets")
        #Create a dictionary to store the data   
                                     
        topics_dict = { "title":[], \
                        "score":[], \
                        "id":[], \
                        "url":[], \
                        "comms_num": [], \
                        "created": [], \
                        "body":[]}
        
        #Extract the top posts with an upper limit defined by the user
        top_subreddit = subreddit.top(limit=posts)
        
        #Extract the relevant data from the subreddit
        for submission in top_subreddit:
            topics_dict["title"].append(submission.title)
            topics_dict["score"].append(submission.score)
            topics_dict["id"].append(submission.id)
            topics_dict["url"].append(submission.url)
            topics_dict["comms_num"].append(submission.num_comments)
            topics_dict["created"].append(submission.created)
            topics_dict["body"].append(submission.selftext)
            
        topics_data = pd.DataFrame(topics_dict)
        
        _timestamp = topics_data["created"].apply(RedditExtractor.get_date)
        topics_data = topics_data.assign(timestamp = _timestamp)
    
        return topics_data



