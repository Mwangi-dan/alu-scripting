#!/usr/bin/python3
"""
Module to query number of subscribers in subreddit
(Reddit API)
"""
import json
import requests


def number_of_subscribers(subreddit):
    """
    Function quesries number of subscribers using Reddit API

    :subreddit - (str) name of subreddit

    :returns - (int) number of subscribers
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-agent': 'myAPI/0.0.1'}
    res = requests.get(url, headers=headers)
    subs = res.json()['data']['subscribers']

    try:
        return subs
    except:
        return 0
