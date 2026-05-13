n=int(input("enter the number of terms"))
first=0
second=1
for i in range(n+1):
    print(first)
    current=first+second
    first=second
    second=current