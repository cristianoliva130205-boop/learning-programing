import os

client_ident = []
client_fullname = []
client_address = []
client_mobile = []
client_email = []
cliente_gender = []
client_age = []

product_code = []
product_name = []
product_guantity = []
product_unit_val = []

def mainMenu():
    os. system('clear')
    print("::: market main menu :::")
    print(""
        "[1]. register client \n"\ 
        "[2]. resgister product \n"\ 
        "[3]. list client \n"\ 
        "[4]. list product \n"\ 
        "[5]. search client by ident \n"\ 
        "[6]. search product by code \n"\ 
        "[7]. uptade client \n"\
        "[8]. uptade product \n"\ 
        "[9]. delate client \n"\ 
        "[10]. delate product \n"\ 
        "[11]. exit \n"\ 
        "::: press any option: ")


# main
menu_status = True
while menu_status:
    mainMenu()
    opt = input()
    if opt == '11':
        print('bye, bye')
        break
    
