import praw

reddit = praw.Reddit(client_id = 'gMovbAmq865JXQ',
                     client_secret = 'n7yj2D5dtzj6WHq1ca7trbKXJOY',
                     username='yesimoneofthem',
                     password='bestiary468',
                     user_agent='firstredditbot')

subreddit = reddit.subreddit('all')

hot_popular = subreddit.hot(limit=7)

for submission in hot_popular:
    if not submission.stickied:
        print('Title: {}, ups: {}, downs: {}'.format(submission.title,
                                                     submission.ups,
                                                     submission.downs))