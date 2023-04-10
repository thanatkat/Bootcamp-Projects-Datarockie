# -*- coding: utf-8 -*-
"""Fetch API with Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-VD01ZxmUgja-K7dsMhyU9fjwHkWFanb

# Plubic API Spotify Top 20 by monthly listners
"""

import requests
import pandas as pd
import time

url = "https://spotify81.p.rapidapi.com/top_20_by_monthly_listeners"

headers = {
	"X-RapidAPI-Key": "378d5a9db3mshd33308ffa8600d7p14dce5jsnca3969cbee27",
	"X-RapidAPI-Host": "spotify81.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)

# check status code
response.status_code # 200 Success!

# preview data
result = response.json()
result[5]

# get data
rank = []
artist = []
monthly_listener = []

for i in range(0,20):
    rank.append(result[i]['rank'])
    artist.append(result[i]['artist'])
    monthly_listener.append(result[i]['monthlyListeners'])
    time.sleep(2)

print("Success!")

# Create DataFrame
df = pd.DataFrame({"Rank":rank,"Artist":artist,"Monthly_listeners":monthly_listener}, index=None)

df