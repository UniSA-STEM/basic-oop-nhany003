"""
File: Asset.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""


class Asset:
    def __init__(self, name='', description='', encrypted=False):
        self.name = name
        self.description = description
        self.encrypted = encrypted

    def __str__(self):
        if self.encrypted:
            return f'<{self.name}>: <{self.description}> [Encrypted]'
        else:
            return f'{self.name}: {self.description}'
