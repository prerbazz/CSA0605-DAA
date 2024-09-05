def reverse(s,rev="",index=-1):
    if len(rev)==len(s):
        return rev
    return reverse(s,rev+s[index],index-1)
string=input("Enter the string to be reversed:")
print("Reversed string:",reverse(string))
