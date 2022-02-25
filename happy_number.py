
#fast and slow pointer example
def happy_number(num):
    slow=fast=num
    while True:
        slow=sum_of_digits(slow)
        fast=sum_of_digits(sum_of_digits(slow))
        if slow==fast:
            break
    return slow==1
def sum_of_digits(n):
    sum1=0
    while n>0:
        digits=n%10
        sum1 += (digits)*(digits)
        n=n//10
    return sum1
print(happy_number(19))
