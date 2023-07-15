#!/usr/bin/python3
"""
Module with function that queries all hot posts in a sub
using recursion with Reddit's API
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    if subreddit is None or not isinstance(subreddit, str):
        return None

    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(subreddit,
                                                                 after)
    headers = {'User-agent': 'myAPI/0.0.1'}
    params = {'limit': 100, 'after': after}

    res = requests.get(url, headers=headers, params=params)
    if res.status_code != 200:
        return None

    # All the data
    all = res.json()

    try:
        children_list = all.get('data').get('children')
        after = all.get('data').get('after')

        if after is None:
            return hot_list

        # get titles from children list
        for child in children_list:
            hot_list.append(child.get('data').get('title'))

        # Recursion for after pages
        return recurse(subreddit, hot_list, after)
    except:
        return None
