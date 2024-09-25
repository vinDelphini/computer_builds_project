"""Inventory Models"""

import sys
sys.path.append('/home/vin/OOP_object_oriented_programming/3_computer_builds/app/utils')
from validators import validate_integer

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
