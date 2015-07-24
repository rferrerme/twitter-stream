"""
Requires: tweepy

Get tweets using a geographic filter.
"""

import tweepy
from tweepy.utils import import_simplejson

json = import_simplejson()

class StreamListener(tweepy.StreamListener):
    
    def __init__(self, on_tweet):
        self.on_tweet = on_tweet

    def on_status(self, tweet):
        pass

    def on_error(self, status_code):
        return False

    def on_data(self, data):
        if data[0].isdigit():
            pass
        else:
            data = json.loads(data)
            self.on_tweet(data)

class TwitterStream:

    # on_tweet will receive json decoded data
    def __init__(self, consumer_key, consumer_secret, access_token_key, access_token_secret, min_lon, min_lat, max_lon, max_lat, on_tweet):
        auth1 = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth1.set_access_token(access_token_key, access_token_secret)
        l = StreamListener(on_tweet)
        streamer = tweepy.Stream(auth=auth1, listener=l)
        streamer.filter(locations=[min_lon, min_lat, max_lon, max_lat])

if __name__ == "__main__":

    from private_tokens import consumer_key, consumer_secret, access_token_key, access_token_secret
    
    # e.g. Seattle
    MIN_LON, MIN_LAT, MAX_LON, MAX_LAT = [-122.7617609, 47.3450457, -121.8910944, 47.8133273]

    OUTPUT_FILENAME = "tweets.json"

    # Append to file
    f = open(OUTPUT_FILENAME, "a")

    def on_tweet(json_data):
        geo = json_data.get('coordinates', None)
        # It can be geo_enabled but e.g. only provide country information so require "Point"
        if geo and geo['type'] == 'Point':
            print >>f, json_data
            f.flush()

    TwitterStream(consumer_key, consumer_secret, access_token_key, access_token_secret, MIN_LON, MIN_LAT, MAX_LON, MAX_LAT, on_tweet)