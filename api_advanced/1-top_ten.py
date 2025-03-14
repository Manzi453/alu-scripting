#!/usr/bin/python3
"""
1-top_ten.py
"""
import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit to query.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "python:subreddit.hot.posts:v1.0 (by /u/yourusername)"}  # Set a custom User-Agent
    params = {"limit": 10}  # Limit the number of posts to 10

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:  # Check if the request was successful
            data = response.json()
            posts = data["data"]["children"]
            for post in posts:
                print(post["data"]["title"])
        else:
            print(None)  # Print None for invalid subreddits or other errors
    except Exception as e:
        print(None)  # Handle any exceptions (e.g., network issues)

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
