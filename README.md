# twitter-stream

Docker container to get tweets from certain area using the Streaming API.

### Requirements:

* Docker: [https://www.docker.com](https://www.docker.com)

### Build:

* `docker build -t twitter-stream .`

### Configuration:

* Area coordinates:
    * Edit `files/twitter-stream.py` and set the coordinates of the target area modifying the following lines:
```
    # e.g. Seattle
    MIN_LON, MIN_LAT, MAX_LON, MAX_LAT = [-122.7617609, 47.3450457, -121.8910944, 47.8133273]
```
* Twitter API keys:
    * Go to [http://apps.twitter.com](http://apps.twitter.com) and create an application to get the `consumer_key`, `consumer_secret`, `access_token_key` and `access_token_secret`
    * Then set those values in `files/private_tokens.py`

### Run:

* ```docker run -d --name twitter-stream -v `pwd`/files:/files twitter-stream /files/run.sh```
* Collection will run in background
* Tweets (full JSON) will be added to the `files/tweets.json` file
* **Note**: Twitter only provides a small percentage of the tweets via the Streaming API. Look for commercial solutions (e.g. Twitter's [Gnip](https://gnip.com/sources/twitter/)) if that's not enough for your project

### Stop:

* `docker stop twitter-stream`

### Credits:

* Tweepy: [https://github.com/tweepy/tweepy](https://github.com/tweepy/tweepy)