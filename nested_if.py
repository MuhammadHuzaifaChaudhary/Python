# int age = 25;
# bool hasLicense = true;
# bool hasID = true;

# if (age >= 18) {
#     cout << "Age check passed" << endl;
    
#     if (hasLicense) {
#         cout << "Has license" << endl;
        
#         if (hasID) {
#             cout << "Has ID - Can drive!" << endl;
#         } else {
#             cout << "Needs ID" << endl;
#         }
#     } else {
#         cout << "Needs license" << endl;
#     }
# } else {
#     cout << "Too young to drive" << endl;
# }

# in python 


age = 25
has_license = True
has_id = True

if (age >= 18):                      # Level 1
    print("Age check passed")      # Level 1
    
    if (has_license):                # Level 2
        print("Has license")       # Level 2

        if (has_id):                 # Level 3
            print("Has ID - Can drive!")  # Level 3
        else:                      # Level 3
            print("Needs ID")      # Level 3
    else:                          # Level 2
        print("Needs license")     # Level 2
else:                              # Level 1
    print("Too young to drive")    # Level 1





# c++ 
#     #include <iostream>
# #include <string>
# using namespace std;

# int main() {
#     string username, password;
#     bool accountLocked = false;
#     int loginAttempts = 0;
    
#     cout << "Enter username: ";
#     cin >> username;
    
#     if (username == "admin") {
#         cout << "Username found" << endl;
        
#         cout << "Enter password: ";
#         cin >> password;
        
#         if (accountLocked) {
#             cout << "Account is locked" << endl;
#         } else {
#             if (password == "admin123") {
#                 cout << "Login successful!" << endl;
                
#                 if (loginAttempts > 3) {
#                     cout << "Warning: Multiple failed attempts" << endl;
#                 }
#             } else {
#                 cout << "Incorrect password" << endl;
#                 loginAttempts++;
                
#                 if (loginAttempts >= 5) {
#                     cout << "Account locked due to too many attempts" << endl;
#                     accountLocked = true;
#                 }
#             }
#         }
#     } else {
#         cout << "Username not found" << endl;
#     }
    
#     return 0;
# }

# in python

username = input("Enter username: ")
password = input("Enter password: ")
account_locked = False
login_attempts = 0

if username == "admin":                    # Level 1
    print("Username found")                # Level 1
    
    if account_locked:                     # Level 2
        print("Account is locked")         # Level 2
    else:                                  # Level 2
        if password == "admin123":         # Level 3
            print("Login successful!")     # Level 3
            
            if login_attempts > 3:         # Level 4
                print("Warning: Multiple failed attempts")  # Level 4
        else:                              # Level 3
            print("Incorrect password")    # Level 3
            login_attempts += 1             # Level 3
            
            if login_attempts >= 5:        # Level 4
                print("Account locked due to too many attempts")  # Level 4
                account_locked = True      # Level 4
else:                                      # Level 1
    print("Username not found")            # Level 1