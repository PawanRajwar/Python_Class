class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers cannot be palindromes
        if x < 0:
            return False
        
        original = x  # Store the original value of x
        ans = 0  # This will store the reversed number

        # Reverse the digits of x
        while x != 0:
            digit = x % 10
            ans = (ans * 10) + digit
            x = x // 10
        
        # Check if the reversed number equals the original number
        return original == ans

# Example usage:
sol = Solution()
num = 121
print(sol.isPalindrome(num))  # Output: True

num = -121
print(sol.isPalindrome(num))  # Output: False

num = 10
print(sol.isPalindrome(num))  # Output: False
