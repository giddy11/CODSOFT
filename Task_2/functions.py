user_first_input = 0
user_second_input = 0
user_op_choice = None
res = 0

def add(user_first_input, user_second_input):
    return user_first_input + user_second_input

def sub(user_first_input, user_second_input):
    return user_first_input - user_second_input

def mul(user_first_input, user_second_input):
    return user_first_input * user_second_input

def div(user_first_input, user_second_input):
    return user_first_input / user_second_input


# def Calculate():
#     global user_first_input, user_second_input, user_op_choice

#     if user_op_choice == "+":
#         return user_first_input + user_second_input
#     elif user_op_choice == "-":
#         return user_first_input - user_second_input
#     elif user_op_choice == "*":
#         return user_first_input * user_second_input
#     elif user_op_choice == "/":
#         return user_first_input / user_second_input
#     else:
#         return 0
    
def Calculate():
    global user_first_input, user_second_input, user_op_choice
    operations = {
        "+": add(user_first_input, user_second_input),
        "-": sub(user_first_input, user_second_input),
        "*": mul(user_first_input, user_second_input),
        "/": div(user_first_input, user_second_input)
    }

    for x in operations:
        if user_op_choice == x:
            return operations[x]
        
    return 0
    
def Print_Result():
    global res, user_first_input, user_second_input
    if res == 0:
        res = user_first_input
    else:
        user_first_input = res
    
    res = Calculate()
    if res == 0:
        print("Invalid operator")
    else:
        print(f"{user_first_input}{user_op_choice}{user_second_input} = {res}")