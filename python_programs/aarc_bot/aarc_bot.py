import keys
import personality01
from tweepy import *
from TwitterSearch import *

auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)

try:
    redirect_url = auth.get_authorization_url()

except tweepy.TweepError:
    print("Error! Failed to get request token.")

api = tweepy.API(auth)

public_tweets = api.user_timeline()
for tweet in public_tweets:
    print(tweet.text, "\n")
