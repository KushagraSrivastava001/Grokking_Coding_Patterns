import math
def k_distinct_elements(arr):
    fruit_frequency={}
    start=0
    max_length=0
    for end in range(len(arr)):
        right_char=arr[end]
        if right_char not in fruit_frequency:
            fruit_frequency[right_char]=1
        else:
            fruit_frequency[right_char]+=1
        while len(fruit_frequency)>2:
            left=fruit_frequency[start]
            fruit_frequency[left]-=1
            if fruit_frequency[left]==0:
                del fruit_frequency[left]
            start+=1
        max_length=max(max_length,end-start+1)
    return max_length
print(k_distinct_elements(['A','B','A','C','C','B']))
