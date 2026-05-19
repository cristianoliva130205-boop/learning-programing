import os 


os.system('clear')
#inputs
n1 = float(input("enter first number: "))
n2 = float(input("enter second number:"))

# main menu 
def main_menu():
    print("#### main menu ####")
    print("[1]. addition") 
    print("[2]. substraction")
    print("[3]. multiplication")
    print("[4]. division")
    print("[5]. average")
    print("[6]. all operations")
   
main_menu()
opt =int(input("enter any option:"))

if (opt == 1):
    add = n1 + n2 
    print("addition is: (add)") 

if (opt == 2):
    subs = n1 / n2 
    print("division is: (subs)")   

if (opt == 3):
    milt = n1 + n2 
    print("multiplication is: (mult)")

if (opt == 4):
    div = n1 / n2 
    print("division is: (div)")

if (opt == 5):
    avg = (n1+n2)/2
    print("division is: (avg)")

 if (opt == 6):
    add = n1 + n2 
    subs = n1 - n2
    mult = n1 + n2 
    div = n1 / n2 
    avg = (n1 + n2) / 2 
    
    