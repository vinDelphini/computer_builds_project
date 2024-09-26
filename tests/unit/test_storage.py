"""
Tests for Storage class
Command line: python3 -m pytest tests/unit/test_storage.py
"""
import pytest
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
models_path = os.path.join(current_dir, '..', '..', 'app', 'models')
sys.path.append(models_path)

from inventory import Storage

@pytest.fixture
def storage_values():
    return {
        "name": "Thumbdrive",
        "manufacturer": "Sandisk",
        "total": 10,
        "allocated": 3,
        "capacity_gb": 512
    }

@pytest.fixture
def storage(storage_values):
    return Storage(**storage_values)

def test_create(storage, storage_values):
    for attr_name in storage_values:
        assert getattr(storage, attr_name) == storage_values.get(attr_name)

@pytest.mark.parametrize("gb, exception", [(10.5, TypeError), (0, ValueError), (-1, ValueError)])
def test_create_invalid_storage(gb, exception, storage_values):
    storage_values["capacity_gb"] = gb
    with pytest.raises(exception):
        Storage(**storage_values)

def test_repr(storage):
    assert storage.category in repr(storage)
    assert str(storage.capacity_gb) in repr(storage)
