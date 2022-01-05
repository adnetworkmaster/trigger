import requests
import random
import time
s = requests.Session()
servers = ["https://po-100.herokuapp.com/crawl.json","https://po-101.herokuapp.com/crawl.json",
           "https://po-102.herokuapp.com/crawl.json","https://po-103.herokuapp.com/crawl.json",
           "https://po-104.herokuapp.com/crawl.json",]

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







