
while True:
    name = input("Input your Fullname: ").upper()
    age = int(input("Input your Age: "))

    while True:    
        gender = input("Input your Gender (male/female): ").capitalize()

        if gender == 'Male':
            break
        elif gender == 'Female':
            break
        else:
            print("Choose netween 'Male' or 'Female' only.")
            continue
        
    while True:
        contact_number = input("Input your contact number: ")

        if len(contact_number) != 11:
            print("Input a valid contact number.")
            continue
        else:
            break
    
    city = input("Input your city: ")

    with open('file_informations.txt', 'a') as file_infos:
        file_infos.write(f"\n{name}\nAge: {age}\nGender: {gender}\nContact Number: {contact_number}\nCity: {city}\n")

    print("------------------------\n")
    print("*Information added to text file*")
    print(f"\nName: {name}\nAge: {age}\nGender: {gender}\nContact Number: {contact_number}\nCity: {city}\n")
    print("------------------------")
    
    while True:
        add_more = input("Add more? (y/n): ")

        if add_more == 'y':
            break
        elif add_more == 'n':
            print("\nGood Bye!")
            break
        else:
            print("***Invalid Input***")

    if add_more == 'n':
        break
