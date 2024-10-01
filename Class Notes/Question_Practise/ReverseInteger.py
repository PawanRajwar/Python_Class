class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        # Determine the sign of the integer
        sign = -1 if x < 0 else 1
        # Work with the absolute value
        x = abs(x)
        
        while x != 0:
            digit = x % 10  # Extract the last digit
            # Check for overflow before updating `ans`
            if ans > (2**31 - 1) // 10:  # equivalent to INT_MAX / 10
                return 0
            ans = ans * 10 + digit
            x //= 10  # Move to the next digit
        
        ans *= sign  # Restore the original sign

        # Handle overflow conditions for 32-bit integer range
        if ans < -2**31 or ans > 2**31 - 1:
            return 0
        
        return ans

# Example usage:
sol = Solution()
num = 12345
print(sol.reverse(num))  # Output: 54321
