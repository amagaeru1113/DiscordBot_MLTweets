import base64
import sys

import tweepy
from discordwebhook import Discord

from config import ConfigForUseTwitterAPI
from functions import _setAuth, _setRequest, _setResponce
from my_dataclasses import Tweet, Secrets


def tweets_with_keyword(keyword: str, maxTweets: int, secrets: Secrets):
    config_for_use_twitter_api = ConfigForUseTwitterAPI(secrets)
    api_auth_info = config_for_use_twitter_api._api_auth_info()
    auth = tweepy.OAuthHandler(api_auth_info.api_key, api_auth_info.api_secret)
    auth.set_access_token(api_auth_info.access_token, api_auth_info.access_token_secret)
    api = tweepy.API(auth)

    tweets_data = []
    for tweet in tweepy.Cursor(
        api.search,
        q=keyword + "-filter:retweets",
        include_entities=True,
        tweet_mode="extended",
        lang="ja",
        result_type="recent",
    ).items(maxTweets):

        if tweet.entities["urls"] != []:
            add_tweet = Tweet(
                user_name=tweet.user.screen_name,
                tweet_text=tweet.full_text,
                created_at=tweet.created_at,
                favorite=tweet.favorite_count,
                retw=tweet.retweet_count,
                url=tweet.entities["urls"][0]["expanded_url"],
            )
            tweets_data.append(add_tweet)

    return tweets_data


if __name__ == "__main__":
    args = sys.argv

    secrets = Secrets(
        webhook_url="{}".format(args[1]),
        api_key="{}".format(args[2]),
        api_secret="{}".format(args[3]),
        access_token="{}".format(args[4]),
        access_token_secret="{}".format(args[5]),
        resource_url="https://api.twitter.com/1.1/statuses/user_timeline.json",
    )

    webhook_url = str(base64.b64decode(secrets.webhook_url))[2:-1]
    discord = Discord(url=webhook_url)
    keyword = "機械学習"

    data = tweets_with_keyword(keyword, 100, secrets)
    sorted_data = sorted(data, reverse=True, key=lambda x: x.favorite)
    push_data = [ps for ps in sorted_data if ps.favorite >= 5]

    for d in push_data:
        if d is not None:
            content = (
                f"=======================================================================================\n"
                + f"user_name: {d.user_name}\n"
                + f"created_at: {d.created_at}\n"
                + f"favo: {d.favorite}\n"  # ツイートのいいね数
                + f"retw: {d.retw}\n"  # ツイートのリツイート数
                + f"text: {d.tweet_text}"  # ツイート内容
            )
            discord.post(content=content)

