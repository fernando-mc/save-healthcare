#!/usr/bin/env python
import random
import json
from twython import Twython
from senators import REPUBLICANS

# Credentials setup
# Loads in 'creds.json' values as a dictionary
with open('creds.json') as f:
    credentials = json.loads(f.read())

# Sets config values from the config file
CONSUMER_KEY = credentials["consumer_key"]
CONSUMER_SECRET = credentials["consumer_secret"]
ACCESS_TOKEN_KEY = credentials["access_token_key"]
ACCESS_TOKEN_SECRET = credentials["access_token_secret"]

# Create the Twython Twitter client using our credentials
twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET,
                  ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)

# Sample random tweets
potential_tweets = [
    '{0} could you please not repeal ACA healthcare. We kind of need that. https://www.wired.com/2017/01/not-even-insurance-companies-want-obamacare-repealed/',
    'Please dont repeal the ACA {0}. The country needs it. https://www.wired.com/2017/01/not-even-insurance-companies-want-obamacare-repealed/',
]

def send_tweet():
    """
    Sends random tweet from list of potential tweets 
    and populates it with a republican twitter handle
    """
    unformatted_tweet = random.choice(potential_tweets)
    random_republican = random.choice(REPUBLICANS)
    tweet_text = unformatted_tweet.format(random_republican)
    twitter.update_status(status=tweet_text)

if __name__ == "__main__":
    send_tweet()
