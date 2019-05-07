import praw

reddit = praw.Reddit(client_id = 'xxxxxxx', client_secret = 'xxxxxxx' , username = 'xxxxxxx' , password = 'xxxxxxx', user_agent ='xxxxxxx')

subreddit = reddit.subreddit('Apple')

hot_inception = subreddit.hot(limit = 3)

for submission in hot_inception :
	if not submission.stickied:
		print('Title: {}, ups: {}, downs: {}, Have we visited: {}'.format(submission.title, submission.ups, submission.downs, submission.visited))

		#PARSING COMMENTS
		comments = submission.comments
		for comment in comments:
			print(20*'-')
			print(comment.body)
			if len(comment.replies) > 0:
				for reply in comment.replies:
					print('REPLY:',reply.body)
