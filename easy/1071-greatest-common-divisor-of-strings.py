from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        #establish possible answer length
        gcd_length = gcd(len(str1), len(str2))

        #Determine if the two strings have the same repeating pattern
        if str1 + str2 != str2 + str1:
            #if not return an empty string
            return ""
        
        #Otherwise return the first gcd_length characters
        return str1[:gcd_length]