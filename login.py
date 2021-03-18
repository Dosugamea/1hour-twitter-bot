import tweepy

# 環境変数読み出す
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

consumer_key = os.environ.get('CONSUMER_KEY')
consumer_secret = os.environ.get('CONSUMER_SECRET')

# 認証するやつ作る
auth = tweepy.OAuthHandler(
    consumer_key,
    consumer_secret
)
redirect_url = auth.get_authorization_url()

# ログインURL作ってもらってPINコード入れる
print("Open below address with your browser")
print(f"{redirect_url}")
verifier = input("PINコード: >> ")
auth.get_access_token(verifier)

# アクセストークンくれるのでこれで完成
print(f"ACCESS_TOKEN: {auth.access_token}")
print(f"ACCESS_TOKEN_SECRET: {auth.access_token_secret}")
