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
    url = f"https://www.reddit.com/{subreddit}/about.json"
    headers = {'User-agent': 'myAPI/0.0.1'}
    res = requests.get(url, headers=headers})
    subs  = res.json()['data']['subscribers']
    if subs is None:
	return 0
    else:
	return subs
