'''
This problem was asked by Airbnb.

You are given an array X of floating-point numbers x1, x2, ... xn.
 These can be rounded up or down to create a corresponding array Y of integers y1, y2, ... yn.

Write an algorithm that finds an appropriate Y array with the following properties:

The rounded sums of both arrays should be equal.
The absolute pairwise difference between elements is minimized.
 In other words, |x1- y1| + |x2- y2| + ... + |xn- yn| should be as small as possible.
For example, suppose your input is [1.3, 2.3, 4.4]. 
In this case you cannot do better than [1, 2, 5], which has an absolute difference of |1.3 - 1| + |2.3 - 2| + |4.4 - 5| = 1.
'''
import math

def find_corresponding_array(X):
    """
    Find an appropriate Y array based on the given properties.
    
    Args:
    X (list of float): Input array of floating-point numbers.
    
    Returns:
    list of int: Corresponding array Y with minimized absolute pairwise differences.
    """
    # Calculate the actual sum of the input array
    actual_sum = sum(X)
    print(f"Actual sum of X: {actual_sum}")

    # Calculate the rounded sums
    rounded_sum = math.floor(sum(math.floor(x) for x in X))
    print(f"Rounded sum of X: {rounded_sum}")

    # Initialize the corresponding array Y
    Y = [math.floor(x) for x in X]
    
    # Calc the fractional part of the input array
    fractional_parts = [(x - math.floor(x), i) for i, x in enumerate(X)]

    # Calculate the difference needed to match the rounded sum
    difference = round(actual_sum) - rounded_sum
    print(f"Difference needed to match rounded sum: {difference}")

    # Sort indices based on fractional parts in descending order
    fractional_parts.sort(reverse=True, key=lambda x: x[0])
    print(f"Sorted fractional parts: {fractional_parts}")

    for i in range(int(difference)):
        # Increment the Y value at the index of the largest fractional part
        index = fractional_parts[i][1]
        Y[index] += 1
        print(f"Incrementing Y at index {index}: {Y}")
    
    return Y

def main():
    # Example input
    X = [1.5, 2.4, 3.1]
    
    # Find the corresponding array Y
    Y = find_corresponding_array(X)
    
    # Print the result
    print("Input array:", X)
    print("Corresponding array:", Y)

if __name__ == "__main__":
    main()