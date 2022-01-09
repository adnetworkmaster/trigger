import pymongo

import urllib

client = pymongo.MongoClient("mongodb://ajar:" + urllib.parse.quote_plus("Raja@1802") + "@cluster0-shard-00-00.1vax0.mongodb.net:27017,cluster0-shard-00-01.1vax0.mongodb.net:27017,cluster0-shard-00-02.1vax0.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-umkr09-shard-0&authSource=admin&retryWrites=true&w=majority")
mydb = client.anime
mycol = mydb["gogoapi_3"]
mydoc = mycol.find()
print(mydoc)
# df = json_normalize(mydoc)

from pandas import json_normalize
df = json_normalize(mydoc)

print(df.shape)

#df = df.iloc[22000:]
# df





import requests
import random
import time
s = requests.Session()
servers = ["https://p-001.herokuapp.com/crawl.json","https://p-002.herokuapp.com/crawl.json",
           "https://p-003.herokuapp.com/crawl.json","https://p-004.herokuapp.com/crawl.json",
           "https://p-005.herokuapp.com/crawl.json",]

def requ(df):
  chossen = random.choice(servers)
  df = df.replace(" ", "")
  url = f"https://www3.gogoanime.cm{df}"
  print(url)
  response = s.get( chossen + "?spider_name=ggspider_dat&url=" + url)
  # print("request completed")

import pandas as pd
pd.set_option('display.max_colwidth',1000)

import multiprocessing
import numpy as np
pool = multiprocessing.Pool(15)
df_2 = list(df["ep_url"])
outputs = pool.map(requ, df_2)
pool.close()
pool.join()







