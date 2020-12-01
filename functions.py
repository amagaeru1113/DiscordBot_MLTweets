import json

from requests_oauthlib import OAuth1Session  # type: ignore

from my_dataclasses import TweetInfo


def _setAuth(api_auth_info):
    AK = api_auth_info.api_key
    AS = api_auth_info.api_secret
    AT = api_auth_info.access_token
    ATS = api_auth_info.access_token_secret
    return OAuth1Session(AK, AS, AT, ATS)


def _setRequest(twitter_auth, resource_url, params):
    return twitter_auth.get(resource_url, params=params)


def _setResponce(request):
    responced_tweets = {}

    if request.status_code != 200:
        return responced_tweets
    else:
        res = json.loads(request.text)

        for idx, line in enumerate(res):
            key = "tweet" + str(idx).zfill(3)
            tweet_info = TweetInfo(
                user_name=line["user"]["name"],
                tweet_text=line["text"],
                created_at=line["created_at"],
            )
            responced_tweets[key] = tweet_info
        return responced_tweets        
