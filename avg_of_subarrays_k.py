
#bruteforce approach
def avg_of_k(arr,k):
    result=[]
    for i in range(len(arr)-k+1):
        sum=0.0
        for i in range(i,i+k):
            sum=sum+arr[i]
            avg=sum/k
        result.append(avg)
    return result
print(avg_of_k([1,2,3,4,5,6],3))

#-----------------------------------------------------------------------------------------------------------------
#Sliding Window Technique


def avg_of_k(arr,k):
    result=[]
    window_sum=0.0
    window_start=0
    for wind_end in range(len(arr)):
        window_sum+=arr[wind_end]
        
        if(wind_end>=k-1):
            result.append(window_sum/k)
            window_sum-=arr[window_start]
            window_start+=1
    return result
print(avg_of_k([1,2,3,4,5,6,7],3))
