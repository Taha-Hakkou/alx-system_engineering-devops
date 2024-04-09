#!/usr/bin/python3
""" 100-count """
import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """parses the title of all hot articles,
    and prints a sorted count of given keywords"""
    """if subreddit is None or not isinstance(subreddit, str):
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
        print(f'{c}: {count.get(c)}')"""
    sub_info = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit),
                            params={"after": after},
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if sub_info.status_code != 200:
        return None

    info = sub_info.json()

    hot_l = [child.get("data").get("title")
             for child in info
             .get("data")
             .get("children")]
    if not hot_l:
        return None

    word_list = list(dict.fromkeys(word_list))

    if word_count == {}:
        word_count = {word: 0 for word in word_list}

    for title in hot_l:
        split_words = title.split(' ')
        for word in word_list:
            for s_word in split_words:
                if s_word.lower() == word.lower():
                    word_count[word] += 1

    if not info.get("data").get("after"):
        sorted_counts = sorted(word_count.items(), key=lambda kv: kv[0])
        sorted_counts = sorted(word_count.items(),
                               key=lambda kv: kv[1], reverse=True)
        [print('{}: {}'.format(k, v)) for k, v in sorted_counts if v != 0]
    else:
        return count_words(subreddit, word_list, word_count,
                           info.get("data").get("after"))
