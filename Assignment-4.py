#Memoization (Top-Down DP)
def fib(n, dp):
    if n <= 1:
        return n

    if dp[n] != -1:
        return dp[n]

    dp[n] = fib(n - 1, dp) + fib(n - 2, dp)
    return dp[n]

#Tabulation (Bottom-Up DP)
def fibonacci_tab(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


n = int(input("Enter number: "))
dp = [-1] * (n + 1)
print("Select Method to use\n1.Memoization Method\n2.Tabulation Method")
choice = int(input("Enter your choice:"))
match choice:
    case 1:
        print("Fibonacci Number:", fib(n, dp))
    case 2:
        print("Fibonacci Number:", fibonacci_tab(n))
    case _:
        print("Select only from given options")

"""
Output 1 :-
Select Method to use
1.Memoization Method
2.Tabulation Method
Enter your choice:1
Fibonacci Number: 139583862445

Output 2 :-
Select Method to use
1.Memoization Method
2.Tabulation Method
Enter your choice:2
Fibonacci Number: 34
"""