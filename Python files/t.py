def binarySearch(arr, l, r, x): 
  
    while l <= r: 
  
        mid = l + (r - l)/2; 
          
        # Check if x is present at mid 
        if arr[mid] == x:
            c+=1
            return mid 
  
        # If x is greater, ignore left half 
        elif arr[mid] < x:
            c+=1
            l = mid + 1
  
        # If x is smaller, ignore right half 
        else:
            c+=1
            r = mid - 1
      
    # If we reach here, then the element was not present 
    return -1
  
  
# Test array 
arr = [ 3,6,7,9,15,20] 
x = 17
c=0
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    #print "Element is present at index %d" % result
    pass
else: 
    print ("Element is not present in array")
    print(c)
