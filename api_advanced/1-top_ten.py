#!/usr/bin/python3
"""
Module that queries reddit api to get 10 hot posts in a subreddit
"""
import requests


def top_ten(subreddit):
    """
    Function that gets ten hot posts in a subreddit

    :subreddit - (str) Name of subreddit

    :hot_list - (list) list of ten hot posts of subreddit
    """
    if subreddit is None or isinstance(subreddit, str) is False:
        print(None)

    headers = {"User-agent": "myAPI/0.0.1"}
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    res = requests.get(url, headers=headers)
    # Gets list of title of post in children
    data = res.json().get('data')
    try:
        all_posts = data.get('children')
        for post in all_posts:
            print(post.get('data').get('title'))
    except:
        print(None)
