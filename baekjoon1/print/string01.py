# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        resultstr = ''
        # 1. 기호를 제거한다.
        for i in s:
            if s.isalnum():
                resultstr = resultstr.join(i.lower)

        #2. 결과를 resultstr에 넣는다. 

        return result


solution = Solution()
isPalindrome("A man, a plan, a canal: Panama")