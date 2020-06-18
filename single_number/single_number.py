'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    #   every   element in arr is arranged from low value  to high value, try to find the same value from other in the arr.
    #choose element i.
    # if the element is not equal to another, continue to compare all another
    arr.sort()
    
    # while i <(len(arr)):
    #     if arr[i]!=arr[i+1]:
    #             return arr.pop(i)
    #         #  other wise return that number
    #         return arr[i]
    #     i +=2

    # return None
     
    s=set()
    for x in arr:
        if x in s:
            s.remove(x)
        else:
            s.add(x)

    return list(s)[0]

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")