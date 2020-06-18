'''
Input: an integer
Returns: an integer
'''
#https://kite.com/python/docs/itertools.combinations
from itertools import combinations
def eating_cookies(n):
    # Your code here
    for k in range(len(arr)):
        # combinations(range(4), 3) --> 012 013 023 123
    #   pool = tuple(n)
    #   m = len(pool)
    #   if r > m:
    #         return
    #         indices = range(r)
    #         yield tuple(pool[i] for i in indices)

    # all_combinations = []

        for i in range(len(n) + 1):
            #Add all combinations of `a_list` to `all_combinations`

            combinations_object = itertools.combinations(n, i)

            combinations_list = list(combinations_object)

            all_combinations += combinations_list

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
