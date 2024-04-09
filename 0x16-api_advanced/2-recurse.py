#!/usr/bin/python3
""" 2-recurse """
import requests


def recurse(subreddit, hot_list=[], after=''):
    """returns a list containing the titles
    of all hot articles for a given subreddit"""
    if subreddit is None or not isinstance(subreddit, str):
        return (None)
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    response = requests.get(url, params={'after': after},
                            headers={'User-Agent': 'MyAPI/0.0.1'})
    posts = response.json().get('data', {}).get('children', [])
    titles = [post.get('data').get('title') for post in posts]
    hot_list += titles
    after = response.json().get('data', {}).get('after', None)
    if after:
        hot_list = recurse(subreddit, hot_list, after)
    return (hot_list)
