#This Is My First Complete Python Program (on my own)
#100DaysOfCode CodeWithHarry Exercise 1
#This Is Made By Adnan Abdin on 08-11-2023

print("This Is A Python Calculator :) !!!!\n")

a = input("Enter Your Name : ")

print("Welcome "+ a+ ","+ " I Am Very Glad That You Used My Caculator." )

instructions = ("""\nBefore You Proceed These Are The Instructions To Use The Calculator :\n
1. When I Ask Your First Number Then Enter Your First Number.
2. Then When I Ask You For Second Number Enter The Second Number.
3. At Last, When I Ask You For What Operation You Want To Do Enter Your Operation Eg: +,-,*,/""")

print(instructions)

instructions2 = """1. When I Ask Your First Number Then Enter Your First Number.
2. Then When I Ask You For Second Number Enter The Second Number.
3. At Last, When I Ask You For What Operation You Want To Do Enter Your Operation Eg: +,-,*,/\n"""

b = input("\nDo You Want To Proceed Now (Yes or No):\n")

if b == "Yes" or "yes":
    print("\nLets Go,")
    c = int(input("Enter Your First Number: "))
    d = int(input("Enter Your Second Number: "))
    e = input("What Operation Do You Want To Do: ")

if e == "+":
    print(c+d)

if e == "-":
    print(c-d)

if e == "*":
    print(c*d)  

if e == "/":
    print(c//d)          
