#!/usr/bin/python3
""" 2-recurse """
import requests


def recurse(subreddit, hot_list=[], after='', count=0):
    """returns a list containing the titles
    of all hot articles for a given subreddit"""
    if subreddit is None or not isinstance(subreddit, str):
        return (None)
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    response = requests.get(url, params={'count': count, 'after': after},
                            headers={'User-Agent': 'MyAPI/0.0.1'},
                            allow_redirects=False)
    """posts = response.json().get('data', {}).get('children', [])
    titles = [post.get('data').get('title') for post in posts]
    hot_list += titles
    after = response.json().get('data', {}).get('after', None)
    if after:
        hot_list = recurse(subreddit, hot_list, after)
    return (hot_list)"""

    """if response.status_code >= 400:
        return None"""

    hot_l = hot_list + [child.get("data").get("title")
                        for child in response.json()
                        .get("data")
                        .get("children")]

    info = response.json()
    if not info.get("data").get("after"):
        return hot_l

    return recurse(subreddit, hot_l, info.get("data").get("count"),
                   info.get("data").get("after"))
