import tweepy
import time
import os

CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
ACCESS_KEY = os.environ.get("ACCESS_KEY")
ACCESS_SECRET = os.environ.get("ACCESS_SECRET")

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

for tweet in tweepy.Cursor(api.search,
                           q="#controlroom AND #callhandler OR #callhandlers OR #emergencyservices OR #what3words OR #controlroomawards",
                           lang="en").items(5):
    try:
        print('Tweet successful')
        tweet.retweet()
        time.sleep(20)

    except tweepy.TweepError as oh_no:
        print(oh_no.reason)
    except StopIteration:
        break
