import math
def k_distinct_elements(string):
    char_freq={}
    start=0
    max_length=0
    for end in range(len(string)):
        right_char=string[end]
        if right_char in char_freq:
            start=max(start,char_freq[right_char]+1)
        char_freq[right_char]=end
    return max(max_length,end-start+1)
print(k_distinct_elements("aababcd"))
