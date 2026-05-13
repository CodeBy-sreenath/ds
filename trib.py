n=int(input("enter the number of terms"))
first=0
second=1
third=1
for i in range(n+1):
    print(first)
    current=first+second+third
    first=second
    second=third
    third=current