class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        merged_string = ""

        for i in range(min(len(word1), len(word2))):
            merged_string += word1[i]
            merged_string += word2[i]
        
        start = min(len(word1), len(word2))

        if len(word1) > len(word2):
            merged_string += word1[start:]
        else:
            merged_string += word2[start:]
        
        return merged_string