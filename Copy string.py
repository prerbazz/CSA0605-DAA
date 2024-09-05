def copy_str(src,dest=" ",index=0):
    if index==len(src):
        return dest
    return copy_str(src,dest+src[index],index+1)
source=input("Enter a string to copy:")
copy=copy_str(source)
print("copied string:",copy)
