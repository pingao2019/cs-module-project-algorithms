'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
import numpy as np

def sliding_window_max(nums, k):
    # Your code here
    # number of output =i-k +1
    outp=[]
    for i in range(len(arr)-1):
        newlist=arr[i:k-1]
        outp.append(max(newlist))
    return outp   
     



if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
