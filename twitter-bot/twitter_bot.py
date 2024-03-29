import tweepy
import time
import os


CON_KEY = os.getenv("CONSUMER_KEY")
CON_SECRET = os.getenv("CONSUMER_SECRET")
ACC_KEY = os.getenv("ACCESS_KEY")
ACC_SECRET = os.getenv("ACCESS_SECRET")

auth = tweepy.OAuthHandler(CON_KEY, CON_SECRET)
auth.set_access_token(ACC_KEY, ACC_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

for tweet in tweepy.Cursor(api.search,
                           q="#callhandlers OR #callhandler OR #ControlRoomAwards OR #heroesinheadsets OR #policecontrolroom OR #PolScotControl OR #scotamb OR #teamhumberside OR #ControlRoomHeroes OR #ProtectingAndServingEssex OR #fireandrescue OR #999family",
                           lang="en").items(10):
    try:
        print('Tweet successful')
        tweet.retweet()
        time.sleep(20)

    except tweepy.TweepError as oh_no:
        print(oh_no.reason)
    except StopIteration:
        break
