"""
File: Hacker.py
Description: The Hacker module includes a class that can acquire a rig, perform attacks and manage digital assets
Author: Nenciliae Nhanga
ID: 110424563
Username: nhany003
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Rig import Rig


class Hacker:
    def __init__(self, name='', rig=False, trace_level=0):
        self.name = name
        self.rig = rig
        self.inventory = ['CryptoToken']
        self.trace_level = trace_level

    def acquire_rig(self):
        if 'CryptoToken' in self.inventory:
            self.inventory.remove('CryptoToken')
            self.rig = Rig(f'{self.name} Rig')
            print('Rig acquired and activated')
        else:
            print('Not enough tokens')

    def increase_trace(self):
        self.trace_level = self.trace_level + 1
        if self.trace_level >= 5:
            print(f'WARNING! Trace level: {self.trace_level}')

    def exposed(self):
        if self.trace_level >= 5:
            print(f'{self.name} is EXPOSED. Cannot perform action')

    def reduce_trace(self):
        self.trace_level = self.trace_level - 1

    def launch_data_spike(self, target_rig):
        if self.trace_level >= 5:
            print(f'{self.name} is EXPOSED. Cannot perform action')
            return

        if self.rig is False:
            print('No rig available')
            return

        if 'Data Spike' not in self.rig.storage:
            print('No data spike available')
            return

        self.rig.storage.remove('Data Spike')
        target_rig.hit()
        self.increase_trace()
        print('Data spike launched')

    def extract_assets(self, target_rig):
        if self.rig is False:
            print('No rig available')
            return

        if not target_rig.broken_state:
            print('Target rig is not broken')
            return

        if 'Removable Drive' not in self.rig.storage:
            print('No removable drive available')
            return

        self.rig.storage.remove('Removable Drive')

        for asset in target_rig.storage:
            if '(Encrypted)' not in asset:
                target_rig.storage.remove(asset)
                self.inventory.append(asset)

    def encrypt_asset(self, asset):
        if 'Security Chip' not in self.inventory:
            print('No security chip available')
            return

        self.inventory.remove('Security Chip')
        self.inventory.append(f'{asset} (Encrypted)')

    def decrypt_asset(self, asset):
        encrypted = f'{asset} (Encrypted)'

        if 'Security Chip' not in self.inventory:
            print('No security chip available')
            return

        self.inventory.remove('Security Chip')
        self.inventory.remove(encrypted)
        self.inventory.append(asset)

    def upgrade_rig(self):
        if self.rig is False:
            print('No rig available')
            return
        if 'Hardware Patch' not in self.inventory:
            print('No hardware patch available')
            return
        self.inventory.remove('Hardware Patch')
        self.rig.upgrade()

    def store_asset(self, asset):
        if self.rig is False:
            print('No rig available')
            return
        if asset in self.inventory:
            self.inventory.remove(asset)
            self.rig.storage.append(asset)
            print(f'{asset} stored in rig')
        else:
            print(f'{asset} not in inventory')

    def retrieve_asset(self, asset):
        if self.rig is False:
            print('No rig available')
            return
        if asset in self.rig.storage:
            self.rig.storage.remove(asset)
            self.inventory.append(asset)
            print(f'{asset} retrieved')
        else:
            print(f'{asset} not in rig')


    def take_asset(self, asset_name):
        if asset_name in self.inventory:
            self.inventory.remove(asset_name)
            return asset_name
        else:
            print(f'{asset_name} not found')
            return None

    def __str__(self):
        if self.rig:
            rig_name = self.rig.name
        else:
            rig_name = 'None'

        inventory_list = ', '.join(self.inventory)

        return (f"Hacker: {self.name}\n"
                f"Rig: {rig_name}\n"
                f"Trace Level: {self.trace_level}\n"
                f"Inventory: {inventory_list}")
