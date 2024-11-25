
while True:
    name = input("Input your Fullname: ")
    age = int(input("Input your Age: "))
    gender = input("Input your Gender: ")
    
    while True:
        contact_number = input("Input your contact number: ")

        if len(contact_number) != 11:
            print("Input a valid contact number.")
            continue
        else:
            break
    
    city = input("Input your city: ")

    print("------------------------")
    print(f"\nName: {name}\nAge: {age}\nGender: {gender}\nContact Number: {contact_number}\nCity: {city}\n")
    print("------------------------")

