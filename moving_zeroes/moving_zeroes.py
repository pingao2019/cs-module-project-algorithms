'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    # for every number int the arr, if == 0. put to end
    for i in range(len(arr)):
        while i < len(arr):
            if arr[i]==0:
                arr[i]= arr[-1]
            else:
                return None

 


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")