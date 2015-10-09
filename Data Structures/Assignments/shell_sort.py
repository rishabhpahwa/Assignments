def sort(a):
    gap=len(a)/2
    while gap>0:
        for i in range(gap,len(a),1):
            temp=a[i]
            j=i
            while j>=gap and a[j-gap]>temp:
                a[j]=a[j-gap]
                j-=gap
            a[j]=temp
        gap=gap/2
    return a
n=input("Enter the array to be sorted.\n")
res=sort(n)
print "The sorted array is:\n",res