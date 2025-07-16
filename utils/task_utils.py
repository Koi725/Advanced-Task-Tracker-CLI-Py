import json
import os

DATA_FILE = "tasks.json"
current_user = None


def set_current_user(username):
    global current_user
    current_user = username


def get_current_user():
    return current_user


def task_init():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump({"tasks": []}, f)


def read_task():
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
        return data


def write_task(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


def append_task(new_tasks):
    task = read_task()
    task["tasks"].append(new_tasks)
    write_task(task)
