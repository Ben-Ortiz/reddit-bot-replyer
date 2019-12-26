import sys
import traceback

import praw

BOT_USERNAME = 'ENTER_HERE'
BOT_PASSWORD = 'ENTER_HERE'
BOT_CLIENT_ID = 'ENTER_HERE'
BOT_CLIENT_SECRET = 'ENTER_HERE'

TARGET_SUBREDDIT = 'ENTER_HERE' #example: TARGET_SUBREDDIT = 'funny'
TARGET_USER = 'ENTER_HERE' 
MESSAGE = "ENTER_HERE"


def harass():
    reddit = praw.Reddit(username=BOT_USERNAME,
                         password=BOT_PASSWORD,
                         client_id=BOT_CLIENT_ID,
                         client_secret=BOT_CLIENT_SECRET,
                         user_agent='reddit-bot-replyer')

    try:
        for comment in reddit.subreddit(TARGET_SUBREDDIT).stream.comments():
            if not comment.saved and comment.author == reddit.redditor(TARGET_USER):
                comment.save()
                comment.reply(MESSAGE)
    except BaseException as e:
        if type(e) == KeyboardInterrupt:
            sys.exit(0)
        else:
            traceback.print_exc()


if __name__ == '__main__':
    while True:
        harass()
