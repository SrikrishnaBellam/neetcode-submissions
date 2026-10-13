class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        cleaned_s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = ''.join(cleaned_s.split())
        s = s.lower()
        first_pt = 0
        last_pt = len(s) - 1
        for i in range(len(s)//2):

            if s[first_pt] != s[last_pt]: 
                return False
            else:
                first_pt += 1
                last_pt -= 1
        return True