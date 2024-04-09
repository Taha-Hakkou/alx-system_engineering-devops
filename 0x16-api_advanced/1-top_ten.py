#!/usr/bin/python3
""" 1-top_ten """
import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts
    listed for a given subreddit"""
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    response = requests.get(url, params={'limit': '10'},
                            headers={'User-Agent': 'MyAPI/0.0.1'},
                            allow_redirects=False)
    posts = response.json().get('data', {}).get('children', [])
    if posts == []:
        print(None)
    for post in posts:
        print(post.get('data').get('title'))
