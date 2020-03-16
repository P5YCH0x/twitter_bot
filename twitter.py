import tweepy
import time

auth = tweepy.OAuthHandler('API_KEY', 'API_SECRET_KEY')
auth.set_access_token('ACCESS_TOKEN','ACCESS_TOKEN_SECRET')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
user = api.me()

search = 'SEARCH'
num_of_tweets = 500

for tweet in tweepy.Cursor(api.search, search).items(num_of_tweets):
	try:
		print('favorited and retweeted a new tweet')
		tweet.favorite()
		tweet.retweet()
		time.sleep(600)
	except tweepy.TweepError as e:
		print(e.reason)
	except StopIteration:
		break
