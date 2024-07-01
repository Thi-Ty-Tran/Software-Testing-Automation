"""
Module for handling JSON read, write and update operations.
"""

import json

class JsonHandler:
    """Class to handle JSON read, write and update operations."""

    def read_json(self, file_path):
        """Read a JSON file and return its contents."""
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data

    def write_json(self, data, file_path):
        """Write data to a JSON file."""
        with open(file_path,'w', encoding='utf-8') as f:
            json.dump(data, f)

    def check_key(self, data, key):
        """Check if a key exists in the JSON data."""
        return key in data

    def update_json(self, key, value, file_path):
        """Update a key's value in the JSON file."""
        with open(file_path, 'r+', encoding='utf-8') as f:
            data = json.load(f)
            data[key] = value
            f.seek(0)
            json.dump(data, f)
            f.truncate()
