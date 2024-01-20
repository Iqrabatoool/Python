"#
Password Saving Application
Welcome to the Password Saving Application! This command-line application allows you to securely manage and store your passwords. It prioritizes your security by encrypting sensitive information using the Fernet symmetric key encryption from the cryptography library.

Features
1. Add Data (Press 1):
Add a new entry with your email, app name, and password.
2. Delete Data (Press 2):
Delete an entry by providing the associated email.
3. Update Data (Press 3):
Update an entry by providing the associated email. You can update your email, app name, and password.
4. Display All Passwords (Press 4):
View all stored passwords in a table, including emails, encrypted passwords, and app names.
5. Display All Decrypted Passwords (Press 5):
View stored passwords with decryption (requires PIN authentication).
How Encryption Works
The application utilizes Fernet symmetric key encryption.
Passwords are encrypted before storage in the store.json file.
Existing passwords are encrypted during application startup if not already encrypted.
When adding or updating entries, the application ensures that passwords are encrypted.
Setup
Key Generation:

The application generates a key stored in the key.txt file for encryption.
Password Encryption:

Existing passwords are encrypted during application startup if not already encrypted.
Usage
Run the Application:

Execute the script to run the Password Saving Application.
Select Operation:

Choose an operation by entering the corresponding key (1 to 5).
Follow Prompts:

Follow prompts to perform the desired operation (add, delete, update, display, decrypt).
PIN Authentication:

Enter a PIN to decrypt passwords. Default PIN is 1234.
Continue or Quit:

Choose to continue using the application or quit.
Note
The application uses a PIN for additional security during the decryption process.
Remember your PIN to successfully decrypt passwords.
Thanks for using our Password Saving Application!" 
