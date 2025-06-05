import requests
from faker import Faker
fake = Faker()

import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("TOKEN")
url = os.getenv("CLICKUP_API_URL")


headers = {"Authorization": token}

def get_all_goals():
    return requests.get(url+"team/90151226803/goal",headers=headers)

def create_goal():
    body = {"name": fake.name()}
    return requests.post(url+"team/90151226803/goal",headers=headers, json=body)

def get_goal():
    result = requests.get(url+"team/90151226803/goal", headers=headers)
    first_goal_id = result.json()["goals"][0]["id"]
    return requests.get("https://api.clickup.com/api/v2/goal/"+first_goal_id, headers=headers)

def update_goal():
    result = create_goal()
    created_goal_id = result.json()["goal"]["id"]
    assert result.json()["goal"]["id"] == created_goal_id
    goal_name_updated = {"name": fake.name()}
    body_for_goal_updated = {"name": goal_name_updated}
    result = requests.put(url + "goal/" + created_goal_id, headers=headers, json=body_for_goal_updated)
    # assert result.json()["goal"]["name"] == goal_name_updated
    return requests.delete(url + "goal/" + created_goal_id, headers=headers)

def delete_goal():
    result = get_all_goals()
    first_goal_id = result.json()["goals"][0]["id"]
    return requests.delete(url + "goal/" + first_goal_id, headers=headers)