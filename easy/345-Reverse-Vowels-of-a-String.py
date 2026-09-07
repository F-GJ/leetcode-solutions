class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        positions = []

        #Find all vowel indices
        for index, char in enumerate(s):
            if char.lower() in vowels:
                positions.append(index)
        
        #Convert the word to list
        s_list = list(s)

        for x, y in zip(positions, positions[::-1]):
            s_list[x] = s[y]
        
        return "".join(s_list)
        