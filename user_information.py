
while True:
    name = input("Input your Fullname: ")
    age = int(input("Input your Age: "))

    while True:    
        gender = input("Input your Gender (male/female): ")

        if gender == 'male':
            break
        elif gender == 'female':
            break
        else:
            print("Choose netween 'male' or 'female' only.")
            continue
        
    while True:
        contact_number = input("Input your contact number: ")

        if len(contact_number) != 11:
            print("Input a valid contact number.")
            continue
        else:
            break
    
    city = input("Input your city: ")

    with open('user_informations.txt', 'a') as file_infos:
        file_infos.write(f"{name}\nAge: {age}\nGender: {gender}\nContact Number: {contact_number}\nCity: {city}\n")

    print("------------------------")
    print(f"\nName: {name}\nAge: {age}\nGender: {gender}\nContact Number: {contact_number}\nCity: {city}\n")
    print("------------------------")

