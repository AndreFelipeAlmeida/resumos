def main():
    cost = list(map(int, input().split()))

    n = len(cost)

    if n == 1:
        print(cost[0])
        return

    dp = [0] * n

    dp[0] = cost[0]
    dp[1] = cost[1]

    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

    print(min(dp[-1], dp[-2]))


if __name__ == "__main__":
    main()
