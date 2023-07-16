#!/usr/bin/python3
"""
Module with function to count words
"""
import requests


def count_words(subreddit, word_list=[], after=None, clean_dict=None):
    """
    Function that queries subreddit for all titles and counts
    the number of times the words in the list appear in the
    titles.
    """

    if subreddit is None or not isinstance(subreddit, str):
        return None

    lowercase_list = [x.lower() for x in word_list]
    clean_word_list = list(dict.fromkeys(lowercase_list))

    if clean_dict is None:
        clean_dict = dict.fromkeys(clean_word_list)

    headers = {'User-Agent': 'myAPI/0.0.1'}
    query_strings = '?show="all"&limit=100&after={}'.format(after)
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit) + query_strings

    response = requests.get(url, headers=headers)

    if response:
        all = response.json()
        after = all.get('data').get('after')
        raw = all.get('data').get('children')

        if after is None:
            new_dict = {k: v for k, v in clean_dict.items() if v is not None}

            for k in sorted(new_dict.items(), key=lambda x: (-x[1], x[0])):
                print('{}: {}'.format(k[0], k[1]))

            return None
 
        for i in raw:
            title = i.get('data').get('title')
            title_split = title.split()
            title_split_lc = [x.lower() for x in title_split]

            for j in title_split_lc:
                if j in clean_dict and clean_dict[j] is None:
                    clean_dict[j] = 1
                elif j in clean_dict and clean_dict[j] is not None:
                    clean_dict[j] += 1

        count_words(subreddit, word_list, after, clean_dict)

    else:
        return None
