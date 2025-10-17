"""
File: Hacker.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""
class Hacker:
    def __init__(self, name="", rig=False, crypto_token=1, trace_level=0):
        self.name = name
        self.rig = rig
        self.crypto_token = crypto_token
        self.trace_level = trace_level

    def accquire_rig(self):
        if self.crypto_token >= 1:
            self.crypto_token -= 1
            self.rig = True
            print('Rig acquired and activated')
        else:
            print('Not enough tokens')

    def increase_trace(self, amount=1):
        self.trace_level += amount
        if self.trace_level >=5:
            print(f'WARNING! Trace level: {self.trace_level}, {self.name} is EXPOSED')

    def exposed(self):
        if self.trace_level >= 5:
            print(f'{self.name} is EXPOSED. Cannot perform action')

    def reduce_trace(self, amount=1):
        self.trace_level = self.trace_level - amount
        print(f"Trace reduced to {self.trace_level}")
