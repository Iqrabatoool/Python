import json
from prettytable import PrettyTable
from cryptography.fernet import Fernet

print("Welcome To Password Saving Application")
print("Press 1 to add data")
print("Press 2 to delete data")
print("Press 3 to update data")
print("Press 4 to display all passwords")
print("Press 5 to display all decrypted passwords")
check = int(input("Press your desired key: "))
existing_data = {}
loop = 1

with open("store.json", 'r') as f:
    existing_data = json.load(f)

# Check if encryption has been done
if not existing_data.get("encryption_done", False):
    with open("key.txt", "rb") as key_file:
        key = key_file.read()
    fkey = Fernet(key)
    passwords = existing_data["data"]
    # Encrypt existing passwords
    for i, entry in enumerate(passwords, start=1):
        pwd_pass = entry.get("Password", "")
        # Check if the password is already encrypted
        if not pwd_pass.startswith("gAAAAA"):
            pwd_bytes = bytes(pwd_pass, 'utf-8')
            encrypted_password = fkey.encrypt(pwd_bytes)
            entry["Password"] = encrypted_password.decode('utf-8')
            print(f"Password {i} - Encrypted: {entry['Password']}")

    existing_data["encryption_done"] = True

    # Save the updated data
    with open("store.json", "w") as f:
        json.dump(existing_data, f, indent=4)


while loop ==1:

    if check == 1:
        email =input("Enter your email : ")
        app_name = input("Enter name of app ")
        password = input("Enter your Password : ")
        y = {"Email":email,"Password":password,"App_name":app_name}
        with open('store.json','r+') as f:
            existing_data = json.load(f)
            existing_data["data"].append(y)
            f.seek(0)
            existing_data["encryption_done"] = False
            json.dump(existing_data,f,indent=4)
            
    
    elif check == 2:
        mail = input("Enter the mail you want to delete: ")
        with open("store.json", 'r') as f:
            existing_data = json.load(f)
        filtered_data = [entry for entry in existing_data["data"] if entry["Email"] != mail]
        existing_data["data"] = filtered_data
        with open("store.json", 'w') as f:
            json.dump(existing_data, f, indent=4)

    elif check == 3:
        up_date = input("Enter the mail you want to update: ")
        with open("store.json", 'r') as f:
            existing_data = json.load(f)
        for entry in existing_data["data"]:
            if entry["Email"] == up_date:
                email = input("Enter your email: ")
                app_name = input("Enter name of app: ")
                password = input("Enter your Password: ")
                entry["Email"] = email
                entry["Password"] = password
                entry["App_name"] = app_name
        with open("store.json", 'w') as f:
            existing_data["encryption_done"] = False
            json.dump(existing_data, f, indent=4)
                


    elif check ==4:
        with open("store.json",'r') as f:
            data_to_display = json.load(f)["data"]
        table = PrettyTable()
        table.field_names = ["Email","Password","App Names"]
        for i in data_to_display:
            table.add_row([i["Email"],i["Password"],i["App_name"]])
        print(table)

    elif check == 5:
        pin = 1234
        entered_pin = int(input("Enter your Pin: "))
        
        if entered_pin == pin:
            decrypted_table = PrettyTable()
            decrypted_table.field_names = ["Email", "Decrypted Password", "App Names"]
            with open("key.txt",'rb') as f:
                key = f.read()
            
            fkey = Fernet(key)
            with open("store.json", 'r') as f:
                existing_data = json.load(f)["data"]
                for i in existing_data:
                    dpass = i["Password"]
                    bpass = bytes(dpass,'utf-8')
                    dpassword = fkey.decrypt(bpass).decode()

                    decrypted_table.add_row([i["Email"], dpassword, i["App_name"]])

            print(decrypted_table)
        else:
            print("Incorrect Pin!")

    ##Again for new values
    with open("store.json", 'r') as f:
        existing_data = json.load(f)

    # Check if encryption has been done
    if not existing_data.get("encryption_done", False):
        with open("key.txt", "rb") as key_file:
            key = key_file.read()
        fkey = Fernet(key)
        passwords = existing_data["data"]
        # Encrypt existing passwords
        for i, entry in enumerate(passwords, start=1):
            pwd_pass = entry.get("Password", "")
            # Check if the password is already encrypted
            if not pwd_pass.startswith("gAAAAA"):
                pwd_bytes = bytes(pwd_pass, 'utf-8')
                encrypted_password = fkey.encrypt(pwd_bytes)
                entry["Password"] = encrypted_password.decode('utf-8')
                print(f"Password {i} - Encrypted: {entry['Password']}")

        existing_data["encryption_done"] = True

        # Save the updated data
        with open("store.json", "w") as f:
            json.dump(existing_data, f, indent=4)

    loop = int(input("Do you want to do something else (Press 1) or quit (Press any button)"))
    if(loop ==1):
        print("Welcome To Password Saving Application")
        print("Press 1 to add data")
        print("Press 2 to delete data")
        print("Press 3 to update data")
        print("Press 4 to display all passwords")
        print("Press 5 to display all decrypted passwords")
        check = int(input("Press your desired key: "))
    else:
        print("Thanks alot for using our app")
    



