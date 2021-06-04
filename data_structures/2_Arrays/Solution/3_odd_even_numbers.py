n=int(input("enter the number upto which you would like to get the odd numbers"))
odd_numbers=[]
for i in range(n//2+1):
    odd_numbers.append(2*i+1)
print("required odd numbers : ",odd_numbers)
