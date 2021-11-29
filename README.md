# reddit_bot
Below are the several tasks that are required to be completed for my HW_04 submission!

### 1. Clearly state which politican your bot is supporting or opposing
My bot supports President Biden and prints comments that are related to his recent implementations.

### 2. Provide a link to your favorite thread involving your bot, an image screenshot of the thread, and a short description of what you like about it.

["Top general was so fearful Trump might spark war that he made secret calls to his Chinese counterpart, new book says"](https://old.reddit.com/r/BotTown2/comments/r489qu/top_general_was_so_fearful_trump_might_spark_war/) was my favorite thread. I liked it because of the way how the conversation that the bots are having is all over the place. It was funny that although the thread is suposed to be about Trump, there isn't a single comment that is about him, and the bots are leaving random comments about other politicians. 

![This is an image](https://github.com/jennifersjlim/reddit_bot/blob/main/favorite_thread.jpg)

### 3. Output of the bot_counter.py file
I've reached 1000 comments but the numbers have been decreasing the more I run the bot. 
```
PS C:\Users\user\Desktop\CSCI40\hw_04> & C:/Users/user/AppData/Local/Programs/Python/Python39/python.exe c:/Users/user/Desktop/CSCI40/hw_04/bot_counter.py --username Mountain_Turnover_98
len(comments)= 1000
len(top_level_comments)= 97
len(replies)= 903
len(valid_top_level_comments)= 85
len(not_self_replies)= 903
len(valid_replies)= 877
========================================
valid_comments= 962
========================================
```


### 4. Explain what your score should be
My total score should be 30/30. I've completed the following tasks. 
  - Each task in bot.py is worth 3 points. (6 tasks * 3 points/task = 18 points)
  - The github repo is worth 2 points.
  - (Optional #1) Getting at least 100 valid comments posted.
  - (Optional #2) Getting at least 500 valid comments posted.
  - (Optional #3) Getting at least 1000 valid comments posted.
  - (Optional #4) Make your bot create new submission posts instead of just new comments. You can easily automate this process by scanning the top posts in your favorite sub (e.g. /r/liberal or /r/conservative) and posting them to the class sub. I recommend creating a separate python file for creating submissions and creating comments.
For full credit, you must have at least 200 submissions, some of which should be self posts and some link posts. Duplicate submissions (i.e. submissions with the same title/selftext/url) do not count. 
      - attached as ```bot_post.py``` file
- (Optional #6) Instead of having your bot reply randomly to posts, make your bot reply to the most highly upvoted comment in a thread that it hasn't already replied to. Since reddit sorts comments by the number of upvotes, this will ensure that your bot's comments are more visible. You will still have to ensure that your bot never replies to itself if your bot happens to have the most upvoted comment.

