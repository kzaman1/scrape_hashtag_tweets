'''
Install Packages
# pip install snscrape
# pip install pandas
'''

import csv
from datetime import date
import pandas as pd
import snscrape.modules.twitter as sntwitter
import time



hashtag_query = "islam"

# Set the limit fow how many tweets you want to correct and convert it into a string in a separate variable to use it in the filename
limit = 10
limit_as_string = str(limit)

# Create the filename
filename = "your_file_path\_" + limit_as_string + "_tweets_" + hashtag_query + "_" + str(date.today().strftime("%m-%d-%y")) + ".csv"
print("Filename Generated: ", filename)

# Create a list to store the tweets in
tweets = []

#Create a variable for the URL to concatenate the username with it to get the full URL since it's not scraping from the library
twitter_profile_url = "https://twitter.com/"

# Create a variable and iterate it to show the count
count = 0

# Set how many minutes the script should sleep for
sleep_time = 900


for tweet in sntwitter.TwitterSearchScraper(hashtag_query).get_items():
    if len(tweets) == limit:
        break
    else:
        #print(tweets)
        count += 1
        if count % 2000 == 0:
            print("Going to sleep for ", sleep_time/60, " minutes")
            time.sleep(sleep_time)
        tweets.append([
            tweet.date,
            tweet.url,
            tweet.content,
            tweet.renderedContent,
            tweet.id,
            tweet.user.username,
            tweet.user.displayname,
            tweet.user.id,
            twitter_profile_url + tweet.user.username,
            tweet.user.description,
            tweet.user.verified,
            tweet.user.created,
            tweet.user.followersCount,
            tweet.user.friendsCount,
            tweet.user.statusesCount,
            tweet.user.location,
            tweet.user.descriptionUrls,
            tweet.user.linkUrl,
            tweet.user.profileImageUrl,
            tweet.user.profileBannerUrl,
            tweet.replyCount,
            tweet.retweetCount,
            tweet.likeCount,
            tweet.quoteCount,
            tweet.lang,
            tweet.source,
            tweet.retweetedTweet,
            tweet.quotedTweet,
            tweet.mentionedUsers,
            tweet.hashtags
        ])
        print("Scraped Tweets:", count)

df = pd.DataFrame(tweets, columns=[
    'date',
    'tweet_url',
    'tweet_content',
    'tweet_rendered_content',
    'tweet_id',
    'user_name',
    'display_name',
    'user_id',
    'concatenated_profile_url',
    'user_description',
    'verified',
    'user_profile_created',
    'user_follower_count',
    'user_friend_count',
    'user_statuses_count',
    'user_location',
    'user_description_url',
    'user_profile_url',
    'user_profile_image_url',
    'user_profile_banner_url',
    'tweet_reply_count',
    'tweet_retweet_count',
    'tweet_like_count',
    'tweet_quote_count',
    'tweet_language',
    'tweet_source',
    'rt_original_tweet_id',
    'quoted_tweet_original_tweet_id',
    'tweet_mentioned_users',
    'tweet_hashtags'
])
print(df)

df.to_csv(filename)
