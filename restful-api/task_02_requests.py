#!/usr/bin/python3
"""
Module task_02_requests
Consuming and processing data from an API using Python
Fetches posts from the JSONPlaceholder API, prints their titles, and saves
selected post fields to a CSV file.
"""

import requests
import csv


def fetch_and_print_posts():
    """Fetch posts from the API and print the response status and titles.
    """
    reponse = requests.get("https://jsonplaceholder.typicode.com/posts")

    print(f"Status Code: {reponse.status_code}")

    if reponse.status_code == 200:
        posts = reponse.json()
        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """Fetch posts from the API and save the response status and titles.
    """
    reponse = requests.get("https://jsonplaceholder.typicode.com/posts")

    if reponse.status_code == 200:
        posts = reponse.json()

        data = [{"id": post["id"],
                "title": post["title"], "body": post["body"]}
                for post in posts
                ]

        name = "posts.csv"

        with open(name, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(data)
