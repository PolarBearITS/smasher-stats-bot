import praw
from docopt import docopt
from smasherstats import *

name = 'smasher-stats-bot'

if True:
	docstring = ''
	r = praw.Reddit(name, user_agent='Smasher stats web scraper by /u/PolarBearITS')
	for post in r.subreddit('smasherstats').hot(limit=10):
		for comment in post.comments.list():
			if f'/u/{name}' in comment.body and comment.author != name and all(c.author != name for c in comment.replies):
				comment.reply('Successful call to bot.')
				print('Replied to /u/' + str(comment.author))
				docstring = comment.body