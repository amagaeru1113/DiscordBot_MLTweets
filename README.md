# DiscordBot_MLTweets

## 概要
- 毎朝9時に実行
- Twitterから指定したキーワード（現在は「機械学習」）に関するツイートを100件取得し、favoriteが5以上のtweetをDiscordに投稿するbot

## ファイル
- py
    - config.py: TwitterAPIのアクセストークンを設定
    - my_dataclasses: コード中で使用するデータクラスの定義
    - functions: Twitterリクエストの設定
    - main: tweet取得、discordへの投稿の実行
- toml
    - pyproject: poetryの設定
- txt
    - requirements: workflowで使用するライブラリ

## 必要な情報

- [TwitterAPI](https://developer.twitter.com/en/docs)のアクセストークン 合計4つ
- DiscordチャンネルのwebhookURL


## 参考サイト
- [【Pythonサンプルコード】tweepyでURLが含まれるツイートを抽出する：expanded_url](https://karupoimou.hatenablog.com/entry/2019/09/06/200742)
- [discordwebhook](https://github.com/10mohi6/discord-webhook-python)
- [超簡単discordwebhook](https://note.com/10mohi6/n/n3420f9e8aef0)
- [【Python】tweepyでTwitterのツイートを検索して取得](https://vatchlog.com/tweepy-search/)
- [RTを除外する方法](https://karupoimou.hatenablog.com/entry/2019/10/09/014020)


