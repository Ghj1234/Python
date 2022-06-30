#Join two sorted lists such that the final list is also sorted

def fsorted(a,b):
    i=j=0
    c=[]
    print(a)
    print(b)
    while i<len(a) and j<len(b):
        if a[i]<=b[j]:
            c.append(a[i])
            i+=1
            print("Start",i,j)
        elif a[i]>b[j]:
            c.append(b[j])
            j+=1
            print("Start",i,j)
        else:
            c.append(a[i])
            i=i+1
            c.append(b[j])
            j=j+1
            print("Start",i,j)
                

    return c+a[i:len(a)]+b[j:len(b)]

a=[int(num) for num in input("Enter 1st sorted list seperated by spaces: ").split()]
b=[int(num) for num in input("Enter 2nd sorted list seperated by spaces: ").split()]
print("Final sorted list is: ",fsorted(a,b))
