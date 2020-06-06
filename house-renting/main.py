#Welcome to my House Renting System
import random
import sys

def main_menu():
    print("     ------Main Menu------\n")
    print("Welcome to NyumbaRahisi Listing Platform.\nWe offer convenient and reliable housing services across Kenya,"
          "tens of thousands of single rooms, apartments, houses and villas on offer.")

    print("""     
                  1. Create an Account With Us
                  2. Rate a Previous Stay With Us
                  3. Exit Program
               """)

    userChoice = input("Choose from the above options: ")

    if userChoice == '1':
        print("Welcome to the NyumbaRahisi Account Creation Screen\nIt is a pleasure to have you join us")
        userName = input("Please enter your full name: ").capitalize()
        userEmail = input("Please input your email address: ")
        userAge = input("Please Input your Age. Note you need to 18 and over to use this service. ")


        x = random.randint(0, 100)
        print("\nThank you for creating an account with NyumbaRahisi " + userName + ". \nYour Account number is " + str(x))






print(main_menu())
