"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit
numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def isPalindrome(n):

    digits = list(str(n))
    reved = list(str(n))[::-1]

    for i in range(len(reved)):
        if reved[i] != digits[i]:
            return False

    return True


def findLargestPalindrome(digits):

    maxNum = int('9' * digits)
    minNum = 10**(digits-1)
    maxFound = 0

    for x in range(maxNum):
        for y in range(maxNum):
            product = x * y
            if isPalindrome(product):
                if product > maxFound:
                    maxFound = product
                    factors = [x, y]

    return [x, y, maxFound]




if __name__ == '__main__':
    print(isPalindrome(9900))
    print(isPalindrome(9009))

    print(findLargestPalindrome(3))
