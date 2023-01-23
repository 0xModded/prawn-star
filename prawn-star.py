import praw
#input app's info and USERS login info, not app's
reddit = praw.Reddit(
                    client_id = '', #input clientID
                    client_secret = '', #input client SECRET
                    user_agent = '', #input user agent doesn't really matter unless
                    username = '', #input your REDDIT USERNAME, OR WHATEVER ACCOUNT IS RUNNING THE BOT, WITHOUT THE U/
                    password = '' #INPUT THE REDDIT PASSWORD OF THE ACCOUNT!
)

#declare target subreddit & obtain a instance of reddit
targetSub = '' #input your subreddits name, without the u/
subreddit = reddit.subreddit(targetSub) 

#functions for actions against the offending post and user
def action_submisson(submission):
    submission.mod.lock()
    submission.mod.remove()


#defines & searchs for target words. YOU MUST INPUT YOUR OWN WORDS OR LEAVE AS DEFAULT.
trigger_words = set(["kik", "snp", "Snap", "👻", "Naughty", "naughty", "sn@p", "CP", "cp", "tele", "telegram", "telegra", "upvote"])
trigger_phrase = set(["sn ap", "till you nut", "sending nudes", "upvote this", "till you cum"])

#searches for and destroys any offending post
for submission in subreddit.stream.submissions():
    title = submission.title.lower()
    if set(title.split()).intersection(trigger_words):
        #input what you want it to say here, or leave as is.
        submission.reply("You are suspected to be a bot! You have used bot like phrases in your title. Please message modmail so we can fix this and get you sorted :)").mod.distinguish(sticky = True, how = "yes")
        action_submisson(submission)
        continue
    for phrase in trigger_phrase:
        if phrase in title:
            submission.reply("You are suspected to be a bot! You have used bot like phrases in your title. Please message modmail so we can fix this and get you sorted :)").mod.distinguish(sticky = True, how = "yes")
            action_submisson(submission)

    

