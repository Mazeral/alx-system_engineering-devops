#!/usr/bin/python3
"""
1-top_ten function module
"""
import requests


def top_ten(subreddit):
    """Queries a subreddit to get it's top 10 hot posts"""

    try:
        response = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                                .format(subreddit),
                                headers={"User-Agent": "My-User-Agent"},
                                allow_redirects=False)

        if response.status_code == 200:
            listings = response.json()["data"]["children"]
            for listing in listings:
                print(listing["data"]["title"])
    except Exception as e:
        print("None")
