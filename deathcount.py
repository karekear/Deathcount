import json #標準のjsonモジュールとconfig.pyの読み込み
from requests_oauthlib import OAuth1Session #OAuthのライブラリの読み込み
#import pprint
import os
import datetime
import math
import time

CK = "CONSUMER_KEY"
CS = "CONSUMER_SECRET"
AT = "ACCESS_TOKEN"
ATS = "ACCESS_TOKEN_SECRET"

twitter = OAuth1Session(os.environ["CONSUMER_KEY"],os.environ["CONSUMER_SECRET"], os.environ["ACCESS_TOKEN"], os.environ["ACCESS_TOKEN_SECRET"]) #認証処理
url_post = "https://api.twitter.com/1.1/statuses/update.json"       #ツイート用urlst

def job():
	now = datetime.datetime.today()
	ttm = datetime.datetime(2019,9,6,0,0,0)
	days = (ttm - now).days * 24
	minutes = ((ttm - now).seconds//60 + 1) % 60
	seconds = (ttm - now).seconds//3600
	hours = days + seconds + 1
	print(seconds)
	print(minutes)
	print(hours)

	#tweet = "@tos\nuec_deathまであと{}時間{}分".format(hours,minutes)
	tweet = "@tos\n{}".format(str(now))
	print(tweet)

	params = {"status" : tweet} #辞書型だよなこれ
	res = twitter.post(url_post, params = params) #post送信

	if res.status_code == 200:   #正常投稿出来た場合
		print("Success.")
	else:                       #正常投稿出来なかった場合
		print("Failed. : %d" % res.status_code)
		if res.status_code == 403:
			print("Already Tweeted")

job()

"""
schedule.every().minute.at(':00').do(job)

while True:
	schedule.run_pending()
	time.sleep(1)
"""