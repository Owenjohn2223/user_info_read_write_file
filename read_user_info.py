
with open("file_informations.txt", "r") as file_infos:
    file_lines = file_infos.readlines()

search_info = input("Input a name to search: ").strip().upper()

found = False
store_info = []

for line in file_lines:
    line = line.strip() 
    if line == "":
        if any(search_info in item.upper() for item in store_info):
            found = True
            print("\n".join(store_info))  
        store_info = []
    else:
        store_info.append(line)  
        
if store_info and any(search_info in item.upper() for item in store_info):
    found = True
    print("\n".join(store_info))

if not found:
    print(f"No result found for '{search_info}'")        


