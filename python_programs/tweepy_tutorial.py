import tweepy
import keys

auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret) 
auth.set_access_token(keys.access_token, keys.access_token_secret)

api = tweepy.API(auth)
    
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text, "\n"
    
     

try:
    redirect_url = auth.get_authorization_url()

except tweepy.TweepError:
    print "Error! Failed to get request token."
