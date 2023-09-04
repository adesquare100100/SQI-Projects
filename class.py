# print("WELCOME TO THE BIGGEST RESTAURANT OF ALL TIME")
# print("--------PLS PLACE YOUR ORDER-------")
# food = input("what food would you like to purchase: ").lower()
# protien = input("what protien do you want: ").lower()
# if food == "rice" and protien == "ponmo":
#     print("great! we will serve you rice and ponmo")
# else:
#     print("sorry we dont have what you order")
# =============================================================================================================

# collect and print(in a sentence, using fommated string) the following infomation from user. name, age and address.
# name = input("what is your name: ")
# age = input("what is your age: ")
# addy = input("what is your address: ")
# print(f"my name is {name} i am {age} years old and i live in {addy}")


# name = input("what is your name: ")
# age = input("what is your age: ")
# addy = input("what is your address: ")
# value1 = input("write your 1st value: ")
# value2 = input("write your 2nd value: ")
# result = int(value1) * int(value2)
# print(f"the result of the two values you enter is: {result}")
# ===========================================================================================================

# value1 = float(input("Enter the first value: "))
# value2 = float(input("Enter the second value: "))
# operation = input("which operation would you like to perform?: ")
# if operation == "addition":
#     result = value1 + value2
# elif operation == "subtraction":
#     result = value1 - value2
# elif operation == "multiplication":
#     result = value1 * value2
# elif operation == "division":
#     result = value1 / value2
# print("The result of operation is:", result)
 
# =============================================================================================================

'''
a friend of yours met you, on wednesday by 8am and ask if you will come to class,
respond to that friend with this condition
you will like to come to class only if the day is thursday and the time for class is 9am
'''

# day = input("enter day of the week: ").lower()
# time = input("enter time of the day: ").lower()
# if day == "thursday" and time == "9am":
#     print("YES! i will come to class")
# else:
#     print("NO! i wont be coming to class")
# ============================================================================================================

'''
ask user to write an article, then ask if user wants to replace any words, if yes, ask for the new words and 
replace it with the old word
'''

# article = input("what aticle would you like to write?: ")
# print("This your Article: ", article)
# user = input("would you like to replace a word in your article? YES/NO?: ").lower()
# if user == "yes":
#     oldWord = input("what is the old word you would like to change?: ")
#     newWord = input("what is the new world you would like to replace?: ")
#     NewArticle = article.replace(oldWord,newWord)
#     print("your Article had been replaced!", NewArticle)
# else:
#     print("no word to be changed!", article)


# # -------phone number-----
# mtn = ("0803", "0806", "0816", "0703", "0706","0813", "0816")
# glo = ("0805", "0807", "0811", "0815", "0705","0905")
# airtel = ("0802", "0808", "0812", "0902", "0907","0901")
# etisalat = ("0809", "0817", "0818", "0908", "0909")
# user = input("enter your phone number here: ")
# if user.startswith(mtn):
#     print("welcome to MTN")
# elif user.startswith(glo):
#     print("welcom to GLO")
# elif user.startswith(airtel):
#     print("welcom to AIRTEL")        
# elif user.startswith(etisalat):
#     print("welcom to etisalat")        
# else:
#     print("invalid number")    
# ==========================================================================================================

'''
Develop a programme that will ask user for the following information. Full name, Age, Address, Gender, Phone number
i want 5 users to attend to this, when the five of them are done, i want a list of zip information for each person
'''

# information = []
# Fullnames, ages, addys, genders, phones = [], [], [], [], []
# for i in range(2):
#     Fullname = input("E nter your full name: ")
#     age = input("What is your age?: ")
#     addy = input("Enter your address: ")
#     gender = input("What is your gender?: ")
#     phone = input("Enter your phone number: ")
#     Fullnames.append(Fullname),ages.append(age),addys.append(addy),genders.append(gender),phones.append(phone)

#     information = list(zip(Fullnames, ages, addys, genders, phones))
#     # information.append((Fullname, age, addy, gender, phone))
# print(information)
# ============================================================================================================


'''write a python program that will set 20 questions, set answers, ask user for answers.
mark the answers, if the user get a question, your program should be able
to score the user 10 marks, and for every question missed, the program should minus
5 marks from the user's original score. Give admission to the student who score 70% and above.
'''
# SOLUTION
# questions = ("what is your Fname?", "what is your Mname?", "what is your Lname?", "what is your age?", "what is your continent?", "what is your country?", "what is your state?", "what is your state capital?",  "what is your LGA?",  "what is your home town?")
# options = ("A. ade\n B. ola\n C. seun", "A. s\n B. ola\n C. seun", "A. square\n B. ola\n C. seun", "A. 18\n B. 19\n C. 20", "A. africa\n B. earth\n C. pluto", "A. nigeria\n B. usa\n C. uganda", "A. oyo\n B. dugbe\n C. lagos", "A. ibadan\n B. ado\n C. akure", "A. ISW\n B. kenya\n C. orbit", "A. dugbe\n B. ola\n C. seun"  )
# answers = ("A", "A", "A", "A", "A", "A", "A", "A", "A", "A")
# score = 0
# quesNum = 0
# for i in questions:
#     print(i)
#     print(options[quesNum])
#     guess = input("enter answer: ").upper()
#     if guess == answers[quesNum]:
#         score += 10
#         print("CORRECT!", score)
#     else:
#         score -= 5
#         print("WRONG!", score)
#     print(" ")
#     quesNum += 1
# print("Your total score is: ",score)
# if score >= 70:
#     print("CONGRATULATION!🤗 YOU HAVE BEEN GIVING ADMISSION TO STUDY PYTHON IN SQI🙂")
# else:
#     print("SORRY!🙄 BUT, YOU HAVE TO COME BACK NEXT YEAR😌")
# ===========================================================================================================

"""Write a python program that will ask user for their username and password, note, if the username and password is in 
the array of username and password, it should login, else invalid login details.
Furthermore, after login, your program should set theory questions,
ask user to provide answers, if user answer is the same as your answer, score the user and add 10 marks, else -5marks"""

# SOLUTION

# userName = ("ade", "ola", "seun")
# password = ("eda", "alo", "nues")
# user = input("Enter your username: ").lower()
# paswd = input("Enteer your password: ").lower()
# login = zip(userName, password)
# if (user,paswd) in login:
#     print("LOGIN SUCCESSFUL!")
#     print("")
#     print("Attempt the following Theory Questions")
#     print(" ")
#     questions = ("what is your name?", "what is your age?", "what is your state?")
#     answers = ("ade", "18", "ibadan")
#     score = 0
#     queNum = 0
#     for i in questions:
#         print(i)
#         ans = input("Enter your answer: ").lower()
#         if ans == answers[queNum]:
#             score += 10
#             print("CORRECT!", score)
#         else:
#             score -= 5
#             print("WRONG!", score)
#             print(" ")
#         queNum += 1 
# else:
#     print("INVALID LOGIN")
# print("YOUR AGGREGATE IS:", score)
# ====================================================================================================


'''
Write a python programme that will ask user to supply 3 sets data, when supplied,
user should be able to decide either to perform any of the following operations:
1. union, 2. Intersection, 3. issuperset, 4. issubset, 5. symmetric difference 6. isdisjoint
'''
# SOLUTION
# x = input("enter first set data (seperate each value with space): ").split()
# y = input("enter second set data (seperate each value with space): ").split()
# z = input("enter third set data (seperate each value with space): ").split()

# set1= set(x)
# set2= set(y)
# set3= set(z)
# print("Sets:", set1,set2,set3)

# operation = input("What operation would you like to perform? (union, Intersection, issuperset, issubset, symmetric difference, isdisjoint): ")

# if operation == "union":
#     result = set1.union(set2, set3)
# elif operation == "intersection":
#     result = set1.intersection(set2, set3)
# elif operation == "issuperset":
#     result = set1.issuperset(set2) and set1.issuperset(set3) 
# elif operation == "issubset":
#     result = set1.issubset(set2) and set1.issubset(set3)
# elif operation == "symmetric difference":
#     result = set1.symmetric_difference(set2, set3)   
# elif operation == "isdisjoint":
#     result = set1.isdisjoint(set2) and set1.isdisjoint(set3)
# else:
#     print("Invalid Operation")              
# print("Operation:", operation)
# print("Result:", result)
# =======================================================================================================


'''
create a programme that will do the following
ask users to register (registration info should include: name, age, address, course and gender), after registering,
generate a random matric number for your users, this matric number and their name should be saved in seperate lists.
Thereafter, print the name of the students, and their respective matric number.
NOTE, MATRIC NUMBER SHOULD BE ALPHANUMERIC CHARACTERS E.G. SQI202201, No matric number should be generated twice
'''
# SOLUTION

# user = []

# import random

# print("Enter your informations for registration")
# matric = ["sqi2000", "sqi3000", "sqi4000", "sqi5000", "sqi6000"]
# random.shuffle(matric)
# for i in range(4):
#     name = input("Enter your name here: ")
#     age =input("Enter your age here: ")
#     addy = input("Enter your addy here: ")
#     course = input("Enter your course here: ")
#     gender = input("Enter your gender here: ")
#     matricNumber = matric[i]
#     user.append((name,age,addy,course,gender,matricNumber))

# print(user)
# =======================================================================================================
    
'''
Create a simple program that will randomly generate numbers from a certain range to another range.
Print the name and number generated as zip array
'''
# SOLUTION
# import random
# user = []
# names, nums = [],[]
# for i in range(7):
#     name = input("Enter your name: ")
#     num = random.randrange(0, 10, 2)
#     names.append(name), nums.append(num)
#     user = list(zip(names, nums))
# print(user)
# ========================================================================================================

# NEXTED FOR LOOP

# for i in range(5):
#     name = input("enter your name: ")
#     print(name, "is picking a unique number")
#     for x in ("001", "002", "003", "004", "005"):
#         print(name, "picked", x)

# MULTIPLICATION TABLE FROM 1 TO 100 (NEXTED FOR LOOP)
# print("MULTIPLICATION TABLE")
# for i in range(1,101):
#     for x in range(1,101):
#         result = i * x
#         print(f"{i} * {x} = {result}")

# ==============================================================================================================


'''
write a python program that will set 10 questions, set answers, ask user for answers.
NOTE: questions should be generated randomly.
mark the answers, if the user get a question, your program should be able
to score the user 10 marks, and for every question missed, the program should minus
5 marks from the user's original score.
'''
# SOLUTION
# import random
# import time

# questions = ["what is your Fname?", "what is your Mname?", "what is your Lname?", "what is your age?", "what is your continent?", "what is your country?", "what is your state?", "what is your state capital?",  "what is your LGA?",  "what is your home town?"]
# options = ["A. ade\n B. ola\n C. seun", "A. s\n B. ola\n C. seun", "A. square\n B. ola\n C. seun", "A. 18\n B. 19\n C. 20", "A. africa\n B. earth\n C. pluto", "A. nigeria\n B. usa\n C. uganda", "A. oyo\n B. dugbe\n C. lagos", "A. ibadan\n B. ado\n C. akure", "A. ISW\n B. kenya\n C. orbit", "A. dugbe\n B. ola\n C. seun"  ]
# answers = ["A", "A", "A", "A", "A", "A", "A", "A", "A", "A"]

# qoa = list(zip(questions, options, answers))
# random.shuffle(qoa)

# score = 0 

# for x,y,z in qoa:
#     print(x)
#     time.sleep(1)
#     print(y)
#     time.sleep(1.5)
#     guess = input("enter answer: ").upper().strip()
#     time.sleep(2)
#     if guess == z:
#         score += 10
#         print("CORRECT!", score)
#     else:
#         score -= 5
#         print("WRONG!", score)
#     print(" ")
# print("Your total score is: ",score)
# ===========================================================================================================


# need to be corrected

# question = ["what is your name?", "what is a noun?"]
# answer = ["ade, ola, seun", "person, animal, place, thing"]
# z = list(zip(question,answer))
# for ques, ans in z:
#     print(ques)
#     guess = input("enter correct answer: ")
#     correctAns = set(ans)
#     userInput = set(guess)
#     if userInput.intersection(correctAns):
#         print("correct")
#     else:
#         print("wrong")
# ====================================================================================================

'''
develop a program that will ask user to enter his username, while the username is in your user database,
ask the user if they want to register, while the user answer is yes, register the user information else,
break and print user information.
'''

# information = []
# dataBase = ("ade", "ola", "oyin", "olu", "kola")
# user = input("Eenter your username: ")
# while user in dataBase:
#     suggest = input("would you like to register your information? yes or no: ")
#     while suggest == "yes":
#         name = input("Enter your name: ")
#         age = input("Enter your age: ")
#         addy = input("Enter your address: ")
#         course = input("Enter your course: ")
#         info = name, age, addy, course
#         information.append(info)
#         print("Your info has been registered")
#         suggest = input("would you like to register your information? yes or no: ")
#     else:
#         print(information)
# else:
#     print("Sorry! user not found")
# =========================================================================================================

'''
Write a program that allows the user to manage a phone book using a dictionary array.
Then implement functionalities to add contacts, search for contacts, and display the phonebook.
'''
# SOLUTION
# import time 
# phonebook = {"ade": "09025354555", "ola": "08025354555", "olu": "07025354555", "oyin": "08125354555"}

# def contacts():
#     print("--------PHONE BOOK-------")
#     print(phonebook)
#     time.sleep(1)
#     toADD = input("would you like to add new contact? yes or no: ")
#     if toADD == "yes":
#         add_()
#     else:
#         print("no new contact to add")
#     # toADD = input("would you like to add new contact? yes or no: ")
#     toSearch = input("would you like to search for a contact? yes or no: ")
#     if toSearch == "yes":   
#         search()
#     else:
#         print("nothing to search")
#     # toSearch = input("would you like to search for a contact? yes or no: ")
#     display()

# def add_():
#     print("YOU'RE ABOUT TO ENTER YOUR CONTACT INFORMATION TO ADD TO PHONEBOOK")
#     add = input("Enter 'stop' to quit or 'enter' to add new contact: ").lower()
#     while add != "stop":
#         name = input("Enter your contact name: ")
#         phone = input("Enter your contact phone number: ")
#         phonebook[name] = phone
#         print(f"{name}:{phone} has been added to phonebook")
#         # print (phonebook)
#         add = input("Enter 'stop' to quit or 'enter' to add new contact: ").lower()
#     else:
#         print("You have stopped adding contact")
    

# def search():
#     print("YOU'RE ABOUT TO ENTER YOUR CONTACT INFORMATION TO SEARCH IN PHONEBOOK")
#     add1 = input("Enter 'stop' to quit or 'enter' to add new contact: ").lower()
#     while add1 != "stop":
#         name = input("Enter contact name you like to search: ")
#         if name in phonebook:
#             print(f"{name}: {phonebook[name]}")
#         else:
#             print(f"{name} not found")
#         add1 = input("Enter 'stop' to quit or 'enter' to add new contact: ").lower()

# def display():
#     print("----PHONEBOOK----")
#     for name, phone in phonebook.items():
#         print(f"{name}:{phone}")
#     # print(phonebook)

# contacts()

# from datetime import datetime
# import random

# x = random.randint(1, 12), datetime.now().year + 4
# print (x)

# =================================================================================================================
# import re

# text ="""Company_Name
# Company_Address
# Date

# Employee_Name
# Employee_Address

# Dear Employee_Name ,

# We are pleased to offer you employment with Company_Name , We were impressed by your skills and qualifications, and we believe you will make a valuable contribution to our team.

# Your position will be Admin Manager, reporting to supervisor. Your initial annual salary will be $50,000.00 , payable on a last day of the month. You will also be eligible for the standard employee benefits package.

# Please review the attached employee handbook, which outlines our company policies and procedures. If you accept this offer, please sign and return a copy of this letter by Acceptance Deadline. You can contact HR for any questions or clarifications.

# We look forward to welcoming you to the Company_Name team. Your acceptance of this offer will signify your understanding and agreement to the terms outlined above.

# Sincerely,

# AdeSquare
# CEO"""
# tx = re.sub(r'Company_Name', 'ADE POS Terminal Institution',
#      re.sub(r'Company_Address', 'Dugbe,IBADAN', 
#      re.sub(r'Date', '10, Aug 2023',
#      re.sub(r'Employee_Name','Chidi Lish',
#      re.sub(r'Employee_Address','Lasgidi', text)))))
# print(tx)
# ==============================================================================================================================


# import re

# myFile = open ("C:\\Users\\Ade\\Desktop\\Employment_letter.txt", 'w')
# myFile.write("Company_Name\nCompany_Address\nDate\n \nEmployee_Name\nEmployee_Address\n \nDear Employee_Name , \nWe are pleased to offer you employment with Company_Name , We were impressed by your skills and qualifications, and we believe you will make a valuable contribution to our team.\nYour position will be Admin Manager, reporting to supervisor. Your initial annual salary will be $50,000.00 , payable on a last day of the month. You will also be eligible for the standard employee benefits package.\nPlease review the attached employee handbook, which outlines our company policies and procedures. If you accept this offer, please sign and return a copy of this letter by Acceptance Deadline. You can contact HR for any questions or clarifications.\nWe look forward to welcoming you to the Company_Name team. Your acceptance of this offer will signify your understanding and agreement to the terms outlined above.\nSincerely,\n \nAdeSquare\nCEO")
# myFile.close()

# with open("C:\\Users\\Ade\\Desktop\\Employment_letter.txt", 'r') as myFile:
#     # print(myFile.read())
#     text = myFile.read()
    
# text = re.sub(r'Company_Name', 'ADE POS Terminal Institution',
#        re.sub(r'Company_Address', 'Dugbe,IBADAN', 
#        re.sub(r'Date', '10, Aug 2023',
#        re.sub(r'Employee_Name','Chidi Lish',
#        re.sub(r'Employee_Address','Lasgidi', text)))))
# print(text)

# with open("C:\\Users\\Ade\\Desktop\\Employment_letter.txt", 'w') as myFile:
#     myFile.write(text)

