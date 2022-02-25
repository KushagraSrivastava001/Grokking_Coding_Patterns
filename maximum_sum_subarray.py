#------------------------------------------------------------
#BruteForce Approach
def maximum_subarray(arr,k):
    maximum_sum=0
    for i in range(len(arr)-k+1):
        current_sum=0
        for i in range(i,i+k):
            current_sum+=arr[i]
        maximum_sum=max(maximum_sum,current_sum)
    return maximum_sum
print(maximum_subarray([4,5,6,3,2,4],3))

#--------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------

#Sliding Window Approach
def maximum_subarray(arr,k):
    maximum_sum=0
    start=0
    window_sum=0
    for end in range(len(arr)):
        window_sum+=arr[end]
        if end>=k-1:
            maximum_sum=max(maximum_sum,window_sum)
            window_sum-=arr[start]
            start+=1
    return maximum_sum
print(maximum_subarray([4,5,2,3,2,4],3))
