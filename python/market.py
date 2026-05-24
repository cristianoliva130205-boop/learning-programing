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
    
if is_positive_number(text):
    """Check that a text is a positive number (can have decimals)."""
    try:
        value = float(text)
        return value > 0
    except ValueError:
        return False
 
 
# ============================================================
#                     CUSTOMER FUNCTIONS
# ============================================================
 
def id_already_exists(id_number):
    """Check if a customer ID is already registered."""
    for customer in customers:
        if customer["id"] == id_number:
            return True
    return False
 
 
def register_customer():
    separator()
    print("          REGISTER NEW CUSTOMER")
    separator()
 
    # --- ID Number ---
    while True:
        id_number = input("ID Number (digits only): ").strip()
        if not is_only_numbers(id_number):
            print("  ! ID must contain digits only. Try again.")
        elif id_already_exists(id_number):
            print("  ! This ID is already registered. Try again.")
        else:
            break
 
    # --- Full Name ---
    while True:
        full_name = input("Full Name: ").strip()
        if not is_only_letters(full_name):
            print("  ! Name must contain letters only. Try again.")
        elif len(full_name) == 0:
            print("  ! Name cannot be empty. Try again.")
        else:
            break
 
    # --- Address ---
    while True:
        address = input("Address: ").strip()
        if len(address) == 0:
            print("  ! Address cannot be empty. Try again.")
        else:
            break
 
    # --- Phone ---
    while True:
        phone = input("Phone (digits only): ").strip()
        if not is_only_numbers(phone):
            print("  ! Phone must contain digits only. Try again.")
        else:
            break
 
    # --- Email ---
    while True:
        email = input("E-mail: ").strip()
        if not is_valid_email(email):
            print("  ! Invalid e-mail. Must include @ and a domain. Try again.")
        else:
            break
 
    # --- Gender ---
    while True:
        gender = input("Gender (Male / Female / Other): ").strip().capitalize()
        if gender not in ["Male", "Female", "Other"]:
            print("  ! Please enter: Male, Female, or Other.")
        else:
            break
 
    # --- Age ---
    while True:
        age = input("Age (digits only): ").strip()
        if not is_only_numbers(age):
            print("  ! Age must be a number. Try again.")
        elif int(age) <= 0 or int(age) > 120:
            print("  ! Please enter a realistic age (1-120). Try again.")
        else:
            break
 
    # --- Save customer ---
    new_customer = {
        "id":       id_number,
        "name":     full_name,
        "address":  address,
        "phone":    phone,
        "email":    email,
        "gender":   gender,
        "age":      age
    }
    customers.append(new_customer)
    print("\n  Customer registered successfully!")
    pause()
 
 
def list_customers():
    separator()
    print("              LIST OF CUSTOMERS")
    separator()
 
    if len(customers) == 0:
        print("  No customers registered yet.")
    else:
        for i, c in enumerate(customers, start=1):
            print(f"\n  Customer #{i}")
            print(f"    ID:      {c['id']}")
            print(f"    Name:    {c['name']}")
            print(f"    Address: {c['address']}")
            print(f"    Phone:   {c['phone']}")
            print(f"    E-mail:  {c['email']}")
            print(f"    Gender:  {c['gender']}")
            print(f"    Age:     {c['age']}")
            print("  " + "-" * 40)
    pause()
 
 
def find_customer_by_id(id_number):
    """Return the customer dict that matches the ID, or None."""
    for customer in customers:
        if customer["id"] == id_number:
            return customer
    return None
 
 
def search_customer():
    separator()
    print("            SEARCH CUSTOMER")
    separator()
 
    id_number = input("Enter the customer ID to search: ").strip()
    customer = find_customer_by_id(id_number)
 
    if customer is None:
        print("  ! No customer found with that ID.")
    else:
        print(f"\n  ID:      {customer['id']}")
        print(f"  Name:    {customer['name']}")
        print(f"  Address: {customer['address']}")
        print(f"  Phone:   {customer['phone']}")
        print(f"  E-mail:  {customer['email']}")
        print(f"  Gender:  {customer['gender']}")
        print(f"  Age:     {customer['age']}")
    pause()
 
 
def update_customer():
    separator()
    print("           UPDATE CUSTOMER")
    separator()
 
    id_number = input("Enter the customer ID to update: ").strip()
    customer = find_customer_by_id(id_number)
 
    if customer is None:
        print("  ! No customer found with that ID.")
        pause()
        return
 
    print(f"\n  Editing customer: {customer['name']}")
    print("  (Press ENTER to keep the current value)\n")
 
    # Full Name
    new_name = input(f"  Full Name [{customer['name']}]: ").strip()
    if new_name != "":
        if not is_only_letters(new_name):
            print("  ! Invalid name. Keeping current value.")
        else:
            customer["name"] = new_name
 
    # Address
    new_address = input(f"  Address [{customer['address']}]: ").strip()
    if new_address != "":
        customer["address"] = new_address
 
    # Phone
    new_phone = input(f"  Phone [{customer['phone']}]: ").strip()
    if new_phone != "":
        if not is_only_numbers(new_phone):
            print("  ! Invalid phone. Keeping current value.")
        else:
            customer["phone"] = new_phone
 
    # Email
    new_email = input(f"  E-mail [{customer['email']}]: ").strip()
    if new_email != "":
        if not is_valid_email(new_email):
            print("  ! Invalid e-mail. Keeping current value.")
        else:
            customer["email"] = new_email
 
    # Gender
    new_gender = input(f"  Gender [{customer['gender']}] (Male/Female/Other): ").strip().capitalize()
    if new_gender != "":
        if new_gender not in ["Male", "Female", "Other"]:
            print("  ! Invalid gender. Keeping current value.")
        else:
            customer["gender"] = new_gender
 
    # Age
    new_age = input(f"  Age [{customer['age']}]: ").strip()
    if new_age != "":
        if not is_only_numbers(new_age) or int(new_age) <= 0 or int(new_age) > 120:
            print("  ! Invalid age. Keeping current value.")
        else:
            customer["age"] = new_age
 
    print("\n  Customer updated successfully!")
    pause()
 
 
def delete_customer():
    separator()
    print("           DELETE CUSTOMER")
    separator()
 
    id_number = input("Enter the customer ID to delete: ").strip()
    customer = find_customer_by_id(id_number)
 
    if customer is None:
        print("  ! No customer found with that ID.")
        pause()
        return
 
    confirm = input(f"  Are you sure you want to delete '{customer['name']}'? (yes/no): ").strip().lower()
    if confirm == "yes":
        customers.remove(customer)
        print("  Customer deleted successfully!")
    else:
        print("  Deletion cancelled.")
    pause()
 
 

 
def code_already_exists(code):
    """Check if a product code is already registered."""
    for product in products:
        if product["code"] == code:
            return True
    return False
 
 
def register_product():
    separator()
    print("          REGISTER NEW PRODUCT")
    separator()
 
    
    while True:
        code = input("Product Code: ").strip()
        if len(code) == 0:
            print("  ! Code cannot be empty. Try again.")
        elif code_already_exists(code):
            print("  ! This code is already registered. Try again.")
        else:
            break
 
    # --- Name ---
    while True:
        name = input("Product Name: ").strip()
        if len(name) == 0:
            print("  ! Name cannot be empty. Try again.")
        else:
            break
 
    # --- Stock Quantity ---
    while True:
        quantity = input("Stock Quantity (whole number): ").strip()
        if not is_only_numbers(quantity):
            print("  ! Quantity must be a whole number. Try again.")
        elif int(quantity) < 0:
            print("  ! Quantity cannot be negative. Try again.")
        else:
            break
 
    # --- Unit Price ---
    while True:
        price = input("Unit Price (e.g. 9.99): ").strip()
        if not is_positive_number(price):
            print("  ! Price must be a positive number. Try again.")
        else:
            break
 
    # --- Save product ---
    new_product = {
        "code":     code,
        "name":     name,
        "quantity": quantity,
        "price":    price
    }
    products.append(new_product)
    print("\n  Product registered successfully!")
    pause()
 
 
def list_products():
    separator()
    print("              LIST OF PRODUCTS")
    separator()
 
    if len(products) == 0:
        print("  No products registered yet.")
    else:
        for i, p in enumerate(products, start=1):
            print(f"\n  Product #{i}")
            print(f"    Code:     {p['code']}")
            print(f"    Name:     {p['name']}")
            print(f"    Stock:    {p['quantity']} units")
            print(f"    Price:    $ {p['price']}")
            print("  " + "-" * 40)
    pause()
 
 
def find_product_by_code(code):
    """Return the product dict that matches the code, or None."""
    for product in products:
        if product["code"] == code:
            return product
    return None
 
 
def search_product():
    separator()
    print("            SEARCH PRODUCT")
    separator()
 
    code = input("Enter the product code to search: ").strip()
    product = find_product_by_code(code)
 
    if product is None:
        print("  ! No product found with that code.")
    else:
        print(f"\n  Code:     {product['code']}")
        print(f"  Name:     {product['name']}")
        print(f"  Stock:    {product['quantity']} units")
        print(f"  Price:    $ {product['price']}")
    pause()
 
 
def update_product():
    separator()
    print("           UPDATE PRODUCT")
    separator()
 
    code = input("Enter the product code to update: ").strip()
    product = find_product_by_code(code)
 
    if product is None:
        print("  ! No product found with that code.")
        pause()
        return
 
    print(f"\n  Editing product: {product['name']}")
    print("  (Press ENTER to keep the current value)\n")
 
    # Name
    new_name = input(f"  Product Name [{product['name']}]: ").strip()
    if new_name != "":
        product["name"] = new_name
 
    # Quantity
    new_qty = input(f"  Stock Quantity [{product['quantity']}]: ").strip()
    if new_qty != "":
        if not is_only_numbers(new_qty):
            print("  ! Invalid quantity. Keeping current value.")
        else:
            product["quantity"] = new_qty
 
    # Price
    new_price = input(f"  Unit Price [{product['price']}]: ").strip()
    if new_price != "":
        if not is_positive_number(new_price):
            print("  ! Invalid price. Keeping current value.")
        else:
            product["price"] = new_price
 
    print("\n  Product updated successfully!")
    pause()
 
 
def delete_product():
    separator()
    print("           DELETE PRODUCT")
    separator()
 
    code = input("Enter the product code to delete: ").strip()
    product = find_product_by_code(code)
 
    if product is None:
        print("  ! No product found with that code.")
        pause()
        return
 
    confirm = input(f"  Are you sure you want to delete '{product['name']}'? (yes/no): ").strip().lower()
    if confirm == "yes":
        products.remove(product)
        print("  Product deleted successfully!")
    else:
        print("  Deletion cancelled.")
    pause()
 
 
# ============================================================
#                         MAIN MENU
# ============================================================
 
def show_menu():
    separator()
    print("       CUSTOMER & PRODUCT MANAGEMENT SYSTEM")
    separator()
    print("  --- CUSTOMERS ---")
    print("  1. Register Customer")
    print("  2. List Customers")
    print("  3. Search Customer")
    print("  4. Update Customer")
    print("  5. Delete Customer")
    print()
    print("  --- PRODUCTS ---")
    print("  6. Register Product")
    print("  7. List Products")
    print("  8. Search Product")
    print("  9. Update Product")
    print("  10. Delete Product")
    print()
    print("  0. Exit")
    separator()
 
 
def main():
    print("\n  Welcome to the Management System!")
 
    while True:
        show_menu()
        option = input("  Choose an option: ").strip()
 
        if option == "1":
            register_customer()
        elif option == "2":
            list_customers()
        elif option == "3":
            search_customer()
        elif option == "4":
            update_customer()
        elif option == "5":
            delete_customer()
        elif option == "6":
            register_product()
        elif option == "7":
            list_products()
        elif option == "8":
            search_product()
        elif option == "9":
            update_product()
        elif option == "10":
            delete_product()
        elif option == "0":
            print("\n  Goodbye! See you next time.\n")
            break
        else:
            print("\n  ! Invalid option. Please choose a number from the menu.")
            pause()
 
 
# --- Run the program ---
main()
 