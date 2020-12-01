import sys

import toml

from my_dataclasses import AuthInfo, Secrets


class ConfigFromToml(object):
    def __init__(self, secrets: Secrets) -> None:
        self.api_key = secrets.api_key
        self.api_secret = secrets.api_secret
        self.access_token = secrets.access_token
        self.access_token_secret = secrets.access_token_secret
        self.resource_url = secrets.resource_url

    def _view_tokens(self):
        print("=" * 50)
        print(f"api_key is {self.api_key}")
        print(f"api_secret is {self.api_secret}")
        print(f"access_token is {self.access_token}")
        print(f"access_token_secret is {self.access_token_secret}")


class ConfigForUseTwitterAPI(ConfigFromToml):
    def __init__(self, secrets: Secrets,) -> None:
        self.api_key = secrets.api_key
        self.api_secret = secrets.api_secret
        self.access_token = secrets.access_token
        self.access_token_secret = secrets.access_token_secret
        self.resource_url = secrets.resource_url

    def _api_auth_info(self):
        api_auth_info = AuthInfo(
            api_key=self.api_key,
            api_secret=self.api_secret,
            access_token=self.access_token,
            access_token_secret=self.access_token_secret,
            resource_url=self.resource_url,
        )
        return api_auth_info


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

    config_from_toml = ConfigFromToml(secrets)
    config_from_toml._view_tokens()

    config_for_use_twitter_api = ConfigForUseTwitterAPI(secrets)
    api_auth_info = config_for_use_twitter_api._api_auth_info()
    print(api_auth_info)
