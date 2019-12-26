import praw

reddit = praw.Reddit(client_id = 'ENTER_HERE',
                     client_secret = 'ENTER_HERE',
                     username='ENTER_USERNAME_HERE',
                     password='ENTER_PASSWORD_HERE',
                     user_agent='ENTER_HERE')

subreddit = reddit.subreddit('all')

hot_popular = subreddit.hot(limit=7)

for submission in hot_popular:
    if not submission.stickied:
        print('Title: {}, ups: {}, downs: {}'.format(submission.title,
                                                     submission.ups,
                                                     submission.downs))
