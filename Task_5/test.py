store = []

def ViewContact(name, phone):
    output = []

    for index, entry in enumerate(store, 1):
        output.append(f"{index}. {entry[name]} - {entry[phone]}")

    result = " ".join(output)

    print(result)


def SearchContact(name):
    for li in store:
        if li["name"] == name:
            print(f"{li["name"]} - {li["phone"]}")
            return
    print("Contact Not Found!!!")

store.append({"name": "gideon",
              "phone": "07031170092",
              "email": "caro@gmail.com",
              "address": "opolo"})

store.append({"name": "caroline",
              "phone": "08037063820",
              "email": "edogh@gmail.com",
              "address": "biogbolo"})

# ViewContact("name", "phone")
SearchContact("gideon")
