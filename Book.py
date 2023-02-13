def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1
#The sample function
  #**********Main Program starts here**************

  #here the program is about how we can search a topic on a book 
class TimeMap(object):
#class defined on the books
    def __init__(self):
        self.book = collections.defaultbooks(list)
      #after defining we set the vlaue and timestamp on splitting the search
        

    def set(self, key, value, timestamp):
        self.book[key].append([timestamp, value])

    def get(self, key, timestamp):
        arr = self.book[key]
        n = len(arr)
        
        left = 0
        right = n
        #the binary search will search the value until the chapter is found
        while left < right:
            mid = (left + right) / 2
            if arr[mid][0] <= timestamp:
                left = mid + 1
            elif arr[mid][0] > timestamp:
                right = mid
        
        return "" if right == 0 else arr[right - 1][1]
        #basically it will output the right chapter after repeatedly splitting 
      
# Test array
arr = [ chapter 1, chapter 2, chapter 3, chapter 4, chapter 5, chapter 6, chapter 7, chapter 8, chapter 9, chapter 10 ]
x = chapter 3
 # Function call
result = binary_search(arr, 0, len(arr)-1, x)
 
if result != -1:
    print("Chapter is present at book", str(result))
else:
    print("Chapter is not present in book")
#output the chapter number and the name will be automatically shown to the user on their screen
