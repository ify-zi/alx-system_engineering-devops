#!/usr/bin/python3
"""
    Reddit api
"""


def number_of_subscribers(subreddit):
    """function returns tthe count of subscribers"""
    import requests

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}

    resp = requests.get(url,
                        headers=headers,
                        allow_redirects=False)
    if resp.status_code >= 300:
        return 0

    return resp.json().get("data").get("subscribers")
