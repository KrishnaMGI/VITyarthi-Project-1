from datetime import datetime
import os
import fitz
import data


def signer(username):
    dt = datetime.now().strftime("%Y%m%d%H%M%S") # date and time in numeric string form 
    
    session_id = (f"{dt}{username}")             # generating session id
    
    f = open("keys.txt", "a")
    f.write(session_id + "\n")
    f.close()          # inserting session id in main data base

    print(r"Test this for testing: test pdfs/Test 3.pdf")
    pdf = input("Please Enter Pdf Path: ")       # getting pdf path
    
    if os.path.exists(pdf):                      # checking path and all that things
        print("Proceeding")
    else:
        print("File Not Found Bhai!")
    
    sign = data.user_sign_path[username].strip()        # importing signature image/stamping image from data base
    
    print("✍️ Mass signing all pages instantly...")

    
    rect = fitz.Rect(480, 730, 580, 780)        #Coordinates of img stamp paste
    
    doc = fitz.open(pdf)
    
    for page in doc:
    
        page.insert_image(rect, filename=sign)     # performing stamping in loop on each page one by one

    # ab apan secure key daalte hain
    metadata = doc.metadata                        # injecting secure key in pdf roots for future verification
    metadata["keywords"] = session_id  
    doc.set_metadata(metadata)

    output_path = f"output/{os.path.basename(pdf)}"         # saving signed pdf for user
    doc.save(output_path)
    doc.close()

    print(f"Success! Signed file dropped at: '{output_path}'")


def runmode():
    print("Mode Numbers........................\n1 = Signing Mode\n2 = Verification Mode")
    rm = int(input("Input Mode Number: "))
    if rm == 1:
        return 1 # call signer()
    if rm == 2:
        return 2 #call verifier()


def verifier():
    print(r"Use This for testing:output\Test 2.pdf")
    pdf = input("Please Enter Pdf Path: ")

    if not os.path.exists(pdf):
        print("PDF not found")
        return

    doc = fitz.open(pdf)
    extracted_key = doc.metadata.get("keywords")
    doc.close()


    if os.path.exists("keys.txt"):
        f = open("keys.txt", "r")
        all_keys = f.read()
        f.close()


    if extracted_key == "":
        print("Verification Failed!!!!!")
    elif extracted_key in all_keys:
        print("Verified Pdf ")
        print(f"Signed By: {extracted_key[14:]}")
        print(f"Date of Signing: {extracted_key[6:8]}/{extracted_key[4:6]}/{extracted_key[0:4]}")




# Core logic and structure, designed and implemented by KRISHNA AGRAWAL 26BCE10210
#  whts written below is just for good vibes :-[
# +-----------------------------------------------------------------+

# |  M G I  S O F T  L T D .   S E C U R I T Y   D A S H B O A R D  |
# |  [ Build Version: 2026.1.0-PRO ]                                |
# |                                                                 |
# |  Copyright (c) 2026 MGISOFTLTD. All commercial rights reserved. |
# |  Unauthorized duplication, spoofing, or tampering is punishable |
# |  under system audit policies.                                   |
# +-----------------------------------------------------------------+



