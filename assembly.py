









import data
import main

print("""
 
██╗   ██╗██╗████████╗
██║   ██║██║╚══████╔╝
██║   ██║██║   ██║   
╚██╗ ██╔╝██║   ██║   
 ╚████╔╝ ██║   ██║   
  ╚═══╝  ╚═╝   ╚═╝   
""")     # Yes this is ai generated logo for fun only




#   Getting the user login 
print(":::::::::PDF SIGNATURE MECH. MGISOFTLTD.:::::::::::::::::")
print("............Aaapka Swagat Hai Janab..................")

users = data.Login_data
username = input("PLease Enter Username (case sensitive):")
if username in users:
    password = int(input("Hnn Bhai Password kya hai apna?: "))
    if password == users[username]:
        print("Welcome, System Ready")
        

        if main.runmode() == 1:
            print("<<<Initialising Signature Protocol>>>")
            main.signer(username)
        else:
            
            print("<<<Initialising Verification Protocol>>>")
            
            main.verifier()

    else:
        print("password bhul gye kya ?")


else:
    print("Aap galat jagah aagye hain Sirji")








