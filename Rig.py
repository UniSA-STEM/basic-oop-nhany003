"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""


import random
class Rig:
    def __init__(self, name='', damage_counter=0, broken_state=False, data_spike=2, removable_drive=1,
                 upgrade_level=0):
        self.name = name
        self.damage_counter = damage_counter
        self.broken_state = broken_state
        self.storage = ['Data Spike', 'Data Spike', 'Removable Drive']
        self.data_spike = data_spike
        self.removable_drive = removable_drive
        self.upgrade_level = upgrade_level

    def hit(self):
        self.damage_counter += 1
        print(f'Rig hit! Damage: {self.damage_counter}')

        if self.damage_counter >= 2:
            self.broken_state = True
            print('Rig is broken!')

    def generate_asset(self):
        possible_assets = ['CryptoToken', 'Hardware Patch', 'Data Spike', 'Removable Drive']
        asset = random.choice(possible_assets)
        print(f'Generated: {asset}')
        return asset

    def store_asset(self,asset):
        self.storage.append(asset)

    def transfer_asset(self,asset):
        if asset in self.storage:
            self.storage.remove(asset)
            return asset
        else:
            print(f'{asset} not found in storage')
            return None

    def repair(self):
        if self.damage_counter >= 2:
            self.damage_counter = 0
            self.broken_state = False
        else:
            print('No repair needed')

    def upgrade(self):
        self.upgrade_level += 1

    def get_condition(self):
        if self.broken_state:
            condition = 'broken'
        elif self.damage_counter == 0:
            condition = 'pristine'
        else:
            condition = 'damaged'
        return f'{condition} (Level {self.upgrade_level})'
















