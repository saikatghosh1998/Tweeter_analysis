import tweepy
from textblob import TextBlob

consumer_key='YnrWFco5LwHawRPo71SxKwCD0'
consumer_secret='vAFXCqcwrzOluveWnfdTdN5BZ5gJr87Ptrs6pAKROaBCC9KoEr'
access_token='3Jpa4KRb4gyBOx65dApj9Q0fg5vzWWfXqDVgl7QjpZi8K'
access_token_secret='778211905005424641-wTKTYmNrbcjMCodaSiOyRTsMUV6hx7N'
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token_secret,access_token)
#auth.set_access_token(778211905005424641-wTKTYmNrbcjMCodaSiOyRTsMUV6hx7N,3Jpa4KRb4gyBOx65dApj9Q0fg5vzWWfXqDVgl7QjpZi8K)

api = tweepy.API(auth)
positive=[]
negative=[]
neutral=[]
def get_tweet_sentiment(tweet):

		analysis = TextBlob(tweet)
		# set sentiment
		if analysis.sentiment.polarity > 0:
			return 'positive'
		elif analysis.sentiment.polarity == 0:
			return 'neutral'
		else:
			return 'negative'


def get_tweets(query):

		tweets = []
		#fetched_tweets = self.api.search(q = query, count = count)
		for tweet in tweepy.Cursor(api.search,q=query,lang="en").items(20):
			parsed_tweet = {}
			parsed_tweet['text'] = tweet.text
			parsed_tweet['sentiment'] = get_tweet_sentiment(tweet.text)
			tweets.append(parsed_tweet)
			#print(parsed_tweet)
		return tweets

def main(query):
    tweets=get_tweets(query)
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    #print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets)))
    netweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'neutral']
	
    for tweet in tweets:
        if tweet['sentiment']=='positive':
            p = tweet['text']
            positive.append(p)
		
        if tweet['sentiment']=='negative':
            p = tweet['text']
            negative.append(p)

		
			#positive.append(p)
           # print(p)
    return tweets
    #for p in ptweets:
     #   print(p['text'])


if __name__ == "__main__":
	main(query)
	
    