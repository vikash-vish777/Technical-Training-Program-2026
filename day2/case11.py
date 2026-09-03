#count negative and positive number in list
#i/p =[3,-2,7,-1,0,5,-4]
#o/p =positive: 4, Negative:3

def count_numbers(lst): #-------------o(1)
    positive_count = 0#--------------O(1)
    negative_count = 0#--------------O(1)
    
    for num in lst:#--------------O(n)
        if num >= 0:#------------O(1)
            positive_count += 1#--------------O(1)
        elif num < 0:#--------------O(1)
            negative_count += 1#--------------O(1)
            
    return positive_count, negative_count #--------------O(1)
lst=[3,9,-2,7,-1,0,5,-4]#--------------O(1)
positive, negative = count_numbers(lst) #--------------O(1)
print("Positive:", positive)#--------------O(1)
print("Negative:", negative)#--------------O(1)

#total time complexity = O(1)+O(n)= O(n)
