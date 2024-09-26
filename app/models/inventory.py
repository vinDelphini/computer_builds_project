"""Inventory Models"""

import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
utils_path = os.path.join(current_dir, '..', 'utils')
sys.path.append(utils_path)

from validators import validate_integer, validate_string


class Resource:

    def __init__(self, name, manufacturer, total, allocated):
        self._name = name
        self._manufacturer = manufacturer

        validate_integer('total', total, min_value=0)
        self._total = total

        validate_integer(
            'allocated', allocated, 0, total,
            custom_max_message="Allocated inventory cannot exceed total inventory"        
        )
        self._allocated = allocated

    @property
    def name(self):
        return self._name
    
    @property
    def manufacturer(self):
        return self._manufacturer

    @property
    def total(self):
        return self._total

    @property
    def allocated(self):
        return self._allocated
    
    @property
    def category(self):
        return type(self).__name__.lower()
    
    @property
    def available(self):
        return self.total - self.allocated
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return (f"{self.name} ({self.category} - {self.manufacturer}) : "
                f"total={self.total}, allocated={self.allocated}"
                )
    
    def claim(self, num):
        """when you claim it goes to in use"""
        validate_integer(
            "num", num, 1, self.available,
            custom_max_message="Cannot claim more than available"
        )
        self._allocated += num
        
    def freeup(self, num):
        """Return an inventory item to the available pool"""
        validate_integer(
            "num", num, 1, self.allocated,
            custom_max_message="Cannot return more than allocated"
            )
        self._allocated -= num
    
    def died(self, num):
        validate_integer(
            "num", num, 1, self.allocated,
            custom_max_message="Cannot retire more than allocated"
        )
        self._total -= num
        self._allocated -= num
    
    def purchased(self, num):
        validate_integer("num", num, 1)
        self._total += num


class CPU(Resource):
    """Resource subclass used to track specific CPU inventory pools"""

    def __init__(
        self, name, manufacturer, total, allocated,
        cores, socket, power_watts
        ):
        super().__init__(name, manufacturer, total, allocated)

        validate_integer("cores", cores, 1)
        validate_integer("power_watts", power_watts, 1)

        self._cores = cores
        self._socket = socket
        self._power_watts = power_watts

    @property
    def cores(self):
        return self._cores
    
    @property
    def socket(self):
        return self._socket
    
    @property
    def power_watts(self):
        return self._power_watts
    
    def __repr__(self):
        return f"{self.category}: {self.name} ({self.socket} - x{self.cores})"


class Storage(Resource):

    def __init__(
        self, name, manufacturer, total, allocated,
        capacity_gb
        ):
        super().__init__(name, manufacturer, total, allocated)
        validate_integer("capacity_gb", capacity_gb, 1)
        self._capacity_gb = capacity_gb

    @property
    def capacity_gb(self):
        return self._capacity_gb
    
    def __repr__(self):
        return f"{self.category}: {self.capacity_gb} GB"
    

class HDD(Storage):

    def __init__(
        self, name, manufacturer, total, allocated, capacity_gb,
        size, rpm
        ):
        super().__init__(name, manufacturer, total, allocated, capacity_gb)
        
        allowed_sizes = ['2.5"', '3.5"']
        if size not in allowed_sizes:
            raise ValueError(f'Invalid HDD size. '
                            f'Must be one of {", ".join(allowed_sizes)}')
        validate_integer("rpm", rpm, min_value=1_000, max_value=50_000)

        self._size = size
        self._rpm = rpm
    
    @property
    def size(self):
        return self._size

    @property
    def rpm(self):
        return self._rpm
    
    def __repr__(self):
        s = super().__repr__()
        return f"{s} ({self.size}, {self.rpm} rpm)"


class SSD(Storage):

    def __init__(
        self, name, manufacturer, total, allocated, capacity_gb,
        interface
        ):
        super().__init__(name, manufacturer, total, allocated, capacity_gb)
        validate_string("interface", interface, "Must be a valid interface name.")
        self._interface = interface

    @property
    def interface(self):
        return self._interface

    def __repr__(self):
        s = super().__repr__()
        return f"{s} ({self.interface})"
