'''
A wall consists ofseveral rows ofbricks ofvarious integer lengths and uniform height.
Your goal is to find a vertical line going from the top to the bottom of the wall that
cuts through the fewest number of bricks. If the line goes through the edge between
two bricks, this does not count as a cut.
For example, suppose the input is as follows, where values in each row represent the
lengths of bricks in that row:
[[3, 5, 1 1 1],
[2, 3, 3, 2],
[5, 5],
[4, 4, 2],
[1, 3, 3, 3],
[1, 1, 6, 1, 1]]
the wall look like:
|   |     | | |
|  |   |  | | |
|      |      |
|    |     |  |
| |  |   |    |
| | |       | |
The best we can we do here is to draw a line after the eighth brick, which will only
require cutting through the bricks in the third and fifth row.
Given an input consisting of brick lengths for each row such as the one above, return
the fewest number ofbricks that must be cut to create a vertical line.

- first glance L testing each vertical line and see how many 
bricks it cuts through. If length of wall is m and there n total bricks,
this would take O(m x n) time.

- better strategy: instead of thinking how to minimize the cuts,
we can try to maximize the number of times a line can pass through
an edges between two bricks.
- We exammine each row and increment a counter in a hash table for the 
accumulated distance covered afted each brick, except the last one.
example after first row: {3: 1, 8: 1, 9: 1}
The key in the dictionary with the largest value represents the
vertical line with the fewest cuts. To find the actual number of bricks,
we can subtract this value from the toal number of rows

'''

from collections import defaultdict
def fewest_cuts(wall):
    cuts = defaultdict(int)  # Dictionary to count cuts at each position

    for row in wall:
        length = 0
        for brick in row[:-1]: # skip the last brick each row
            length += brick
            cuts[length] += 1

    return len(wall) - max(cuts.values())  # Find the maximum cuts at any position

def main():
    wall = [
        [3, 5, 1, 1],
        [2, 3, 3, 2],
        [5, 5],
        [4, 4, 2],
        [1, 3, 3, 3],
        [1, 1, 6, 1, 1]
    ]
    print(fewest_cuts(wall))  # Output: 2

if __name__ == "__main__":
    main()