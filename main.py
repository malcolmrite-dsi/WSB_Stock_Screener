from Data_Extractor import RedditExtractor as re

def main():
    reddit = re.authorise_extractor("590725")
    
    train_data = re.extract_top_data(reddit, 100)
    
    print(train_data.head())
    
    


if __name__ == '__main__':
    main()