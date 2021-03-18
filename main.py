import tweepy
import schedule
import requests
import random
import os
from time import sleep
from datetime import datetime
from dotenv import load_dotenv


class TwitterScheduledMethods():
    def __init__(self, cl):
        self.cl = cl
        schedule.every(1).minutes.do(self.ten_minutes_gacha)
        schedule.every(1).hours.do(self.one_hour_gacha)

    def generateMessage(self, body):
        build_message = [
            "[定期]",
            body,
            datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        ]
        return "\n".join(build_message)

    def ten_minutes_gacha(self):
        print("Executing 10 minutes Gacha...")
        choices = [
            "香風智乃すき",
            "九条カレンすき",
            "能美クドリャフカすき"
        ]
        msg = random.choice(choices)
        self.cl.update_status(status=self.generateMessage(msg))

    def one_hour_gacha(self):
        print("Executing 1 Hour Gacha...")
        choices = [
            ("1.png", "https://www.pixiv.net/artworks/54265978"),
            ("2.png", "https://www.pixiv.net/artworks/64978502?page=18"),
            ("3.png", "https://twitter.com/nekomimimix/status/1330295814879653888?page=1")
        ]
        filename, page_address = random.choice(choices)
        self.cl.update_with_media(
            status=self.generateMessage(
                f"推しイラストです!!\n{page_address}"
            ),
            filename=filename
        )


class TwitterBot(TwitterScheduledMethods):
    def __init__(
        self,
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret
    ):
        # クライアント作る
        auth = tweepy.OAuthHandler(
            consumer_key,
            consumer_secret
        )
        auth.set_access_token(
            access_token,
            access_token_secret
        )
        self.cl = tweepy.API(auth, wait_on_rate_limit=True)
        TwitterScheduledMethods.__init__(self, self.cl)


if __name__ == "__main__":
    load_dotenv(verbose=True)
    consumer_key = os.environ.get('CONSUMER_KEY')
    consumer_secret = os.environ.get('CONSUMER_SECRET')
    access_token = os.environ.get('ACCESS_TOKEN')
    access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')
    cl = TwitterBot(
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret
    )
    print("Login success")
    while True:
        schedule.run_pending()
        sleep(1)
