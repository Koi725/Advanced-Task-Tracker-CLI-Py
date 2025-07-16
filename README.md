# 🗂️ Task Tracker CLI Application

This is a **Command-Line Based Task Management App** that allows users to register, log in, and manage their personal to-do tasks efficiently.

---

## 🚀 Features

- 🔐 **User Authentication** (Sign Up / Login)
- ✍️ **Add Tasks** with Title & Description
- 📋 **View All Tasks** (Only Yours!)
- 🔍 **Search Tasks** by ID or Title
- ✅ **Mark Tasks as Done**
- 📝 **Edit Tasks** (Only your own)
- 🗑️ **Delete Tasks**
- 🧠 All tasks are linked to the currently logged-in user

---

## 📁 Project Structure

```
Task_tracker/
│
├── main.py                # Main driver program (menu + logic)
├── auth.py                # User login and signup logic
├── utils/
│   ├── auth_utils.py      # File handling and user session
│   └── task_utils.py      # JSON I/O for tasks
├── task_manager.py        # Task operation logic (CRUD)
├── users.json             # Stores registered users
└── tasks.json             # Stores all tasks linked to users
```

---

## 📦 Dependencies

- Python 3.x

> No external packages required. Uses built-in libraries: `json`, `os`, `datetime`.

---

## 🛠️ How to Run

1. Clone the repo:
   
   ```bash
   git clone https://github.com/yourusername/Task_tracker.git
   cd Task_tracker
   ```

2. Run the app:
   
   ```bash
   python3 main.py
   ```

---

## 🔐 Example Users

You can register as a new user or manually add entries into `users.json`.

```json
{
  "users": [
    {
      "id": 1,
      "name": "kousha",
      "password": "1234"
    }
  ]
}
```

---



## 👨‍💻 Developed by Kousha
