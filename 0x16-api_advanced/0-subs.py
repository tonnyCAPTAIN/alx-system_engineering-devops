#!/usr/bin/python3
"""
Queries the Reddit API
"""
import requests


def number_of_subscribers(subreddit):
    '''Returns 0 if an invalid
    subreddit is given'''

    user = {"User-Agent": "RasberyyCalm762"}
    request = requests.get("https://www.reddit.com/r/{}/about.json"
                           .format(subreddit), headers=user)
    if request.status_code == 200:
        return request.json().get("data").get("subscribers")
    else:
        return 0
