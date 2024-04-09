#!/usr/bin/python3
""" 0-subs """
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""
    if subreddit is None or not isinstance(subreddit, str):
        return (0)
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers={'User-Agent': 'MyAPI/0.0.1'})
    return (response.json().get('data', {}).get('subscribers', 0))
