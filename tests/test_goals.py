import pytest
import requests

from methods.goals_methods import get_all_goals, create_goal, get_goal, update_goal, delete_goal


def test_get_all_goals():
    result = get_all_goals()
    assert result.status_code == 200


def test_create_goal():
    result = create_goal()
    created_goal_id = result.json()["goal"]["id"]
    assert result.status_code == 200
    assert result.json()["goal"]["id"] == created_goal_id

def test_get_goal():
    result = get_goal()
    first_goal_id = result.json()["goal"]["id"]
    assert result.json()["goal"]["id"] == first_goal_id

def test_update_goal():
    result = update_goal()
    assert result.status_code == 200

def test_delete_goal():
    result = delete_goal()
    assert result.status_code == 200
