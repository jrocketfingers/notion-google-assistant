import os

import requests
from flask import Flask, request

app = Flask(__name__)

NOTION_KEY = os.environ["NOTION_KEY"]
NOTION_DATABASE_ID = os.environ["NOTION_DATABASE_ID"]

def add_a_task_to_inbox(task_name):
    response = requests.post(
        "https://api.notion.com/v1/pages",
        headers={"Authorization": f"Bearer {NOTION_KEY}", "Notion-Version": "2021-05-13"},
        json={
            "parent": {"database_id": NOTION_DATABASE_ID},
            "properties": {
                "Name": {
                    "title": [
                        {
                            "type": "text",
                            "text": {
                                "content": task_name,
                            }
                        }
                    ],
                }
            },
        },
    )
    assert response.status_code == 200, print(response.json())

add_a_task_to_inbox("Test task")

@app.route("/new-task", methods=["GET","POST"])
def new_task():
    # data = request.json()

    # add_a_task_to_inbox("test")

    return 'OK'

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port="5000")
