# scrape_hashtag_tweets

**Purpose**

This Python script scrapes tweets containing a specific hashtag from Twitter without need for the Twitter API and saves them to a CSV file. It was created by kzaman1 and is available on GitHub.

**Requirements**

This script requires Python 3 and the following packages:
- snscrape
- pandas

**How to Use**

1. Clone or download the repository to your local machine.
2. Install the required packages listed above in the requiremetns section by running pip install.
3. Open the python file and edit: the hashtag, the number of tweets you want, and the directory path where you want the .csv to be located.
4. Run the script 
5. The script will scrape tweets containing the specified hashtag and save them to a CSV file with the filename containing the number of tweets you specified (note: it will not be the actual number of tweets), hashtag you used, and the current date.

**Tweet Parameters Scraped**

The script will scrape the following from each tweet that mentions the hashtag
1. date: the date of the tweet
2. tweet_url: the url to the tweet
3. tweet_content: the actual content of the tweet
4. tweet_rendered content: the actual content of the tweet but not sure how it's different from the tweet_content
5. tweet_id: the id of the tweet
6. user_name: the username of the person who tweeted the tweet (ex: zamandigital)
7. display_name: the display of the person who tweeted the tweet (ex: ** zaman digital 4 eva **)
8. user_id: the user id of the person who tweeted it
9. concatenated_profile_url: this takes the user_name and combines it with www.twitter.com (ex: www.twitter.com/zamandigital) so you can just click on the URL in the csv and it will open in your browser
10. user_description: the description of the user
11. verified: whether the user is a verified or not
12. user_profile_created: when the account was created
13. user_follower_count: how many followers the user has
14. user_friend_count: how many friends the user has
15. user_statuses_count: how many tweets the user has made
16. user_location: if the user lists a location in their profile, it will dislpay the location
17. user_description_url: I don't remember what this is for
18. user_profile_url: I don't remember what this is for
19. user_profile_image_url: a link to the user's profile image
20. user_profile_banner_url: a link to the user's banner image
21. tweet_reply_count: number of tweet's the user replied to
22. tweet_retweet_count: number of tweet's the user RT'd
23. tweet_like_count: number of tweets the user liked
24. tweet_quote_count: number of tweets the user quote tweeted
25. tweet_language: the language of the account (I think this is largely deprecated as it's always empty)
26. tweet_source: what type of device the user is using
27. rt_original_tweet_id: I believe this has been deprecated
28. quoted_tweet_original_tweet_id: if the user quote tweeted a tweet, a link to that tweet 
29. tweet_mentioned_users: the nested metadata of other users if they were mentioned in the user's tweets
30. tweet_hashtags: the neseted hashtag metadata if it was used in the user's tweets


**License**

This script is released under the MIT License.

**Disclaimer**

This script is provided as-is, without any warranty or support. Use at your own risk.
