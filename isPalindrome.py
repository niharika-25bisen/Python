def isPalindrome(s):
    if len(s) <= 1:
        return True
    
    if s[0] != s[-1]:
        return False
    
    return isPalindrome(s[1:-1])
print(isPalindrome("racecar"))  # True
print(isPalindrome("hello"))  # False