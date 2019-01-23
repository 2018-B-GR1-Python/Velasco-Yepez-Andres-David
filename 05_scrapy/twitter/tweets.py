import sys
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

#  API CREDENTIALS

ckey = "XTwJNYD8b9bekoIvJ4q5j1JUf"
csecret = "cmIe1H37tPXYgYqRKa5PyeQKhCkc62f3BDgaquRIEpCJlHBPTY"
atoken = "1012062505617805312-Y2wGE78wLUweV4zYVBLK0ogoeAOmdd"
asecret = "zC3CggazLLUcHJhTjl7la95m70ZeVPK4QqGytVYJNQnMu"


class listener(StreamListener):

    def on_data(self, data):
        with open('tweets.json','a') as diccionario:
            diccionario.write(data)
        return True

    def on_error(self, status):
        print (status)


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())



'''===============LOCATIONS=============='''
twitterStream.filter(locations=[-0.5816, 51.3304, 0.3138, 51.7336], track=['venezuela'])  # Quito