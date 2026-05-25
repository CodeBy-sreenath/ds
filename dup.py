def frequency(str):
    freq={}
    for ch in str:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
    return freq
s=input("enter a string")
print(frequency(s))            