"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""


class Rig:
    def __init__(self, name='', damage_counter=0, broken_state=False, storage=None, data_spike=2, removable_drive=1,
                 upgrade_level=0):
        if storage is None:
            storage = []
        self.name = name
        self.damage_counter = damage_counter
        self.broken_state = broken_state
        self.storage = storage
        self.data_spike = data_spike
        self.removable_drive = removable_drive
        self.upgrade_level = upgrade_level

    def hit(self):
        self.damage_counter += 1
        print(f'Rig hit! Damage: {self.damage_counter}')

        if self.damage_counter >= 2:
            self.broken_state = True
            print('Rig is broken!')

