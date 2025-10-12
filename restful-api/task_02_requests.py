#!/usr/bin/python3
"""Module for fetching posts from JSONPlaceholder"""
import requests

# Defining the URL
url = 'https://jsonplaceholder.typicode.com/posts'


def fetch_and_print_posts():
    """Function to send request to JSONPlaceholder"""

    # Sending the request
    response = requests.get(url)

    # Printing the response status code
    print(f"Status Code: {response.status_code}")

    # Fetching the data if request is successful
    if response.status_code == 200:
        data = response.json()

        # Printing the titles of the response
        for resp in data:
            title = resp["title"]
            print(title)

    # If request is not successful
    else:
        print("Request was not successful.")


def fetch_and_save_posts():
    """Function to save the response data to a dictionary"""
    import csv

    # Sending the request
    response = requests.get(url)

    # Printing the response status code
    print(f"Status Code: {response.status_code}")

    # Fetching the data if request is successful
    if response.status_code == 200:
        data = response.json()
        csvf = 'posts.csv'
        datalist = []

        # Creating new list element for each post
        for element in data:
            post = {
                'id': element.get('id'),
                'title': element.get('title'),
                'body': element.get('body')
            }
            datalist.append(post)

        # Writing to the csv file
        with open(csvf, 'w', encoding='UTF-8') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(datalist)

    # If request is not successful
    else:
        print("Request was not successful.")
