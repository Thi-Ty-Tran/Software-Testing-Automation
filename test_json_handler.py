"""
Tests for the JsonHandler class.
"""

import pytest
from json_handler import JsonHandler  #assuming the class is in json_handler.py

def requirement(req_id):
    """Decorator to assign a requirement ID to a test function."""
    def decorator(function):
        function.requirement = req_id
        return function
    return decorator

@pytest.fixture
def json_handler_instance():
    """Provides a JsonHandler instance for tests."""
    return JsonHandler()

@pytest.fixture
def temp_json_file(tmp_path):
    """Creates a temporary JSON file for tests."""
    return tmp_path / "test.json"

@requirement("REQ-101")
def test_read_json(json_handler_instance, temp_json_file):
    """Test the read_json method."""
    data = {"test": "data"}
    json_handler_instance.write_json(data, temp_json_file)
    read_data = json_handler_instance.read_json(temp_json_file)
    assert read_data == data

@requirement("REQ-102")
def test_write_json(json_handler_instance, temp_json_file):
    """Test the write_json method."""
    data = {"test": "data"}
    json_handler_instance.write_json(data, temp_json_file)
    read_data = json_handler_instance.read_json(temp_json_file)
    assert read_data == data

@requirement("REQ-103")
def test_check_key(json_handler_instance):
    """Test check_key method."""
    data = {"test": "data"}
    assert json_handler_instance.check_key(data, 'test')

@requirement("REQ-104")
def test_update_json(json_handler_instance, temp_json_file):
    """Test update_json method."""
    data = {"test": "data"}
    json_handler_instance.write_json(data, temp_json_file)
    json_handler_instance.update_json("test", "new data", temp_json_file)
    updated_data = json_handler_instance.read_json(temp_json_file)
    assert updated_data["test"] == "new data"
