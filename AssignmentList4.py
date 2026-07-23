#1. Write a Python program to find the sum of all elements in the list [10, 20, 30,40, 50].
# list =[10, 20, 30,40, 50]
# sum=0
# for i in list:
#     sum+=i
# print(sum)

#2. Write a Python program to display the odd and even elements from the list [10,23, 11, 12, 33, 44, 2, 5, 6].

# list =[10,23, 11, 12, 33, 44, 2, 5, 6]
# for i in list:
#     if i%2==0:
#           print(i,"even number")
#     else:
#          print(i,"odd number")

  #3. Write a Python program to count the odd and even numbers in the list [10, 23,11, 12, 33, 44, 2, 5, 6].

# list =[10, 23,11, 12, 33, 44, 2, 5, 6]
# even=0
# odd=0

# for i in list:
#      if i%2==0:
#           even+=1
#      else:
#           odd+=1
# print("count of even=",even)
# print("count of odd=",odd)


#4. Write a Python program to interchange the first and last elements in the list [10,23, 11, 12, 33, 44, 2, 5, 6].
# list =[10,23, 11, 12, 33, 44, 2, 5, 6]
# temp=list[0]
# list[0]=list[-1]
# list[-1]=temp
# print(list)

#5. Write a Python program to duplicate all the items in the list li = [1, 2, 3],
#such that the result is:
#output = [1, 2, 3, 1, 2, 3, 1, 2, 3].
# li = [1, 2, 3]
# print (li+li+li)

#6. Find the smallest element in the list [10, 23, 11, 12, 33, 44, 2, 5,6].
list=[10, 23, 11, 12, 33, 44, 2, 5,6]
# using built-in method
# print(min(list))
# print(max(list))

#without built-in method
# small=list[0]
# large=list[0]

# for i in list:
#     if i<small:
#         small=i
#     if i>large:
#         large=i
# print("small number is =",small)
# print("large number is=",large)

#7. Find the greatest element in the list [89, 23, 24, 2, 55, 54, 64]
# list=[89, 23, 24, 2, 55, 54, 64]
# large=list[0]
# for i in list:
#     if i>large:
#         large=i
# print("greatest element is=",large)

# 8.remove the duplicate elements in the list but order should be same [1,2,3,4,56,1,22,23,33,23, 56]

# list=[1,2,3,4,56,1,22,23,33,23, 56]
# temp_list=[]
# for i in list:
#     if i in list and i not in temp_list:
#         temp_list.append(i)

# print("After removing duplicate element from given list list will be->",temp_list)


#9.Find the repetitive elements in the list [1,2,3,4,56,1,22,23,33,23, 56]

# list=[1,2,3,4,56,1,22,23,33,23, 56]
# temp_list=[]
# repeat_ele=[]

# for i in list:
#     if i in temp_list and i not in repeat_ele:
#         repeat_ele.append(i)
#     else:
#         temp_list.append(i)
# print("Repetitive element in given list ->",repeat_ele)

#9.Remove all the odd elements from the list [10, 23, 11,12,33,44,2,5, 6]
list=[10,23,11,12,33,44,2,5,6]
for i in list[:]:
    if i%2!=0:
        #print("odd",i)
    
        list.remove(i)

print("after removed odd element from list will be->",list)

    
        

      
  
    


        
    

    

        





