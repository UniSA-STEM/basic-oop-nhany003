"""
File: Hacker.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""
class Hacker:
    def __init__(self, name="", rig=None, trace_level=0):
        self.name = name
        self.rig = rig
        self.inventory = ['crypto_token']
        self.trace_level = trace_level

    def acquire_rig(self):
        if 'CryptoToken' in self.inventory:
            self.inventory.remove('CryptoToken')
            self.rig = Rig(f"{self.name}'s Rig")
            print(f"Rig acquired and activated!")
        else:
            print('Not enough tokens')

    def increase_trace(self):
        self.trace_level = self.trace_level + 1
        if self.trace_level >= 5:
            print(f'WARNING! Trace level: {self.trace_level}, {self.name} is EXPOSED')

    def exposed(self):
        if self.trace_level >= 5:
            print(f'{self.name} is EXPOSED. Cannot perform action')

    def reduce_trace(self):
        self.trace_level = self.trace_level - 1
        print(f"Trace reduced to {self.trace_level}")

    def launch_data_spike(self, target_rig):
        if self.trace_level >= 5:
            print(f'{self.name} is EXPOSED. Cannot perform action')
            return

        if 'Data Spike' not in self.rig.storage:
            print('No Data Spike available')
            return

        self.rig.storage.remove('Data Spike')
        target_rig.hit()
        self.increase_trace()
        print(f'Data spike launched!')

    def extract_assets(selfself, target_rig):
        if target_rig.broken_state == False:
            print('Target rig is not broken')
            return

        if 'Removable Drive' not in self.rig.storage:
            print('No removable drive available')
            return

    self.rig.storage.remove('Removable Drive')

    for asset in target_rig.storage[:]:
        if '(Encrypted)' not in asset:
            target_rig.storage.remove(asset)
            self.inventory.append(asset)

    print('Assets extracted!')


def encrypt_asset(self, asset):

    if 'Security Chip' not in self.inventory:
        print('No Security Chip available')
        return

    if asset not in self.inventory:
        print(f'{asset} not found')
        return

    self.inventory.remove('Security Chip')
    self.inventory.remove(asset)
    self.inventory.append(f'{asset} (Encrypted)')
    print(f'{asset} encrypted!')

    def decrypt_asset(self, asset):
        encrypted = f'{asset} (Encrypted)'

        if 'Security Chip' not in self.inventory:
            print('No Security Chip available')
            return

        if encrypted not in self.inventory:
            print(f'{encrypted} not found')
            return

        self.inventory.remove('Security Chip')
        self.inventory.remove(encrypted)
        self.inventory.append(asset)
        print(f'{asset} decrypted!')

    def upgrade_rig(self):
        if 'Hardware Patch' not in self.inventory:
            print('No Hardware Patch available')
            return
        self.inventory.remove('Hardware Patch')
        self.rig.upgrade()

    def store_asset(self, asset):
        if asset in self.inventory:
            self.inventory.remove(asset)
            self.rig.storage.append(asset)
            print(f'{asset} stored in rig')
        else:
            print(f'{asset} not in inventory')

    def retrieve_asset(self, asset):
        if asset in self.rig.storage:
            self.rig.storage.remove(asset)
            self.inventory.append(asset)
            print(f'{asset} retrieved')
        else:
            print(f'{asset} not in rig')

    def scan_inventory(self, asset_name):
        if asset_name in self.inventory:
            self.inventory.remove(asset_name)
            return asset_name
        else:
            print(f'{asset_name} not found')
            return None
