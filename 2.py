def knapsack_dynamic_programming(weights, values, capacity):
    """
    Solves the 0/1 Knapsack problem using dynamic programming.

    :param weights: List of weights of the items
    :param values: List of values of the items
    :param capacity: Maximum capacity of the knapsack
    :return: Maximum achievable value within the given capacity
    """
    n = len(values)
    
    # Create a 2D array to store the maximum value at each n and capacity
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build the dp array in bottom-up manner
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                # Maximize value by either including or excluding the item
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                # If item cannot be included, retain the previous max value
                dp[i][w] = dp[i - 1][w]

    # The maximum value is found at dp[n][capacity]
    return dp[n][capacity]

def main():
    # Taking input from the user
    weights = list(map(int, input("Enter the weights of items separated by space: ").split()))
    values = list(map(int, input("Enter the values of items separated by space: ").split()))
    capacity = int(input("Enter the capacity of the knapsack: "))

    # Calculating and displaying the maximum value
    max_value = knapsack_dynamic_programming(weights, values, capacity)
    print("Maximum value in Knapsack =", max_value)

if __name__ == "__main__":
    main()
