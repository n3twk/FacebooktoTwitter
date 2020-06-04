import facebook_scraper
import tweepy
from datetime import date
page1 = "#PageName"
consumer_key = "get_from_twitter"
consumer_secret = "get_from_twitter"
access_token = "get_from_twitter"
access_token_secret = "get_from_twitter"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
today = date.today()
api = tweepy.API(auth)
checked = []


def fb_fetch():

    looping = facebook_scraper.get_posts(page1, pages=5)
    for post in looping:
        if "#Text_from_post" in post['text']:
            # print(checked)
            if post['time'] not in checked:
                checked.append(post['time'])
                post = post['text']
                print(post)
#            charlen = len(post)
                for chunk in chunkstring(post, 220):
                    print(chunk + "  End of chunk")
                    chunk = chunk + "  "+today.strftime("%d/%m/%Y")
                    tweet_it(chunk, api)

def tweet_it(post, api):
    try:
        api.update_status(post)
    except Exception as e:
        print(e)
        pass


def chunkstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))


if __name__ == '__main__':

    fb_fetch()

