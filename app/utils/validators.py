"""Various Validators"""

def validate_integer(
    arg_name, arg_value, min_value=None, max_value=None,
    custom_min_message=None, custom_max_message=None
):
    if not isinstance(arg_value, int):
        raise TypeError(f"{arg_name} must be an integer.")
    
    if min_value is not None and arg_value < min_value:
        if custom_min_message is not None:
            raise ValueError(custom_min_message)
        raise ValueError(f"{arg_name} cannot be less than {min_value}")

    if max_value is not None and arg_value > max_value:
        if custom_max_message is not None:
            raise ValueError(custom_max_message)
        raise ValueError(f"{arg_name} cannot be greater than {max_value}") 

def validate_string(arg_name, arg_value, custom_error_message=None):
    if not isinstance(arg_value, str):
        raise TypeError(f"{arg_name} must be a string.")
        
# a = validate_integer("total", -10, 0, 20, custom_max_message="cannot exceed 20")
# print(a)
