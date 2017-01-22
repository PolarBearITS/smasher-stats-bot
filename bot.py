import praw

r = praw.Reddit('smasher-stats-bot', user_agent='Bot for scraping smash stats off the net')
print(r)