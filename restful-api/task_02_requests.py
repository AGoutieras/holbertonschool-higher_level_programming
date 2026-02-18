#!/usr/bin/python3

import requests
import csv


def fetch_and_print_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')

    print(f"Status Code: {r.status_code}")

    if r.status_code == 200:
        data = r.json()

        for post in data:
            print(post["title"])

def fetch_and_save_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')

    if r.status_code == 200:
        data = r.json()

        filtered_posts = []

        for post in data:
            post_data = {}
            post_data["id"] = post["id"]
            post_data["title"] = post["title"]
            post_data["body"] = post["body"]
            filtered_posts.append(post_data)

        with open('posts.csv', 'w', newline='') as f:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(filtered_posts)
