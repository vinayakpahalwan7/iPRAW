import praw

reddit = praw.Reddit(client_id = 'xxxxxxx', client_secret = 'xxxxxxx' , username = 'xxxxxxx' , password = 'xxxxxxx', user_agent ='xxxxxxx')

subreddit = reddit.subreddit('Apple')

hot_inception = subreddit.hot(limit = 3)

for submission in hot_inception :
	if not submission.stickied:
		print('Title: {}, ups: {}, downs: {}, Have we visited: {}'.format(submission.title, submission.ups, submission.downs, submission.visited))

		#PARSING COMMENTS TREE
		submission.comments.replace_more(limit=0)
		for comment in submission.comments.list():
			print(20*'-')
			print('Parent Id:', comment.parent())
			print('Comment Id:', comment.id)
			print(comment.body)
