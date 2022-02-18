"""
    Write a program that converts any number from one number base to another. The programme takes three inputs from a user: 
    Number to be converted, source base, and target base. The programme should also detect when a user inputs a number that is 
    invalid for a particular base. E.g. if the user tries to convert 12301 from base two to base eight.
"""

class BaseConversion:
    def __init__(self, source_base, number, target_base):
        self.source_base = source_base
        self.number = number
        self.target_base = target_base
    
    def two_to_ten(self):
        result = 0
        upper_bound = str(self.number)[::-1]

        for pow in range(0, len(upper_bound)):
            result += int(upper_bound[pow]) * (self.source_base ** pow)
        return result

# case = BaseConversion(2, 10011, 10)
# print(case.two_to_ten())