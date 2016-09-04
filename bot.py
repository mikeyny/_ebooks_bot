import markovify ,tweepy ,io
from secrets import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
with io.open("Text\jokes.txt", encoding="utf-8") as f:
	text = f.read()

# Build the model.
text_model = markovify.Text(text)

# generate a random sentences of no more than 140 characters(a tweet)
message =text_model.make_short_sentence(140)

#post your tweet
api.update_status(message)