from art import logo, options, added

contact_list_store = []
open_List = True
change_details_choice = [1,2,3,4]


def AddContactToList(name, phone_no, email, address):
    contact_list_store.append(
    {
        "name": name,
        "phone": phone_no,
        "email": email,
        "address": address,    
    })
    print(added)

def ViewContact():
    global contact_list_store
    if not contact_list_store:
            print("No Contact has been saved yet")
    else:
        output = []

        for index, entry in enumerate(contact_list_store, 1):
            output.append(f"{index}. {entry["name"]} - {entry["phone"]} - {entry["email"]} - {entry["address"]}")

        result = "\n".join(output)

        print(result)
    
def ChangeDetails(index_name, key):
    global contact_list_store

    contact_list_store[index_name][key] = input(f"Update your {key}: ")
    print(added)


def CheckChoice(search_name, choice):
    # this commented lines is for when a user wants to update all details at once
    # myDic = {
    #     1:ChangeDetails(search_name, "name"),
    #     2:ChangeDetails(search_name ,"phone"),
    #     3:ChangeDetails(search_name, "email"),
    #     4:ChangeDetails(search_name, "address"),
    # }

    # for x in myDic:
    #     if choice == x:
    #         return myDic[x]
        
    # return 0


    if choice == 1:
        ChangeDetails(search_name, "name")
    elif choice == 2:
        ChangeDetails(search_name, "phone")
    elif choice == 3:
        ChangeDetails(search_name, "email")
    elif choice == 4:
        ChangeDetails(search_name, "address")
    else:
        print("Invalid!!! Please enter the serial number for the particular details you want to update")


def AddContact():
    name = input("Enter name: ")
    phone_no = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    AddContactToList(name, phone_no, email, address)

def SearchContact(name):
    global contact_list_store
    for index, contact in enumerate(contact_list_store):
        if contact["name"] == name:
            print(f"Here is your contact: \n{contact_list_store[index]["name"]} - {contact_list_store[index]["phone"]}")
            return index
    print("Contact Not Found!!!")
    return -1

def UpdateContact(name):
    search_name = SearchContact(name)
    if search_name != -1:
        choice = int(input("1. Update Name\n2. Update Phone Number\n3. Update Email\n4. Update Address... "))
        res = CheckChoice(search_name, choice)
        # if res == 0:
        #     print("Invalid")


def DeleteContact(name):
    global contact_list_store
    search_result = SearchContact(name)
    if search_result != -1:
        contact_list_store.pop(search_result)
        print(f"{name} has been deleted successfully")


def OpenContactList():
    global open_List
    print(logo)
    print(options)

    choice = int(input("Enter your choice (1 - 6): "))
    if choice == 1:
        AddContact()
    elif choice == 2:
        ViewContact()
    elif choice == 3:
        res = SearchContact(input("which contact are you searching for?...").lower())
    elif choice == 4:
        res = UpdateContact(input("Type the name of the contact you want to update?... ").lower())
    elif choice == 5:
        DeleteContact(input("What is the name of the contact you wish to delete?...").lower())
    elif choice == 6:
        open_List = False

while open_List:
    OpenContactList()