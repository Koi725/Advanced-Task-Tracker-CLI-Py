from utils.task_utils import *
from utils.auth_utils import *
from datetime import datetime


def add_task(title, description):
    data = read_task()
    tasks = data["tasks"]
    new_id = max([t["id"] for t in tasks], default=0) + 1
    task = {
        "id": new_id,
        "title": title,
        "description": description,
        "status": "Pending",
        "created_by": get_current_user(),
        "created_at": datetime.now().isoformat(),
    }
    append_task(task)
    print(f"✅ Task '{title}' added successfully with ID {new_id}.")


def view_tasks():
    data = read_task()
    tasks = [t for t in data["tasks"] if t["created_by"] == get_current_user()]
    if not tasks:
        print("📭 You have no tasks.")
        return
    for task in tasks:
        print(
            f"🆔 {task['id']} | 📌 {task['title']} | 📄 {task['description']} | 📊 {task['status']} | 🕒 {task['created_at']}"
        )


def search_task(query):
    data = read_task()
    tasks = [t for t in data["tasks"] if t["created_by"] == get_current_user()]
    results = [
        t for t in tasks if query.lower() in t["title"].lower() or str(t["id"]) == query
    ]
    if results:
        for t in results:
            print(
                f"🔍 Found → 🆔 {t['id']} | 📌 {t['title']} | 📄 {t['description']} | 📊 {t['status']}"
            )
    else:
        print("❌ No matching task found.")


def mark_done(task_id):
    data = read_task()
    updated = False
    for task in data["tasks"]:
        if task["id"] == task_id and task["created_by"] == get_current_user():
            task["status"] = "Done"
            updated = True
            break
    if updated:
        write_task(data)
        print("✅ Task marked as done.")
    else:
        print("❌ Task not found or permission denied.")


def edit_task(task_id, new_title, new_desc):
    data = read_task()
    for task in data["tasks"]:
        if task["id"] == task_id and task["created_by"] == get_current_user():
            task["title"] = new_title
            task["description"] = new_desc
            write_task(data)
            print("✅ Task updated.")
            return
    print("❌ Task not found or permission denied.")


def delete_task(task_id):
    data = read_task()
    for task in data["tasks"]:
        if task["id"] == task_id and task["created_by"] == get_current_user():
            data["tasks"].remove(task)
            write_task(data)
            print("🗑️ Task deleted.")
            return
    print("❌ Task not found or permission denied.")
