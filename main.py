import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key= 'jgKVRz2SJs7BofuVJ8yPNwa3V'
consumer_secret= 'YWo03TeQ2tUWlnn9rKzlBg1tIf41dlBegeFghmFaZW8FwXj0tz'

access_token='548398388-UPp1o1RofZkt70v8slqEbMxMvo2EIRP53CYgir5i'
access_token_secret='75xMZQCjqj3KVurlt0cJCtNe7sLsqTRMs3zu83DAT0l3w'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('CongressPresidentRahulGandhi')


for tweet in public_tweets:
    print(tweet.text)
    
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
