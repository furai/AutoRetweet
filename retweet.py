from twython import Twython
from twython import TwythonStreamer

import settings

class RetweetingStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'retweeted_status' in data:
            my_retweets = [item for item in twitter.get_retweets(id=data['retweeted_status']['id']) if item["user"]['id'] == my_user_id]
        else:
            my_retweets = []
        if len(my_retweets) == 0 and data['user']['screen_name'] in settings.ACCOUNTS:
            if settings.NEEDSTAG.get(data['user']['screen_name'], False) == False or (settings.NEEDSTAG.get(data['user']['screen_name'], False) and data['text'].lower().find(settings.TAG) != -1) :
                twitter.retweet(id=data['id'])
                print "Retweeting %s: %s" % (data['user']['name'].encode('utf-8'), data.get('text', "Tweet ID: " + str(data['id'])).encode('utf-8'))

    def on_error(self, status_code, data):
        print status_code, data

if not hasattr(settings, 'OAUTH_TOKEN'):
    twitter = Twython(settings.APP_KEY, settings.APP_SECRET)
    auth = twitter.get_authentication_tokens()

    print "Open %s to authorize application and get PIN  number." % auth['auth_url']
    twitter = Twython(settings.APP_KEY, settings.APP_SECRET, auth['oauth_token'], auth['oauth_token_secret'])

    pin = raw_input("Enter PIN: ")
    final_step = twitter.get_authorized_tokens(pin)

    print "Now save tokens to your settings.py and run this script again.\n"
    print "OAUTH_TOKEN = \"%s\"" % final_step['oauth_token']
    print "OAUTH_TOKEN_SECRET = \"%s\"\n" % final_step['oauth_token_secret']

else:
    twitter = Twython(settings.APP_KEY, settings.APP_SECRET, settings.OAUTH_TOKEN, settings.OAUTH_TOKEN_SECRET)
    user_ids = [str(user['id']) for user in twitter.lookup_user(screen_name=','.join(settings.ACCOUNTS))]
    my_user_id = twitter.verify_credentials()['id']

    stream = RetweetingStreamer(settings.APP_KEY, settings.APP_SECRET, settings.OAUTH_TOKEN, settings.OAUTH_TOKEN_SECRET)
    stream.statuses.filter(follow=user_ids)