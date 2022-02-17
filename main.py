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
        return num_letters[num]
  
    def tens(self, num):
        
        for_unit = self.unit(self.number[-1])
        if num in num_letters:
            return num_letters[num]

        if (self.integer > 19) and (self.integer < 30):
            return f'{num_letters["20"]}ty {for_unit}'
        elif (self.integer > 29) and (self.integer < 40):
            return f'{num_letters["30"]}ty {for_unit}'
        elif (self.integer > 49) and (self.integer < 50):
            return f'{num_letters["50"]}ty {for_unit}'
        else:
            return f'{num_letters[self.number[-2]]}ty {for_unit}'

    def hundreds(self, num):
        for_tens = self.tens(num[-2:])

        if num[1] == "0":
            return f'{num_letters[self.number[1]]} hundred and {self.unit(num[-1])}'
        else:
            return f'{num_letters[self.number[1]]} hundred and {for_tens}'
    
    def thousands(self, num):
        for_hundreds = self.hundreds(num[1:])

        if num[1] == "0":
            return f'{self.unit(num[0])} thousand, and {self.tens(num[1:])}'
        else:
            return f'{self.unit(num[0])} thousand, {self.hundreds(num[1:])}'

    def get_words(self):
        if self.number in num_letters:
            return num_letters[self.number].capitalize()
        if len(self.number) == 1:
            return self.unit(self.number)
        elif len(self.number) == 2:
            return self.tens(self.number)
        elif len(self.number) == 3:
            return self.hundreds(self.number)
        else:
            return self.thousands(self.number)
      

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


print(main())