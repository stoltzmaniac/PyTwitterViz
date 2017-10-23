from flask import Flask, json, request, render_template
from tweepy import OAuthHandler, Stream, StreamListener, API

app = Flask(__name__)
# Load our config from an object, or module (config.py)
app.config.from_object('config')

# These config variables come from 'config.py'
auth = OAuthHandler(app.config['TWITTER_CONSUMER_KEY'],
                           app.config['TWITTER_CONSUMER_SECRET'])
auth.set_access_token(app.config['TWITTER_ACCESS_TOKEN'],
                      app.config['TWITTER_ACCESS_TOKEN_SECRET'])
tweepy_api = API(auth)

@app.route('/')
def hello_world():
    return "<h1>Hello World</h1>"



def get_tweets(username):
    tweets = tweepy_api.user_timeline(screen_name=username)
    return [{'tweet': t.text,
              'created_at': t.created_at,
              'username': username,
              'headshot_url': t.user.profile_image_url}
           for t in tweets]



@app.route('/tweet-harvester/<string:username>')
def tweets(username):
  # 'tweets' is passed as a keyword-arg (**kwargs)
  # **kwargs are bound to the 'tweets.html' Jinja Template context
  return render_template("tweets.html", tweets=get_tweets(username))


