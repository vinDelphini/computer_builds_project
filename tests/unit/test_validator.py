"""
Tests the validator functions
Command line: python3 -m pytest tests/test_validators.py
"""

import pytest
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
utils_path = os.path.join(current_dir, '..', '..', 'app', 'utils')
sys.path.append(utils_path)

from validators import validate_integer


class TestIntegerValidator:

    def test_valid(self):
        validate_integer("arg", 10, 0, 20, "custom min message", "custom max message")
    
    def test_type_error(self):
        with pytest.raises(TypeError):
            validate_integer('arg', 1.5)
    
    def test_min_std_err_msg(self):
        with pytest.raises(ValueError) as ex:
            validate_integer("arg", 10, 100)
        assert "arg" in str(ex.value)
        assert "100" in str(ex.value)
    
    def test_min_custom_msg(self):
        with pytest.raises(ValueError) as ex:
            validate_integer("arg", 10, 100, custom_min_message="custom")
        assert "custom" == str(ex.value)
    
    def test_max_std_err_msg(self):
        with pytest.raises(ValueError) as ex:
            validate_integer("arg", 10, min_value=1, max_value=5)
        assert "arg" in str(ex.value)
        assert "5" in str(ex.value)
    
    def test_max_custom_err_msg(self):
        with pytest.raises(ValueError) as ex:
            validate_integer("arg", 100, max_value=5, custom_max_message="custom")
        assert "custom" == str(ex.value)
        