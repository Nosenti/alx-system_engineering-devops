#!/usr/bin/python3
"""fetching the number of subscribers of a subreddit"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API to find the number of
    subscribers to a given subreddit.
    Args:
        subreddit (str): The subreddit to query.
    Returns:
        int: The number of subscribers or 0 if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Ubuntu 20.04; Python/3.4.3) MySubredditCounter/0.1'
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data.get("data", {}).get("subscribers", 0)
    else:
        return 0
