n = int(input("Enter number of houses: "))

money = []

for i in range(n):
    amount = int(input(f"Enter amount in house {i + 1}: "))
    money.append(amount)

if n == 0:
    maximum = 0
elif n == 1:
    maximum = money[0]
else:
    dp = [0] * n
    dp[0] = money[0]
    dp[1] = max(money[0], money[1])
    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + money[i])
    maximum = dp[n - 1]
print("Maximum possible amount:", maximum)

"""
Enter number of houses: 5
Enter amount in house 1: 50000
Enter amount in house 2: 40000
Enter amount in house 3: 80000
Enter amount in house 4: 60000
Enter amount in house 5: 40000
Maximum possible amount: 170000
"""
