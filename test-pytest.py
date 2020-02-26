import pytest
import requests


def test_get_check_status_code_equals_200():
    response = requests.get("http://0.0.0.0:8081/api/tasks")
    assert response.status_code == 200


def test_get_check_content_type_equals_json():
    response = requests.get("http://0.0.0.0:8081/api/tasks")
    assert response.headers['Content-Type'] == "application/json"


def test_get_check_value_equals_hardcoded_float():
    response = requests.get("http://0.0.0.0:8081/api/tasks")
    response_body = response.json()
    assert response_body["tasks"][0]["value"] == 22.51



