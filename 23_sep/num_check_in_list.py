#check if a number is present in a list if not print -1

list=[1,2,3,4,5]
n=int(input("Enter number to find="))
if n in list:
    print(n)
else:
    print(-1)