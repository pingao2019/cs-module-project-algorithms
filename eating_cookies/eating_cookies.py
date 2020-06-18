'''
Input: an integer
Returns: an integer
'''
#https://kite.com/python/docs/itertools.combinations
#import itertool



# Runtime: O(3^n)

# def eating_cookies(n):

#     if n < 0:

#         return 0

#     elif n == 0:

#         return 1

#     else:

#         return eating_cookies(n-3) + eating_cookies(n-2)+ eating_cookies(n-1)
# the cache allows us to save our work 

# cache is a dictionary where keys is the n, value is the answer 

# Runtime: O(n)

def eating_cookies(n, cache):

    if n < 0:

        return 0

    elif n == 0:

        return 1

    # check if the answer is in our cache 

    elif cache[n] > 0:

        return cache[n]

    else:

        # otherwise, our cache doesn't contain the answer, so we'll use our 

        # recursive logic to calculate it, and then save the answer in our 

        # cache for future uses 

        cache[n] = eating_cookies(n-3, cache) + eating_cookies(n-2, cache)+ eating_cookies(n-1, cache) 

    return cache[n]
​if __name__ == "__main__":

    # Use the main function here to test out your implementation

    num_cookies = 100

    cache = {i: 0 for i in range(num_cookies+1)}

    print(f"There are {eating_cookies(num_cookies, cache)} ways for Cookie Monster to each {num_cookies} cookies")



# def eating_cookies(n):
#     # Your code here
#     if n< 0:
#         return 0
#     elif n==0:
#         return 1
#     else: 
#         return eating_cookies(n-3)+ eating_cookies(n-2)+eating_cookies(n-1)


    # for k in range(len(arr)):
    #     # combinations(range(4), 3) --> 012 013 023 123
    # #   pool = tuple(n)
    # #   m = len(pool)
    # #   if r > m:
    # #         return
    # #         indices = range(r)
    # #         yield tuple(pool[i] for i in indices)

    # # all_combinations = []

    #     for i in range(len(n) + 1):
    #         #Add all combinations of `a_list` to `all_combinations`

    #         combinations_object = itertools.combinations(n, i)

    #         combinations_list = list(combinations_object)

    #         all_combinations += combinations_list




# if __name__ == "__main__":
#     # Use the main function here to test out your implementation
#     num_cookies = 5

#     print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
