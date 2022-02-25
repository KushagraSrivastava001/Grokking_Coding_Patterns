import math
def smallest_subarray(arr,k):
    window_sum=0
    start=0
    min_length=math.inf
    
    for end in range(len(arr)):
        window_sum+=arr[end]
        while(window_sum>=k):
            min_length=min(min_length,end-start+1)
            window_sum-=arr[start]
            start+=1
    if(min_length==math.inf):
        return 0
    return min_length
        
print(smallest_subarray([4,5,2,3,2,4],3))
