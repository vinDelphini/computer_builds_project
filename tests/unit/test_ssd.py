"""
Test for SSD class
Command line: python3 -m tests/unit/test_ssd.py
"""

import pytest
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
models_path = os.path.join(current_dir, '..', '..', 'app', 'models')
sys.path.append(models_path)

from inventory import SSD

@pytest.fixture
def ssd_values():
    return {
        "name": "Samsung 860 EVO",
        "manufacturer": "Samsung",
        "total": 10,
        "allocated": 3,
        "capacity_gb": 1_000,
        "interface": "SATA III"
    }

@pytest.fixture
def ssd(ssd_values):
    return SSD(**ssd_values)

def test_create(ssd, ssd_values):
    for attr_name in ssd_values:
        assert getattr(ssd, attr_name) == ssd_values.get(attr_name)

@pytest.mark.parametrize("interface", [1, 10.5, True, 3 + 4j, None])
def test_create_invalid_interface(interface, ssd_values):
    ssd_values["interface"] = interface
    with pytest.raises(TypeError):
        SSD(**ssd_values)

def test_repr(ssd):
    assert ssd.category in repr(ssd)
    assert str(ssd.capacity_gb) in repr(ssd)
    assert ssd.interface in repr(ssd)
    