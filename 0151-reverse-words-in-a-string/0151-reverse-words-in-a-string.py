class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip() #remove spaces from start and end 
        s=s.split() #split string 
        s.reverse() #reverse string
        return " ".join(s) #join string with " "