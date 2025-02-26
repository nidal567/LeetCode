class Solution:
    def countPrimes(self, n: int) -> int:
        #Base case
        if n <= 2:
            return 0
        
        # iterate up to sqrt(n), as factors repeat beyond range
        prime = [0] * n # initialize prime numbers list
        for i in range(2, int(n**0.5) + 1):
            if prime[i] == 0:
                for j in range(i * i, n, i):
                    prime[j] = 1
        # Essentially gives the total count of prime numbers less than n
        return sum(1 for i in range(2, n) if prime[i] == 0)