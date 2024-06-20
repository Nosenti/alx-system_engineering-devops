#!/usr/bin/python3
"""Script to recursively fetch titles of all
hot articles from a given subreddit."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API to find the titles of
    all hot articles for a given subreddit.

    Args:
        subreddit (str): The subreddit to query.
        hot_list (list): Accumulator for article titles.
        after (str): The 'after' marker to paginate the Reddit API.

    Returns:
        list: A list containing the titles of all hot articles or None
        if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Ubuntu 20.04; Python/3.4.3) MyRecursiveRedditClient/0.1'}
    params = {'limit': 100, 'after': after}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])
        if not posts and not hot_list:
            return None
        for post in posts:
            hot_list.append(post.get("data", {}).get("title"))

        after = data.get("data", {}).get("after")
        if after is not None:
            return recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None
