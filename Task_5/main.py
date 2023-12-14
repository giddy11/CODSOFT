from art import logo, options, added

contact_list_store = []
open_List = True

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
            output.append(f"{index}. {entry["name"]} - {entry["phone"]}")

        result = "\n".join(output)

        print(result)
    

def AddContact():
    name = input("Enter name: ")
    phone_no = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    AddContactToList(name, phone_no, email, address)

# def SearchContact(name):
#     for contact in contact_list_store:
#         if contact["name"] == name:
#             print(f"{contact["name"]} - {contact["phone"]}")
#             return
#     print("Contact Not Found!!!")

def SearchContact(name):
    global contact_list_store
    for index, contact in enumerate(contact_list_store):
        if contact["name"] == name:
            print(f"Here is your contact: \n{contact_list_store[index]["name"]} - {contact_list_store[index]["phone"]}")
            return index
    print("Contact Not Found!!!")
    return -1

# def UpdateContact()
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
    elif choice == 5:
        DeleteContact(input("What is the name of the contact you wish to delete?...").lower())
    elif choice == 6:
        open_List = False

while open_List:
    OpenContactList()