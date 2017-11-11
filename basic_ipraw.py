import praw

reddit = praw.Reddit(client_id = 'xxxxxxxxxxx', client_secret = 'xxxxxxxxx' , username = 'xxxxxxxxx' , password = 'xxxxxxxxxx', user_agent ='xxxxxxxxxx')

subreddit = reddit.subreddit('Apple')

hot_inception = subreddit.hot(limit = 5) #increase the limit to get more results

for submission in hot_inception :
	if not submission.stickied:
		print('Title: {}, ups: {}, downs: {}, Have we visited: {}'.format(submission.title, submission.ups, submission.downs, submission.visited))


subreddit.subscribe()

# to unsubscribe : subreddit.unsubscribe()
# to get thread ids : print(submission)
# to get attribute list : print(dir(submission))
