# '''
# Create a database for SQI if the student age is above 18 the student should be able to register but if the student
# is below tell the student we can’t take them, also create a table for course
# (data science, data analysis, graphic design, web design , Java script ) the course I’m registering should go to
# the respective course above
# '''
# # SOLUTION

# import mysql.connector as connection
# import random

# conn = connection.connect(host="127.0.0.1", user="root", password = "Database001@", database="db")
# cursor = conn.cursor()

# print("WELCOME TO SQI")

# class information:
#     def __init__(self):
#         self.age = input("enter your age: ")
#         if self.age >= "18":
#             self.id = random.randint(100, 106) 
#             self.fname =input("enter your first name: ")
#             self.lname =input("enter your last name: ")
#             self.gender =input("enter your gender: ")
#             self.addy =input("enter your address: ")
#             self.phone =input("enter your phone number: ")
#             self.course = input("enter your course: ")
#             self.val = (self.id, self.fname, self.lname, self.gender, self.addy, self.phone, self.course)
#             self.general()
#         else:
#             print("we cant register you to SQI, you're too young")
        
#     def general(self):
#         if self.course == "data science":
#             self.data_science()
#         elif self.course == "data analysis":
#             self.data_analysis()
#         elif self.course == "graphic design":
#             self.graphic_design()
#         elif self.course == "web":
#             self.web()
#         elif self.course == "java":
#             self.java()
#         else:
#             print("course not available!")
            
#     def data_science(self):
#         query = "INSERT INTO data_science(id,fname, lname, gender, addy, phone, course) VALUES (%s, %s, %s, %s, %s, %s, %s)"
#         cursor.execute(query, self.val)
#         conn.commit()
#         print("Registration successful")
#         cursor.close()
        
#     def data_analysis(self):
#         query = "INSERT INTO data_analysis(id,fname, lname, gender, addy, phone, course) VALUES (%s, %s, %s, %s, %s, %s, %s)"
#         cursor.execute(query, self.val)
#         conn.commit()
#         print("Registration successful")
#         cursor.close()
        
#     def graphic_design(self):
#         query = "INSERT INTO graphic_design(id,fname, lname, gender, addy, phone, course) VALUES (%s, %s, %s, %s, %s, %s, %s)"
#         cursor.execute(query, self.val)
#         conn.commit()
#         print("Registration successful")
#         cursor.close()
        
#     def web(self):
#         query = "INSERT INTO web(id,fname, lname, gender, addy, phone, course) VALUES (%s, %s, %s, %s, %s, %s, %s)"
#         cursor.execute(query, self.val)
#         conn.commit()
#         print("Registration successful")
#         cursor.close()
        
#     def java(self):
#         query = "INSERT INTO java(id,fname,lname,gender,phone,addy, course) VALUES (%s, %s, %s, %s, %s, %s, %s)"
#         cursor.execute(query, self.val)
#         conn.commit()
#         print("Registration successful")
#         cursor.close()
        
# info = information()


# =================== Mini Project =================================================================================

# import mysql.connector as connection
# import random
# from datetime import datetime

# conn = connection.connect(host="127.0.0.1", user="root", password = "Database001@", database="bank")
# cursor = conn.cursor()


# class Bank:
#     def __init__(self):
#         self.run()

#     def run(self):
#         print("------WELCOME TO ADE POS TERMINAL------")
#         print("What transaction would you like to perform?")
#         print("1. Register an account")
#         print("2. Make a withdrawal")
#         choice = input("Enter your choice (1/2): ")

#         if choice == "1":
#             self.register_account()     
#         elif choice == "2":
#             self.withdrawal()
#         else:
#             print("Invalid OPTION")

#     def generate_atm(self):
#         self.cardNum = random.randint(5399000000000000, 9999999999999999)
#         self.cvv = random.randint(200, 999)
#         self.exp = (datetime.now().month, datetime.now().year + 4)
#         self.atm_pin = input("Enter a four-digit PIN for your ATM card: ")
#         self.acc_balance = random.randint(10000, 20000)
#         print("You have successfully registered an account.")
#         print("Here is your ATM CARD details:")
#         print(f"Card Number: {self.cardNum}\nCVV: {self.cvv}\nExpiry Date: {self.exp[0]}/{self.exp[1]}\nATM PIN: {self.atm_pin}\nBalance: {self.acc_balance}")

#     def register_account(self):
#         user = input("Would you like to set up an account? (yes/no): ")
#         if user.lower() == "yes":
#             print("Select a bank to register with:")
#             print("1. Bank A\n2. Bank B\n3. Bank C\n")
#             choice = input("Enter your bank choice (1-3): ")
#             if choice in ("1", "2", "3"):
#                 self.registration()
#             else:
#                 print("Invalid entry")
#         else:
#             print("Only registered customers can use the terminal")

#     def registration(self):
#         self.id = random.randint(100, 999)
#         self.fname = input("Enter your first name: ")
#         self.lname = input("Enter your last name: ")
#         self.addy = input("Enter your address: ")
#         self.age = input("Enter your age: ")
#         self.gender = input("Enter your gender: ")
#         self.phone = input("Enter your phone number: ")
#         self.generate_atm()
        
#         reg_info = (self.id, self.fname, self.lname, self.addy, self.age, self.gender, self.phone, self.acc_balance)
#         customers_query = "INSERT INTO customers (id, fname, lname, addy, age, gender, phone, acc_balance) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
#         cursor.execute(customers_query, reg_info)
#         conn.commit()

#         # id = self.cursor.lastrowid
#         atm_query = "INSERT INTO atm_cards (cardNum, cvv, exp_month, exp_year, atm_pin, id) VALUES ( %s, %s, %s, %s, %s, %s)"
#         atm_card_details = (self.cardNum, self.cvv, self.exp[0], self.exp[1], self.atm_pin, self.id)
#         cursor.execute(atm_query, atm_card_details)
#         conn.commit()
#         print("Account registration Completed.")

#     def withdrawal(self):
#         print("Enter your ATM card information for withdrawal:")
#         card_number = int(input("Enter your ATM CARD 16 digit: "))
#         querry = "SELECT * FROM atm_cards WHERE cardNum =%s"
#         val = (card_number, )
#         cursor.execute(querry, val)
#         results = cursor.fetchone()
#         if results:
#             print(results)
#             card_cvv = int(input("Enter your ATM CARD CVV: "))
#             card_expiry_month = input("Enter your ATM CARD expiry month: ")  
#             card_expiry_year = input("Enter your ATM CARD expiry year: ")
#             card_pin = int(input("Enter your ATM CARD PIN: "))
#         else:
#             print("Invalid ATM CARD number")
        
#         if card_cvv == results[1] and card_expiry_month == results[2] and card_expiry_year == results[3] and card_pin == results[4]:
#             query = "SELECT * FROM customers WHERE id =%s"
#             val2 = (results[5], )
#             cursor.execute(query, val2)
#             result2 =  cursor.fetchone()
#             print(result2)
#             amount = int(input("Enter the amount you want to withdraw: "))
#             if result2[7] > amount:
#                 new_amount = result2[7] - amount
#                 query3 = "UPDATE customers SET acc_balance = %s where id = %s" 
#                 val3 = (new_amount, results[5])
#                 cursor.execute(query3, val3)
#                 conn.commit()
#                 print("Withdrawal Successful")
#             else:
#                 print("Insufficent Balance")
                
# bnk = Bank()


# ==============================================================================================================================
# '''
# # -----------------PROJECT----------------

# Develop a program for SQI Electoral Body
# Voters registration should be by Department
# 1. Datascience
# 2. Data Analysis
# 3. Web Development
# 4. Javascript
# 5. Graphic Design
# 6. UI/UX
# 7. Cyber security
# ** At least 10 electorate from each of these departments must register
# ** There should be 2 candidates vying for the post of the president, and 2 for the post of the General Secretary
# ** On election day, electorate should be able to vote based on their Departments, when they vote, these votes should be counting for the candidate of their choice.
# At the end of the voting, there should be a total count for each of the aspirants and winner must be declared immediately
# '''




# # SOLUTION

# Import the required MySQL connector library and  Establish a connection to the MySQL server

# import mysql.connector as connection
# conn = connection.connect(host="127.0.0.1", user="root", password = "Database001@", database="sqi_electoral")
# cursor = conn.cursor()


# class sqi_Election:
#     def __init__(self):
#         self.president_voters = set()                   #-----------------------------------------------------This store voted president_voters
#         self.gen_sec_voters = set()                   #-----------------------------------------------------This store voted gen_sec_voters
        
#     def menu(self):
#         while True:
#             print("----------WELCOME TO SQI ELECTION----------")
#             print("Please choose an option:")
#             print("1. Registration")
#             print("2. Cast your vote")
#             print("3. Check winner")
#             print("4. Quit the election process")
#             choice = input("Enter the number of your choice(1/4): ")
#             if choice == '1':
#                 self.handle_reg()
#             elif choice == '2':
#                 self.Elections("president", "gen_sec")
#             elif choice == '3':
#                 self.calculateWinner()
#             elif choice == '4':
#                 print("Thank you for using SQI Election.")
#                 break
#             else:
#                 print("Invalid choice. please choose a valid option")

       
#     def handle_reg(self):
#         print("Kindly tell us your Department to begin with the Election process")
#         print("A. data science\nB. data analysis\nC. web development\nD. java script\nE. graphic design\nF. ui/ux\nG. cyber security")
#         choice = input("Enter (A / G) to choose your department: ").upper()
#         if choice == "A":
#             self.dataScience()
#         elif choice == "B":
#             self.dataAnalyst()
#         elif choice == "C":
#             self.webDeveloper()
#         elif choice == "D":
#             self.javaScript()
#         elif choice == "E":
#             self.graphicDesign()
#         elif choice == "F":
#             self.UiUx()
#         elif choice == "G":
#             self.cyberSecurity()
            
#         else:
#             print("Sorry! Your Department is not allowed to perform the Election process")
#             self.__init__()
            
            
#     def dataScience(self):                          #---------------------- Define election functions for each department
#         for i in range(2):
#             print(" ")
#             self.registration()
#             dept_id = 1
#             query = "UPDATE departments SET reg_votes = reg_votes + 1 WHERE dept_id = %s"
#             val = (dept_id,) 
#             cursor.execute(query, val)
#             conn.commit()
            
#     def dataAnalyst(self):
#         for i in range(2):
#             print(" ")
#             self.registration()
#             dept_id = 2
#             query = "UPDATE departments SET reg_votes = reg_votes + 1 WHERE dept_id = %s"
#             val = (dept_id,) 
#             cursor.execute(query, val)
#             conn.commit()
            
#     def webDeveloper(self):
#         for i in range(2):
#             print(" ")
#             self.registration()
#             dept_id = 3
#             query = "UPDATE departments SET reg_votes = reg_votes + 1 WHERE dept_id = %s"
#             val = (dept_id,) 
#             cursor.execute(query, val)
#             conn.commit()
            
#     def javaScript(self):
#         for i in range(2):
#             print(" ")
#             self.registration()
#             dept_id = 4
#             query = "UPDATE departments SET reg_votes = reg_votes + 1 WHERE dept_id = %s"
#             val = (dept_id,) 
#             cursor.execute(query, val)
#             conn.commit()
            
#     def graphicDesign(self):
#         for i in range(2):
#             print(" ")
#             self.registration()
#             dept_id = 5
#             query = "UPDATE departments SET reg_votes = reg_votes + 1 WHERE dept_id = %s"
#             val = (dept_id,) 
#             cursor.execute(query, val)
#             conn.commit()
            
#     def UiUx(self):
#         for i in range(2):
#             print(" ")
#             self.registration()
#             dept_id = 6
#             query = "UPDATE departments SET reg_votes = reg_votes + 1 WHERE dept_id = %s"
#             val = (dept_id,) 
#             cursor.execute(query, val)
#             conn.commit()
            
#     def cyberSecurity(self):
#         for i in range(2):
#             print(" ")
#             self.registration()
#             dept_id = 7
#             query = "UPDATE departments SET reg_votes = reg_votes + 1 WHERE dept_id = %s"
#             val = (dept_id,) 
#             cursor.execute(query, val)
#             conn.commit()
            
         
#     def registration(self):                     #----------------------------------------------Define the voter registration process
#         print("-----Welcome To The Registration Portal------")
#         self.Fname = input("Enter your first name: ")
#         self.Lname = input("Enter your last name: ")
#         self.Department = input("Enter your Department: ")
        
#         query = "INSERT INTO voters (Fname, Lname, department) VALUES (%s, %s, %s)"     #------- Insert voter details into the 'voters' table
#         values = (self.Fname, self.Lname, self.Department,)
#         cursor.execute(query, values)
#         conn.commit()
#         print("Registration completed.")        


            
#     def Elections(self, president, gen_sec):                  #------------ Define the election process for both President and General Secretary
#         print("----------President Election----------")
#         for i in range(1):
#             self.vote(president)
            
#         print("----------General Secretary Election----------")
#         for i in range(1):
#             self.vote(gen_sec)
            
#         # self.calculateWinner()
        
    
    
#     def vote(self, position):                     # --------------------------Define the voting process for a given position
#         print(f"-----Welcome To The {position} Voting Portal------")
#         self.Fname = input("Enter your first name: ")
#         self.Lname = input("Enter your last name: ")
#         self.Department = input("Enter your Department: ")
        
#         #check if voter is registered
#         query = "SELECT * FROM voters WHERE Fname = %s AND Lname = %s"
#         values = (self.Fname, self.Lname)
#         cursor.execute(query, values)
#         voter = cursor.fetchone()
#         print(voter)
        
#         # Check if voter has already voted
#         if voter:
#             if position == "president" and (self.Fname, self.Lname) in self.president_voters:
#                 print("You have already cast your vote for president.")
#             elif position == "gen_sec" and (self.Fname, self.Lname) in self.gen_sec_voters:
#                 print("You have already cast your vote for general secretary.")
#             else:
#                 if position == "president":
#                     self.president_voters.add((self.Fname, self.Lname))              #--------------------------Add voter to voted set
#                 elif position == "gen_sec":
#                     self.gen_sec_voters.add((self.Fname, self.Lname)) 
                
#                 valid_departments = ["data science", "data analysis", "web development", "java script", "graphic design", "ui/ux", "cyber security"]
#                 if self.Department.lower() in valid_departments:
#                     candidate = input(f"Choose {position} candidate (candidate A / candidate B): ")
#                     if candidate.lower() == "candidate a" or candidate.lower() == "candidate b":
#                         query = f"UPDATE candidates SET {position}_votes = {position}_votes + 1 WHERE department = %s AND candidate_name = %s"
#                         values = (self.Department, candidate)
#                         cursor.execute(query, values)
#                         conn.commit()
#                         print("Vote cast successfully!")
#                     else:
#                         print("Invalid candidate choice.")
#                 else:
#                     print("Invalid department for voting.")
#         else:
#             print("you are not a registered voter or your details are incorrect.")
#             self.vote(position)
        

#         # ------------------------------------------------------- Define the winner calculation process
#         # ---------------------------------------------(ORDER)Ordering results in (DESC)decending order and (LIMIT 1)fetch the top result(highest num of votes)
 
#     def calculateWinner(self):                 
#         print("----------Calculating Winner----------")
#         query1 = f"SELECT candidate_name, SUM(president_votes) AS total_votes FROM candidates GROUP BY candidate_name ORDER BY total_votes DESC LIMIT 1"  
#         cursor.execute(query1)
#         winner1 = cursor.fetchone()
        
#         query2 = f"SELECT candidate_name, SUM(gen_sec_votes) AS total_votes FROM candidates GROUP BY candidate_name ORDER BY total_votes DESC LIMIT 1"
#         cursor.execute(query2)
#         winner2 = cursor.fetchone()
        
#         if winner1:
#             print(f"The winner for President is {winner1[0]} with {winner1[1]} total votes!")
#         else:
#             print(f"No winner found for President")
            
#         if winner2:
#             print(f"The winner for General Secretary is {winner2[0]} with {winner2[1]} total votes!")
#         else:
#             print(f"No winner found for General Secretary")
            

# elect = sqi_Election()
# elect.menu()
# # elect.Elections("president", "gen_sec")
# # elect.calculateWinner()

# conn.close()




# # This codes handles the voter registration, casting votes for both President and General Secretary positions, and calculates and displays the winners for both positions.
# # The program will run as follows:
# # It will start by asking the user's department to initiate the election process and register.
# # It will allow registered voters to cast their votes based on their departments and candidates of choice.
# # After all votes are cast, it will calculate and display the winners for both the President and General Secretary positions.
