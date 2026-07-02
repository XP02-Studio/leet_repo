class Solution:
    def isPalindrome(self, x: int) -> bool:
        word = str(x)
        i,j=0, len(word)-1
        is_palindrome=True
        while(i<j):
            if word[i]!=word[j]:
                is_palindrome=False
                break
            i+=1
            j-=1
        return is_palindrome