import praw
from docopt import docopt
from smasherstats import *

name = 'smasher-stats-bot'

def nums_from_string(string):
    nums = ''
    for char in string:
        if char.isnumeric():
            nums += char
    return int(nums)

if True:
	docstring = ''
	r = praw.Reddit(name, user_agent='Smasher stats web scraper by /u/PolarBearITS')
	for post in r.subreddit('smasherstats').hot(limit=10):
		for comment in post.comments.list():
			if f'/u/{name}' in comment.body and comment.author != name and all(c.author != name for c in comment.replies):
				docstring = comment.body.strip(name)
				tags = ['Mang0', 'Armada']
				results = []
				for tag in tags:
					r = smasherstats.getResults(tag, ['2016'], 'Super Smash Bros. Melee', 'Singles')
					results.append([r[2], r[0]])
				for i in range(len(tags)):
					res = sorted(results[i][1], key=lambda x: nums_from_string(x[0]))
				record = smasherstats.getRecord(tags, results, 'melee')

				headers = f'Tournament|Round|{tags[0]} vs. {tags[1]}|Winner\n'
				rtable = headers
				rtable += '|'.join(':-:' for _ in range(len(headers.split('|')))) + '\n'

				tourneys = record[0]
				for i in range(len(tourneys)):
					tourney = tourneys[i]
					r_name = tourney[0]
					if i > 0:
						if r_name == tourneys[i-1][0]:
							r_name = ' '
						else:
							rtable += '|'.join('&nbsp;' for _ in range(len(headers.split('|')))) + '\n'
					rtable += r_name + '|' + '|'.join(tourney[1:]) + '  \n'
				rtable += '\n&nbsp;  \n'
				rtable += f'Total Set Count: {tags[0]} {record[1][0]} - {record[1][1]} {tags[1]}'
				rtable += f'  \nTotal Game Count {tags[0]} {record[2][0]} - {record[2][1]} {tags[1]}'
				print(rtable)
				comment.reply(rtable)
				print('Replied to /u/' + str(comment.author))
