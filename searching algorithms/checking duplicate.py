'''                                      Given an array of
                            numbers, give an algorithm for checking whether 
                            there are any duplicate elements in the array or no?
'''
def check_duplicate(arr):
    #to check duplicate we have to know if there is occurence of more than once for number
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]== arr[j]:
                print("Duplicate exists at :", arr[i])
                return
    print("No duplicate found")



'''                                      Can we improve the complexity of Problem-1 solution?
'''
def duplicate_improved(arr):
    arr.sort()  #sort list elements first
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]==arr[j]:
                print("Duplicate found at",arr[i])
                return
    print("No duplicate found")


'''                                      Is there any alternative way of solving Problem-1?
                                        Actuall Yes:
                                                   Hash table is best for this particular type of question
                                                   with an improved complexity.
'''

def bigOn_time_duplicate(arr):
    arr_searched={}
    for i in range(len(arr)):
        #checking if number is in dictiory there is three ways:
        #use dict.get(number,default_value), default value is value retured if key not found
        #use if value in dict: this check value if is key of dict
        #use also try except(KeyError) block to cash KeyError
        if arr_searched.get(arr[i],-1) >=0:
            print("Duplicate found at ",arr[i])
            return
        arr_searched[arr[i]]=i
    print("No duplicate was found")

'''                                      Main Function for testing all problem's solutions
'''
def main():
    arr = [3,5,9,1,2,3,9,9,10,20,32,1,2,3]
    print("Checking Duplicate Initial:")
    check_duplicate(arr)

    print("\nChecking duplicate with Sorting First :")
    duplicate_improved(arr)

    print("\nChecking duplicate with Hash table:")
    bigOn_time_duplicate(arr)

main()