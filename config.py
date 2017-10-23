from pandas import read_csv

DEBUG = True

creds = read_csv('credentials.csv')

TWITTER_CONSUMER_KEY = creds.consumer_key[0]
#TWITTER_CONSUMER_KEY = 'poop'
TWITTER_CONSUMER_SECRET = creds.consumer_secret[0]
TWITTER_ACCESS_TOKEN = creds.access_token[0]
TWITTER_ACCESS_TOKEN_SECRET = creds.access_token_secret[0]
