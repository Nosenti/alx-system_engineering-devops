#!/usr/bin/python3
"""print the titles of the top 10 posts for a given subreddit"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit.

    Args:
        subreddit (str): The subreddit to query.

    Prints:
        The titles of the first 10 hot posts if the subreddit is valid,
        otherwise, prints 'None'.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent':
               'Mozilla/5.0 (Ubuntu 20.04; Python/3.4.3) MyRedditClient/0.1'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])
        if posts:
            for post in posts:
                print(post.get("data", {}).get("title"))
        else:
            print(None)
    else:
        print(None)
