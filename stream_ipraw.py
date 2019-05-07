import praw

reddit = praw.Reddit(client_id = 'xxxxxxx', client_secret = 'xxxxxxx' , username = 'xxxxxxx' , password = 'xxxxxxx', user_agent ='xxxxxxx')

subreddit = reddit.subreddit('Apple')

for submission in subreddit.stream.submissions():
	try:
		print(submission.title)

	except Exception as e:
		print(str(e))
