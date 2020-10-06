import base64
import dataclasses
import sys

import toml
import tweepy
from discordwebhook import Discord

from config import ConfigForUseTwitterAPI
from functions import _setAuth, _setRequest, _setResponce


@dataclasses.dataclass(frozen=True)
class Tweet:
    user_name: str
    tweet_text: str
    created_at: str
    favorite: str
    retw: str
    url: str


@dataclasses.dataclass(frozen=True)
class Secrets:
    webhook_url: str
    api_key: str
    api_secret: str
    access_token: str
    access_token_secret: str
    resource_url: str


def tweets_with_keyword(keyword: str, maxTweets: int, secrets: Secrets):

    config_for_use_twitter_api = ConfigForUseTwitterAPI(secrets)
    api_auth_info = config_for_use_twitter_api._api_auth_info()
    print("1" + "*" * 100)
    print(api_auth_info)
    auth = tweepy.OAuthHandler(api_auth_info.api_key, api_auth_info.api_secret)
    print("2" + "*" * 100)
    auth.set_access_token(api_auth_info.access_token, api_auth_info.access_token_secret)
    print("3" + "*" * 100)
    api = tweepy.API(auth)
    print("4" + "*" * 100)

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
            # print("id   : ", tweet.user.id)
            # print("name : ", tweet.user.screen_name)
            # print("date : ", tweet.created_at)  # 呟いた日時
            # print("favo : ", tweet.favorite_count)  # ツイートのいいね数
            # print("retw : ", tweet.retweet_count)  # ツイートのリツイート数
            # print(tweet.full_text)  # ツイート内容
            # print(tweet.entities["urls"][0]["expanded_url"])
            # print("*" * 100)

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

    print(secrets)
    webhook_url = str(base64.b64decode(secrets.webhook_url))[2:-1]
    discord = Discord(url=webhook_url)
    data = tweets_with_keyword("機械学習", 10, secrets)

    for d in data[:2]:
        if d is not None:
            content = (
                f"=======================================================================================\n"
                + f"user_name: {d.user_name}\n"
                + f"created_at: {d.created_at}\n"
                + f"favo: {d.favorite}\n"
                + f"retw: {d.retw}\n"
                + f"text: {d.tweet_text}"
            )
            discord.post(content=content)

