"""
    Write a program that converts a number in the range [0…10000] to words,
    corresponding to the English pronunciation.

    constraints = [0, 10, 19, 37, 405, 1047, 4598]
"""

num_letters = { 
  "0": "", "1": "one" , "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven", 
  "8": "eight", "9": "nine", "10": "ten", "11": "eleven", "12": "twelve", "13": "thirteen", 
  "14": "fourteen", "15": "fifteen", "16": "sixteeen", "17": "seventeen", "18": "eighteen",
  "19": "nineteen", "20": "twenty", "30": "thirty", "40": "fourty", "50": "fifty", "60": "sixty",
  "70": "seventy", "80": "eighty", "90": "ninety", "100": "one hundred", "1000": "one thousand", 
  "10000": "ten thousand"
}


class Measuration:
    def __init__(self, number):
        self.number = number
        self.integer = int(number)
    
    def unit(self, num):
        if num == '0':
            return ''
        return num_letters[num]
  
    def tens(self, num):
        num_int = int(num)

        if num in num_letters:
            return num_letters[num]
        elif num[0] == '0':
            return f'{self.unit(num[-1])}'
        else:
            new_num = num[0] + '0'
            return f'{num_letters[new_num]} {self.unit(num[-1])}'

    def hundreds(self, num):
        num_int = int(num)
        h = self.unit(num[0])
        t = self.tens(num[1:])
        u = self.unit(num[-1])
        
        if num[1:] == '00':
            return f'{h} hundred'
        elif len(str(num_int % 100)) == 2:
            return f'{h} hundred and {t}'
        else:
            return f'{h} hundred and {u}'
    
    def thousands(self, num):
        num_int = int(num)
        th = self.unit(num[0])
        h = self.hundreds(num[1:])
        t = self.tens(num[2:])
        u = self.unit(num[-1])

        if num[1:] == '000':
            return f'{th} thousand'
        elif len(str(num_int % 1000)) == 3:
            return f'{th} thousand, {h}' 
        elif len(str(num_int % 1000)) == 2:
            return f'{th} thousand and {t}'
        elif len(str(num_int % 1000)) == 1:
            return f'{th} thousand  and {u}'

    def tens_of_thousands(self, num):
        num_int = int(num)
        tt = self.unit(num[0] + '0') 
        t = self.thousands(num[1:])

        if num[1:] == '0000':
            return f'{tt} thousand'
        elif (len(str(num_int % 10000)) == 4) or (len(str(num_int % 10000)) == 3):
            return f'{tt} {t}'
            
    def get_words(self):
        if len(self.number) == 1:
            return self.unit(self.number)
        elif len(self.number) == 2:
            return self.tens(self.number)
        elif len(self.number) == 3:
            return self.hundreds(self.number)
        elif len(self.number) == 4:
            return self.thousands(self.number)
        else:
            return self.tens_of_thousands(self.number)
      

def main():
    user_input = input("Enter numbers you want to convert into words: \n")

    if user_input == "0":
        print("Zero")
   
    try: 
        numbers_words = Measuration(user_input)
        return numbers_words.get_words()
    except ValueError:
        print("Please enter a valid number")
        main()


print(main().capitalize())