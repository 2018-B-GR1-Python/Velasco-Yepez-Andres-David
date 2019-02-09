from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

#  API CREDENTIALS

ckey = "XTwJNYD8b9bekoIvJ4q5j1JUf"
csecret = "cmIe1H37tPXYgYqRKa5PyeQKhCkc62f3BDgaquRIEpCJlHBPTY"
atoken = "1012062505617805312-Y2wGE78wLUweV4zYVBLK0ogoeAOmdd"
asecret = "zC3CggazLLUcHJhTjl7la95m70ZeVPK4QqGytVYJNQnMu"


class listener(StreamListener):

    def on_data(self, data):
        with open('tweets_mexico.json', 'a') as diccionario:
            diccionario.write(data+",")
        return True

    def on_error(self, status):
        print (status)


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())


filters = [
    'donaldtrump',
    'trump',
    'goverment',
    'whitehouse',
    'Trump'
]


# EEUU = -120.3,29.7,-87.8,46.3
# RUS = 37.28,52.72,91.07,66.19
# JAPON 131.46,30.57,146.57,44.94
# MEXICO -113.13,11.19,-88.91,31.74

twitterStream.filter(locations=[-113.13,11.19,-88.91,31.74], track=filters)