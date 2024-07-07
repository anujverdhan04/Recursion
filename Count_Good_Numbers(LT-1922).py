class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        even_positions = (n + 1) // 2  # Number of even positions
        odd_positions = n // 2  # Number of odd positions
    # Calculating the power using modular exponentiation
        total_even = pow(5, even_positions, MOD)
        total_odd = pow(4, odd_positions, MOD) 
    # Total number of good digit strings
        total_good_numbers = (total_even * total_odd) % MOD
        return total_good_numbers