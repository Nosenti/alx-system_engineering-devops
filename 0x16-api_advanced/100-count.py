#!/usr/bin/python3
"""Script to count words in the titles of all hot
articles from a given subreddit."""
import requests
import re


def count_words(subreddit, word_list, hot_list=[], after=None, word_count={}):
    """
    Recursively counts and prints the number of times each keyword appears
    in the titles of all hot articles from a subreddit,
    sorted by the count in descending order.

    Args:
        subreddit (str): The subreddit to query.
        word_list (list): List of words to count.
        hot_list (list): Accumulator for titles, used during recursion.
        after (str): ID of the last article in the current page,
        used for pagination.
        word_count (dict): Accumulator for word counts.
    """
    if not word_list or word_list == [] or not subreddit:
        return
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Ubuntu 20.04; Python/3.4.3) MyRedditKeywordCounter/0.1"
    }
    params = {"limit": 100, "after": after}

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code != 200:
        return None if not hot_list else print_sorted(word_count)

    data = response.json()
    posts = data.get("data", {}).get("children", [])
    for post in posts:
        hot_list.append(post.get("data", {}).get("title"))

    after = data.get("data", {}).get("after")
    if after is not None:
        count_words(subreddit, word_list, hot_list, after, word_count)
    else:
        for title in hot_list:
            normalize_and_count_words(title, word_list, word_count)
        print_sorted(word_count)


def normalize_and_count_words(title, word_list, word_count):
    """Normalize the title to count occurrences of each keyword."""
    title = title.lower()
    for word in word_list:
        if word.lower() in title:
            """
            Regex to find whole word matches only, excluding substrings
            within longer words
            """
            matches = re.findall(r"\b" + re.escape(word.lower()) +
                                 r"\b", title)
            if word.lower() in word_count:
                word_count[word.lower()] += len(matches)
            else:
                word_count[word.lower()] = len(matches)


def print_sorted(word_count):
    """Sorts and prints the results in the specified format."""
    sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_words:
        if count > 0:
            print(f"{word}: {count}")
