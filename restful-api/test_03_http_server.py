#!/usr/bin/env python3
"""
Local test script for task_03_http_server.py
Simulates the tests from the grading system.
"""

import urllib.request
import json

BASE_URL = "http://localhost:8000"

def get(path):
    """Helper to send GET requests."""
    with urllib.request.urlopen(BASE_URL + path) as response:
        content = response.read().decode("utf-8")
        status = response.status
    return status, content


def test_root():
    status, content = get("/")
    assert status == 200, "Root endpoint did not return 200"
    assert "Hello, this is a simple API" in content, "Root endpoint returned incorrect content"
    print("Test if root endpoint returns correct content.: OK")


def test_data():
    status, content = get("/data")
    data = json.loads(content)
    assert status == 200, "Data endpoint did not return 200"
    assert data == {"name": "John", "age": 30, "city": "New York"}, "Data endpoint returned incorrect JSON"
    print("Test if data endpoint returns correct data.: OK")


def test_status():
    status, content = get("/status")
    assert status == 200, "Status endpoint did not return 200"
    assert content.strip() == "OK", "Status endpoint returned incorrect content"
    print("Test if status endpoint returns correct status.: OK")


def test_undefined():
    status, content = get("/undefined")
    assert status == 404, "Undefined endpoint did not return 404"
    assert "Endpoint not found" in content, "Undefined endpoint returned incorrect content"
    print("Test if undefined endpoint returns correct status.: OK")


if __name__ == "__main__":
    tests = [test_root, test_data, test_status, test_undefined]
    ok = 0
    for test in tests:
        try:
            test()
            ok += 1
        except AssertionError as e:
            print(f"FAIL - {e}")
    print(f"Total tests: {len(tests)}, OK: {ok}, FAIL: {len(tests) - ok}")
