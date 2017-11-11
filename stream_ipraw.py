import praw

reddit = praw.Reddit(client_id = 'UsTn8e_ZkjNl6g', client_secret = 'A9Uxm0cq1WQwfaiofWLh6BT47tA' , username = 'prawtutorial7' , password = 'vinayak123456', user_agent ='prawtutorial7')

subreddit = reddit.subreddit('Apple')

for submission in subreddit.stream.submissions():
	try:
		print(submission.title)

	except Exception as e:
		print(str(e))
