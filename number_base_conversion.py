"""
    Write a program that converts any number from one number base to another. The programme takes three inputs from a user: 
    Number to be converted, source base, and target base. The programme should also detect when a user inputs a number that is 
    invalid for a particular base. E.g. if the user tries to convert 12301 from base two to base eight.
"""

class BaseConversion:
    def __init__(self, from_base, number, to_base):
        self.from_base = from_base
        self.number = number
        self.to_base = to_base