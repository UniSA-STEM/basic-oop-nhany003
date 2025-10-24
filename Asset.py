"""
File: Asset.py
Description: This module features an asset class that represents items
Author: Nenciliae Nhanga
ID: 110424563
Username: nhany003
This is my own work as defined by the University's Academic Misconduct Policy.
"""


class Asset:
    def __init__(self, name='', description='', encrypted=False):
        self.name = name
        self.description = description
        self.encrypted = encrypted

    def __str__(self):
        if self.encrypted:
            return f'{self.name}: {self.description} [Encrypted]'
        else:
            return f'{self.name}: {self.description}'
