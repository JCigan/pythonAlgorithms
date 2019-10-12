#!/usr/bin/env python3

class Solution:
    def __init__(self):
        self.singleDigits = {
            1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven',
            8: 'eight', 9: 'nine'
        }
        self.teens = {
            10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
            19: 'nineteen'
        }
        self.doubleDigitPrefixes = {
            2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty',
            7: 'seventy', 8: 'eighty', 9: 'ninety'
        }

    def numberWord(self, num):
        try:
            if int(num) != num:
                raise Exception('Input must be an integer')
        except ValueError:
            raise Exception('Input value must be a number')
        if num > 1000000 or num < 0:
            raise Exception('Please enter a non-negative integer less than 1,000,000')
        if num == 1000000:
            return "one million"
        if num == 0:
            return "zero"
        return self.getWord(num)

    def getWord(self, num):
        if num < 10:
            return self.singleDigits[num]
        if num < 100:
            return self.getDoubleDigitWord(num)
        if num < 1000:
            return self.getTripleDigitWord(num)
        else:
            return self.getThousandsWord(num)

    def getDoubleDigitWord(self, num):
        if num < 20:
            return self.teens[num]
        else:
            tens = num // 10
            ones = num % 10
            word = self.doubleDigitPrefixes[tens]
            return word if not ones else '{}-{}'.format(word, self.singleDigits[ones])

    def getTripleDigitWord(self, num):
        hundreds = num // 100
        addend = num % 100
        word = '{} hundred'.format(self.singleDigits[hundreds])
        return word if not addend else '{} {}'.format(word, self.getWord(addend))

    def getThousandsWord(self, num):
        thousands = num // 1000
        addend = num % 1000
        word = '{} thousand'.format(self.getWord(thousands))
        return word if not addend else '{} {}'.format(word, self.getWord(addend))
