import requests
import random
import time
s = requests.Session()
servers = ["https://io-00001.herokuapp.com/crawl.json","https://io-0001.herokuapp.com/crawl.json",
           "https://io-001.herokuapp.com/crawl.json","https://io-10000.herokuapp.com/crawl.json",
           "https://io-oioio.herokuapp.com/crawl.json",]

def requ(df):
  chossen = random.choice(servers)
  url = f"https://amuseanime.netlify.app/episode/{df}"
  print(url)
  response = s.get( chossen + "?spider_name=anime_earner&url=" + url)
  # print("request completed")
for i in range(1,100000000000000000000000000000000):
  try:
    import multiprocessing
    # import numpy as np
    pool = multiprocessing.Pool(15)
    df_2 = list(range(126871,253992))
    # pool = multiprocessing.Pool(processes=5)
    # df_split = np.array_split(df, 5)
    outputs = pool.map(requ, df_2)
    pool.close()
    pool.join()
  except:
    print("Failed bro")







