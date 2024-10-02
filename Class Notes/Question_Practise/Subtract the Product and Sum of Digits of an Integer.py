class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum_digits = 0
        product_digits = 1
        while n != 0:
            digit = n % 10
            sum_digits += digit
            product_digits *= digit
            n //= 10
        return product_digits - sum_digits

# Taking input from the user
n = int(input("Enter an integer: "))
solution = Solution()
result = solution.subtractProductAndSum(n)
print(f"The result of subtracting the sum from the product of digits is: {result}")
