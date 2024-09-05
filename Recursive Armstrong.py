def armstrong(n,temp=None):
    if temp is None:
        temp=n
        num_dig=len(str(n))
    else:
        num_dig=len(str(temp))
    if n==0:
        return 0
    return (n%10)**num_dig+armstrong(int(n/10),temp)
no=153
if no==armstrong(no):
    print(no,"is an armstrong number")
else:
    print(no,"is not an armstrong number")
    
