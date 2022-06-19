from os import read, write
import tweepy
from time import sleep
import random

api_key= 'Zt2MYJO5y4eDm2Bc6jwCdRWStA'
api_secret_key = 'ZbexQ2wLCyA3P5MltaHDxMKfC0I8PaUzqzllv1yFDEYzwl1h4n'
acess_key = '319247946-7IcGCAmPK7U6RhDl0bmnL7wUQDSlmhVf9Zb6iWdf'
acess_secret = 'ZYmOsPxsXz81kWLe7GU3IIQhJXO9qFyBnchW0NgUCtCR4'

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(acess_key, acess_secret)

api = tweepy.API(auth, wait_on_rate_linit=True, wait_on_rate_limit_notify=True)

FILE_NAME = 'last_seen.txt'

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id
                

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return


def random_phrase():
    p1 = ['Rafous', 'Lumibly', 'Fulas', 'Joãozinho', 'Sysak', 'Luis', 'Kaiki' 'SuperNando'] 
    p2 = ['ta muito', 'ta', 'é', 'era']
    p3 = ['focado','0 foco','dangerous']
    p4 = ['na academy', 'no ejif', 'no discord']

    genius_phrase = random.choice(p1) + random.choice(p2) + random.choice(p3)
    return genius_phrase

def _main_():
    read_last_seen_str = str(read_last_seen(FILE_NAME))
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode = 'extended')
    print('Ultimo ID pesquisado:' + read_last_seen_str)
    for tweet in reversed(tweets):
        store_last_seen(FILE_NAME, tweet.id)
        genius_phrase = random_phrase()
        api.update_status("@" + tweet.user.screen_name + ' ' + genius_phrase, in_reply_to_status_id=tweet.id)
        #api.update_status("@" + tweet.user.screen_name + ' ' + genius_phrase, in_reply_to_status_id=tweet.id)

while True:
    _main_()
    sleep(60)