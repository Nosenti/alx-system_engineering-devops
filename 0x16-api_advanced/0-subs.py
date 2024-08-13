#!/usr/bin/python3
"""Fetching the number of subscribers of a subreddit."""
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
        "User-Agent":
        "request"
    }

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data")
        num_subs = data.get("subscribers")
        return num_subs
    else:
        return 0
