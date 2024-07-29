#!/usr/bin/python3
"""Python script that, using this REST API, for
a given employee ID, returns information about
 his/her TO list progress."""
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(id)).json()
    # *get todo where userID = id
    todos = requests.get(url + "todos", {"userId": id}).json()

    name = user["name"]

    done = sum(1 for d in todos if d['completed'])  # Count True values

    print("Employee {} is done with tasks({}/{}):"
          .format(name, done, len(todos)))
    for d in todos:
        if d['completed']:
            print("\t {}".format(d['title']))
