#1. Write a function to print your name and age.

# def info(name,age):
#    print(f"Name is:{name},Age is:{age}") 
# info("Rohit",27)
  
#2. Write a function that accepts two numbers and returns their sum.

# def add(num1,num2):
#       return num1+num2
# result=add(20,30)
# print("sum of num1 and num2 is:",result)

# 3. Write a function that takes a number and prints whether it is positive, negative, or zero.

# def pos_neg_zero(num):
#     if num>0:
#         print(num,"number is positive")
#     elif num<0:
#         print(num,"number is negative")
#     else:
#         print(num,"number is zero")
# pos_neg_zero(0)
    
# 4. Write a function to calculate the square of a given number.

# def square(num):
#     return num*num
# result=square(5)
# print("Square of given Number is:",result)

# 5. Write a function to print all even numbers between 1 and 50.

# def even_no():
#     for i in range(1,50):
#         if i%2==0:
#             print("Even B/W 1 to 50:",i)
# even_no()


# 6. Write a function that takes a number and prints its multiplication table.
# def multiplication_table(num):
#     for i in range(1,11):
#         print(f"{num}*{i}=",i*num)
# multiplication_table(5)

# 7. Write a function to check whether a number is divisible by 5 or not.
# def div(num):
#     if num%5==0:
#         print("Given Number completely divisible by 5")
#     else:
#         print("Given Number not completely divisible 5")
# div(27)

# 8. Write a function that takes two strings and concatenates them.
# def string_concat():
#     string1="Hello"
#     string2="World"
#     print("After Concatination of Both String->",string1 +" " +string2)
# string_concat()

# 9. Write a function to count how many times a word appears in a given sentence.
# def check_occurance():
#     sentence="The sun is bright, and the sun gives us light"
#     sentence=sentence.replace(",","").lower()

#     #spilt here
#     words=sentence.split()

#     # count word here
#     word_count={}

#     for word in words:
#         if word in word_count:
#             word_count[word]+=1
#         else:
#             word_count[word]=1
#         print(word_count)
     
# check_occurance()

#10. Write a function to return the length of a string without using the built-in len() function.

# def find_str_len():
#     string="this python programming"
#     count=0
#     for i in string:
#         count+=1
#     print(count)
     
# find_str_len()

#11. Write a function to count the number of vowels in a given string.
# def count_vowel():
#     string="this python programming"
#     count=0
#     for vowel in string.lower():
#         if vowel in "aeiou":
#              count+=1

#     print(count,"vowels in given string")
# count_vowel()  

# 12. Write a function to check whether a string starts with a vowel.
# def check_start_letter():
   
#    string="this python programming"
#    if string[0].lower() in "aeiou":
#       print("string start with vowels")
#    else:
#       print("string not start from vowel")
# check_start_letter()


#13. Write a function to remove all spaces from a given string.

# def remove_space():
#     string="this python programming"
#     for i in string:
#         if i==" ":
#             string=string.replace(i,"")
#             return string

#             #print("after remove all space from given string->",string)
# final_string=remove_space()
# print("after remove all space->",final_string)

#14. Write a function to replace all vowels in a string with *.

# def replace_vowel():

#    string="this python programming"
#    vowel="aeiouAEIOU"
#    for i in string:
#       if i in vowel:

#          print(i)
# replace_vowel()

#15. Write a function to count capital and small letters in a string.
# def count_letter():
#     string="this is python programming"
#     small = 0
#     capital = 0
#     for ch in string:
#        if ch.islower():
#         small += 1
#        elif ch.isupper():
#         capital += 1
#     print("Small letters:", small)
#     print("Capital letters:", capital)
# count_letter()


#16. Write a function to reverse a string passed by the user.
# def reverse_string(s):
#     return s[::-1]

# string = input("Enter a string: ")

# result = reverse_string(string)

# print("Reversed string:", result)

#17. Write a function to check if a string is a palindrome or not.

# def check_palindrome(string):
#     if string == string[::-1]:
#         return "Palindrome"
#     else:
#         return "Not Palindrome"


# string = input("Enter a string: ")

# print(check_palindrome(string))

#18. Write a function to count the number of words in a given sentence.

# def count_word():
#     count=0
#     string="this is python programming"
#     for i in string:
#         count+=1
#     print("total",count)
# count_word()

#19. Write a function to fi nd the most repeated character in a string.
# def repeat_character(string):
#     count = {}

#     for ch in string:
#         if ch != " ":
#             count[ch] = count.get(ch, 0) + 1

#     most_repeated = max(count, key=count.get)

#     return most_repeated


# string = input("Enter a string: ")

# print("Most repeated character:", repeat_character(string))

#20. Write a function to convert all lowercase letters to uppercase without using .upper().
# def convert_uppercase(string):
#     result = ""

#     for ch in string:
#         if 'a' <= ch <= 'z':
#             result += chr(ord(ch) - 32)
#         else:
#             result += ch

#     return result


# string = input("Enter a string: ")

# print("Uppercase:", convert_uppercase(string))












