#!/usr/bin/python3
"""Python script that, using this REST API, for
a given employee ID, returns information about
 his/her TO list progress.
 and export into csv"""
import json
import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(id)).json()
    # *get todo where userID = id
    todos = requests.get(url + "todos", {"userId": id}).json()

    name = user.get("username")

    json_data = {id: [{"task": item['title'],
                       "completed": item['completed'],
                       "username": name} for item in todos]}

    file_name = "{}.json".format(id)
    with open(file_name, 'w') as f:
        json.dump(json_data, f, indent=4)
