"""
File: main.py
Description: This module tests othe modules (Hacker, Asset and Rig).
Author: Nenciliae Nhanga
ID: 110424563
Username: nhany003
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Rig import Rig
from Hacker import Hacker
from Asset import Asset

""" Test 1: Basic setup"""


def test_basic_setup():
    print('TEST 1: Basic Setup')
    hacker = Hacker('Zero')
    print(hacker)
    print()


""" Test 2: Acquiring a rig """


def test_acquire_rig():
    print('TEST 2: Acquiring a Rig')
    hacker = Hacker('Neo')
    print(f'Before: {hacker.inventory}')
    hacker.acquire_rig()
    print(f"After: {hacker.inventory}")
    print(hacker)
    print()


"""Test 3: Battle between two rigs"""


def test_battle():
    print('TEST 3: Battle')
    hacker1 = Hacker('Paul')
    hacker1.acquire_rig()

    hacker2 = Hacker('Ted')
    hacker2.acquire_rig()

    print(f'{hacker1.name} attacks {hacker2.name}!')
    hacker1.launch_data_spike(hacker2.rig)
    hacker1.launch_data_spike(hacker2.rig)

    print(hacker2.rig)
    print()


""" Test 4: Upgrading rig """


def test_upgrade_rig():
    print('TEST 4: Upgrading Rig')
    hacker = Hacker('Morpheus')
    hacker.acquire_rig()

    hacker.inventory.append('Hardware Patch')
    print(f'Before upgrade: {hacker.rig.get_condition()}')

    hacker.upgrade_rig()
    print(f'After upgrade: {hacker.rig.get_condition()}')
    print()


"""Test 5: Encryption/Decryption"""


def test_encryption():
    print('TEST 5: Encryption/Decryption')
    hacker = Hacker('Chad')
    hacker.inventory.append('Security Chip')
    hacker.inventory.append('Hardware Patch')

    print(f'Before: {hacker.inventory}')
    hacker.encrypt_asset('Hardware Patch')
    print(f'After encrypt: {hacker.inventory}')

    hacker.inventory.append('Security Chip')
    hacker.decrypt_asset('Hardware Patch')
    print(f'After decrypt: {hacker.inventory}')
    print()


"""Test 6: Extracting assets from broken rig"""


def test_extract_assets():
    print('TEST 6: Extracting Assets')
    attacker = Hacker('Liam')
    attacker.acquire_rig()

    victim = Hacker('Allo')
    victim.acquire_rig()
    victim.rig.storage.append('CryptoToken')
    victim.rig.storage.append('Hardware Patch')

    print(f'Victim rig storage: {victim.rig.storage}')

    attacker.launch_data_spike(victim.rig)
    attacker.launch_data_spike(victim.rig)

    attacker.extract_assets(victim.rig)
    print(f"Attacker inventory: {attacker.inventory}")
    print(f"Victim's rig storage: {victim.rig.storage}")
    print()


"""Test 7: Asset class"""


def test_asset_class():
    print('TEST 7: Asset Class')
    token = Asset('CryptoToken', 'Used to acquire rigs')
    print(token)

    chip = Asset('Security Chip', 'Encrypts assets', encrypted=True)
    print(chip)
    print()


"""Test 8: Storing and retrieving assets"""


def test_store_retrieve():
    print('TEST 8: Store and Retrieve Assets')
    hacker = Hacker('Billie')
    hacker.acquire_rig()
    hacker.inventory.append('Hardware Patch')

    print(f'Inventory: {hacker.inventory}')
    print(f'Rig storage: {hacker.rig.storage}')

    hacker.store_asset('Hardware Patch')
    print(f'After store - Inventory: {hacker.inventory}')
    print(f'After store - Rig storage: {hacker.rig.storage}')

    hacker.retrieve_asset('Hardware Patch')
    print(f'After retrieve - Inventory: {hacker.inventory}')
    print()


"""Test 9: Edge case - Upgrade without rig"""


def test_upgrade_without_rig():
    print('TEST 9: EDGE CASE - Upgrade Without Rig')
    hacker = Hacker('Alix')
    hacker.inventory.append('Hardware Patch')
    hacker.upgrade_rig()
    print()


"""Test 10: Edge case - Encrypt without Security Chip"""


def test_encrypt_without_chip():
    print('TEST 10: EDGE CASE - Encrypt Without Security Chip')
    hacker = Hacker('Lilly')
    hacker.inventory.append('Hardware Patch')
    hacker.encrypt_asset('Hardware Patch')
    print()


def run_all_tests():
    test_basic_setup()
    test_acquire_rig()
    test_battle()
    test_upgrade_rig()
    test_encryption()
    test_extract_assets()
    test_asset_class()
    test_store_retrieve()
    test_upgrade_without_rig()
    test_encrypt_without_chip()

    print('ALL TESTS COMPLETE')


if __name__ == "__main__":
    run_all_tests()
