def ispalindrome(r):
    return r==r[::-1]
s=int(input("enter a number"))
r=str(s)
ans=ispalindrome(r)
if ans:
    print("yes")
else:
    print("no")