#!/usr/bin/python3
""" 100-count """
import requests


def count_words(subreddit, word_list, after='', count={}):
    """parses the title of all hot articles,
    and prints a sorted count of given keywords"""
    if subreddit is None or not isinstance(subreddit, str):
        return (None)
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    response = requests.get(url, params={'after': after},
                            headers={'User-Agent': 'MyAPI/0.0.1'},
                            allow_redirects=False)
    posts = response.json().get('data', {}).get('children', [])
    titles = [post.get('data').get('title') for post in posts]
    for title in titles:
        words = title.split()
        for word in words:
            for w in word_list:
                if word.upper() == w.upper():
                    if count.get(w):
                        count[w] += 1
                    else:
                        count[w] = 1
    after = response.json().get('data', {}).get('after', None)
    if after:
        count = count_words(subreddit, word_list, after, count)
        return
    count = sorted(count, key=lambda x: x)
    for c in sorted(count, key=lambda x: count[x], reverse=True):
        print(f'{c}: {count.get(c)}')
