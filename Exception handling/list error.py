a=[1,2,3,4]
b=int(input("enter the index to get value:"))
try:
    print(a[b])
except Exception as e:
    print("exception occured:",e)