# In this Assignment I work on all stirng manipulations logics

#1. Filter vowels and consonants from the string "How are you sir".
 
# string= "How are you sir"
# for i in string:
#     if i in "aeiouAEIOU":
#         print(i,"is vowel")
#     else:
#         print(i,"is consonent")

#2. Count vowels and consonants in the string "How are you sir". 

# st1 ="How are you sir"
# v_count=0
# c_count=0
# for i in st1:
#     if i in " ":
#         continue
#     if i in "aeiouAEIOU":
#         v_count+=1
#     else:
#         c_count+=1

# print("vowels:",v_count) 
# print("consonants:",c_count)

#3. Reverse the string "How are you sir". 
# st1 ="How are you sir"
# for i in range(len(st1)-1,-1,-1):
#     print(st1[i],end="")


#4. Convert lowercase letters to uppercase in the string "How are you sir". 

# string ="How are you sir"
# temp=(string.upper())
# print(temp)

#5.Remove duplicate letters from the string "this is python programming place".

# string ="this is python programming place" 
# tempstr=""

# for i in string:
#     if i in string and i not  in  tempstr:
#         tempstr+=i
#         print(i,end=" ")



#6. Search for a specific character in the string "this is python programming place".

# string ="this is python programming place"
# if 'r' in string:
#     print("found")
# else:
#     print("not found")

#7. Find the greatest and smallest characters from the string "venugopaliyer".

# string = "venugopaliyer"

# greatest=string[0]
# smallest=string[0]

# for ch in string:
#     if ch > greatest:
#         greatest = ch
#     if ch<smallest:
#             smallest=ch

# print(greatest,"is greatest character")
# print(smallest,"is smallest character")


#8.Count the total occurrences of all letter in the string "this is python programming place".

# string ="this is python programming place"
# counter=0
# for i in string:
#     counter+=1
# print(counter)

#9.Count the total occurrences of specific letter in the string "this is python programming place".
# string ="this is python programming place"
# counter=0
# for i in string:
#     if i=='t':
#         counter+=1
# print(counter)

# 10.Replace with method "python" with "javascript" in the string "python developer python engineer python holder".
# string ="python developer python engineer python holder"
# newstr=string.replace("python","javascript")
# print(newstr,end=" ")

# 11.Replace without method "python" with "javascript" in the string "python developer python engineer python holder".
# string ="python developer python engineer python holder"
# result = ""
# i = 0
# while i < len(string):
 
 
#  if string[i:i+6] == "python":
#         result = result + "javascript"
#         i = i + 6
#  else:
#         result = result + string[i]
#         i = i + 1

# print(result)

#12. Print alternate letters from the string "How are you sir".

# string ="How are you sir"
# for i in range(0,len(string),2):
#     print(string[i],end=" ")

#13. Print alternate letters using while-loop from the string "How are you sir".
# string = "How are you sir"
# i = 0

# while i < len(string):
#     print(string[i], end=" ")
#     i = i + 2

#14. Convert the string "qwertyuiopasdfghjklzxcvbnm"to" "abcdefghijklmnopqrstuvwxyz.

# string ="qwertyuiopasdfghjklzxcvbnm"
# # phle string ko list mein convert kya kyonki string immutable hoti hai usme koi bhi changes nahi kr skte the
# # list ko hum index basis par swap kr skte hai
# string = list("qwertyuiopasdfghjklzxcvbnm")

# for i in range(len(string)):
#     for j in range(i + 1, len(string)):
#         if string[i] > string[j]:
#             string[i], string[j] = string[j], string[i]
# # yaha par list ko wapas string mein convert kiya gya using .join()method.
# print("".join(string))

#15. Check if the string is a palindrome (e.g., "madam" → Palindrome, "hello" → Not palindrome).
# string ="madam"  # eg."naman,kanak,madam,mam,pap"
# rev=""
# for i in range(len(string)-1,-1,-1):
#     rev=rev+string[i]
# if string==rev:
#     print(rev,"is palindrome string")
# else:
#     print(rev,"is not palindrome string")

#16. Count spaces, digits, alphabets, and special characters in "Python 3.9 is awesome!!".

# string="Python 3.9 is awesome!!"
# space_count=0
# digit_count=0
# special_char=0
# alphabet_count=0
# for i in string:
#     if i==" ":
#         space_count+=1
#     elif i>='0' and i<='9':
#         digit_count+=1
#     elif not((i>='a'and i<='z') or (i>='A' and i<='z' )):
#         special_char+=1
#     elif ((i>='a' and i<='z') or(i>='A' and i<='Z')):
#         alphabet_count+=1
# print("counting of spaces is=",space_count)
# print("counting of digit is=",digit_count)
# print("counting of special character is=",special_char)
# print("Total number of alphabet in given string is=",alphabet_count)


#17. Find the longest word in the string "Python programming is interesting".
# string = "Python programming is interesting"
# word = ""
# longest = ""
# for ch in string:

#     if ch != " ":
#         word += ch
#     else:
#         if len(word) > len(longest):
#             longest = word
#         word = ""

# # Last word check
# if len(word) > len(longest):
#     longest = word

# print("Longest Word is =", longest)

#18. Capitalize the first letter of each word in "welcome to python world".
# using title()-> is used to capitalize first letter of every word in given string and have no argument.
# string="welcome to python world"
# new_str=string.title()
# print(new_str)

#18. Capitalize the first letter of each word in "welcome to python world"
# without title()
# string = "welcome to python"
# words = string.split()
# result = ""

# for word in words:
#     result += word[0].upper() + word[1:] + " "

# print(result.strip())

#19. Remove all spaces from "How are you sir".
# using replace()
# string="How are you sir"
# new_str=string.replace(" ","")
# print(new_str)

#20. Remove all spaces from "How are you sir".
# without using replace()

# string="How are you sir"
# result=""

# for i in string:
#     if i !=" ":
#         result+=i
# print(result)

#21. Check if all characters in the string are unique (e.g., "abcde" → True, "hello" → False).

# string="hello"
# temp=""
# flag =True
# for i in string:
#     if i in temp:
#         flag=False
#         break
#     temp+=i
# print(flag)

# 22. Sort characters alphabetically in "programming" → "aggimmnoprr".
# by using sorted()-> sort in alphabatically order

# string="programming"
# new_str="".join(sorted(string))
# print(new_str)

# 22. Sort characters alphabetically in "programming" → "aggimmnoprr".
# without sorted()
# string="programming" 
# list_str=list(string)

# for i in range(len(list_str)):
#     for j in range(i+1,len(list_str)):
#         if list_str[i]>list_str[j]:
#             list_str[i],list_str[j]=list_str[j],list_str[i]

# result=""

# for i in list_str:
#     result+=i

# print("Sorted given string in alphabatically order is->",result)

  
#23. Swap cases of all letters in "Python Is Fun" → "pYTHON iS fUN".
# By Using swapcase() method

# string= "Python Is Fun"
# new_str=string.swapcase()
# print(new_str)

#O/P->pYTHON iS fUN

#23.Swap cases of all letters in "Python Is Fun" → "pYTHON iS fUN".
# without Using swapcase() method

# string= "Python Is Fun"
# str1="" 
# for i in string:
#      if i.islower():
#         str1+=i.upper()
#      elif i.isupper():
#         str1+=i.lower()
#      else:
#         str1+=i
# print(str1) 


# 24. Find frequency of each character in "banana" → { 'b':1, 'a':3, 'n':2 }.    

# string="banana" 
# temp={}

# for i in string:
#     if i in temp:
#         temp[i]+=1
#     else:
#         temp[i]=1
# print(temp)

# 24. Find frequency of each character in "banana" → { 'b':1, 'a':3, 'n':2 }. 
# string = "banana"

# for ch in set(string):
#     print(ch, ":", string.count(ch))


#25. Remove vowels from "How are you sir" → "Hw r y sr".
# string="How are you sir"
# vowel="aeiouAEIOU"
# temp=""
# for i in string:
#     if i not in vowel:
#         temp+=i
# print(temp)

# 26. Check if a substring exists in "Python programming" (e.g., "thon" → Found).
# string="Python programming"
# sub="thon"

# if sub  in string:
#     print(sub,":->substring exist in original string")
# else:
#     print(sub,":->substring not exist in original string")

# using find method  26 check substring
# string="Python programming"
# sub="thon"

# if  string.find(sub)!=-1:
#     print(sub,":->substring exist in original string")
# else:
#     print(sub,":->substring not exist in original string")


#27. Print every character in reverse order in "How are you sir" → "ris uoy era woH".

# string="How are you sir"
# reverse_str=""
# for i in string:
#     reverse_str=i+reverse_str
# print(reverse_str)
        
# using slicing

# string="How are you sir"
# reverse_str=""
# reverse_str=string[::-1]
# print(reverse_str)

#using join() and reversed() method

# string="How are you sir"
# print("after reversed character of this string->","".join(reversed(string)))

#27. Print words in reverse order in "How are you sir" → "sir you are How".

# string="How are you sir"
# words=string.split()
# for i in range(len(words)-1,-1,-1):
#     print(words[i],end=" ")

#Using split() and slicing(),join() method
# string="How are you sir"
# words=string.split()
# print("".join(words[::-1]),end=" ")



#28. Count words in the string "This is a python assignment".

# string="This is a python assignment"
# count=0
# for i in string:
#     count+=1
# print(count)


#29. Find the ASCII value of each character in "ABcd".
# char="ABcd"
# for i in char:
#     print(i,"=",ord(i))

#30. Convert a string into a list of words using "split()" (e.g., "Python is fun" → ["Python", "is", "fun"]).
# string= "Python is fun" 
# lst=string.split() # split() method by default seprates the string at spaces.It return a list by default
# print(lst)

#31. Join a list of words into a string using "join()" (e.g., ["Python", "is", "fun"] → "Python is fun").

# lst=["Python", "is", "fun"]
# new_str=" ".join(lst)
# print(new_str)
 
#32. Find the first non-repeating character in "swiss" → "w".
# string="swiss" 
# for i in string:
#     if string.count(i)==1:
#         print("first non-repeating character is:",i)
#         break
  
#33. Check if two strings are anagrams (e.g., "listen" and "silent" → Anagrams).
# string1="listen"
# string2="silent"
# if sorted(string1)==sorted(string2):
#     print("both strings are anagram")
# else:
#     print("both string are not anagram")

#Without sorted() method
# string1="listen"
# string2="silent"

# if len(string1)!=len(string2): # check length both string
#     print("not anagram string")
# else:
#     flag=True
#     for i in string1:
#         if string1.count(i)!=string2.count(i): # check count of every character in both character
#             flag=False                         # agr kisi bhi character ki count alag ho to not anagram
#             break                              # agr count same hai to anagram
#     if flag:
#         print("Both string anagram")
#     else:
#         print("not anagram")

#34. Replace all spaces with hyphens (-) in "Python is easy to learn" → "Python-is-easy-to-learn".

string="Python is easy to learn"
for i in string:
    if i==" ":
        temp=string.replace(i,"-")
print(temp)


            
        
        