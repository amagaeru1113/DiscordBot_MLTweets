import dataclasses


@dataclasses.dataclass(frozen=True)
class TweetInfo:
    user_name: str
    tweet_text: str
    created_at: str


@dataclasses.dataclass(frozen=True)
class AuthInfo:
    api_key: str
    api_secret: str
    access_token: str
    access_token_secret: str
    resource_url: str


@dataclasses.dataclass(frozen=True)
class QueryInfo:
    tweet_count: str
    account_name: str


@dataclasses.dataclass(frozen=True)
class Secrets:
    webhook_url: str
    api_key: str
    api_secret: str
    access_token: str
    access_token_secret: str
    resource_url: str


@dataclasses.dataclass(frozen=True)
class Tweet:
    user_name: str
    tweet_text: str
    created_at: str
    favorite: str
    retw: str
    url: str
