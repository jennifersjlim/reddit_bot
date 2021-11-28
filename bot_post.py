import praw
import random
import datetime
import time

reddit = praw.Reddit('bot', user_agent='cs40bot')
reddit.validate_on_submit = True

all_submissions = []
for submission in reddit.subreddit("Liberal").hot(limit=200):
    all_submissions.append(submission)

cnt = 0

for submission in all_submissions:
    cnt+=1
    print()
    print(cnt, ': new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)
    print(submission.selftext)
    rand = random.randrange(1,3)
    if rand == 1:
        reddit.subreddit("BotTown2").submit(title=submission.title, url=submission.url)
    else:
        reddit.subreddit("BotTown2").submit(title=submission.title, selftext=submission.selftext)
    time.sleep(10)