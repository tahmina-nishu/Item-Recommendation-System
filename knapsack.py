def knapsack(items, max_budget):
    n = len(items)
    dp = [[0] * (max_budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        price = items[i-1]["price"]
        value = items[i-1]["value"]
        for w in range(max_budget + 1):
            if price <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - price] + value)
            else:
                dp[i][w] = dp[i-1][w]

    # Backtracking to find selected items
    selected_items = []
    w = max_budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(items[i-1])
            w -= items[i-1]["price"]

    return dp[n][max_budget], selected_items
