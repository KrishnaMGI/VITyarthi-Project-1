# VITyarthi-Project-1
Course: Python Essentials  Deadline: Sep 30, 2026, 11:59 PM  Problem Statement: As part of the flipped course evaluation process you need to submit a project, You can choose Any Project From the Course Domain

## Pdf Verification and Signing System ##
usage: The project intents to mass sign the pdfs of terms and conditions or tender files and adding unique identity to them which can be further verified by using this programme itself.
The programme can serve as a trustworthy pdf verification system and exist as an unbiased independent entity which can be trusted by both the signer and the verifier.

## How it works ##
The programme uses multiple files which includes the data.py which conatains the usernames, passwords,  confidential signature images, and other additive items for future.

1.Authentication : The first thing programme does is to ask the user for his/her unique username and password and then matches the enteries with the dedicated database.py file if everything goes right the programme proceeds

2.Mode Selection: the programme then asks the user to choose what he wants to do 1. Put signature and stamp on lengthy 1200+ page pdf 2. verify the signed pdf for authenticity of the provided pdf.

3. Working: now if user opt for signing the signer function from main.py is called which extracts user data like his stamps and signs and paste them onto the pdf at specific legal coordinates (preffered bottom right corner). This is achieved by using the PyMuPdf library of python since pdfs are very comlicated to handle without using library, by using the Fitz's PyMuPdf library the project remained in its basic behaviour and also was saved from getting deflected to another pdf reader project.

The signer fn also puts a unique key into the pdfs metadata which is core element for verification since the signature images can be pasted by anyone but the confidential key builiding and injection process can be done by this programme only and where it is places also remains hidden until the sourcecode is hidden

The verifier fn simply searches for this unique key in pdf if the key is found on dedicated place the verification is completed.

To make the process more refined and avoid unneccesary addition of blank pdfs to our data base we used os fn path check process which just ends the programme if the path entered by the user is invalid.



# How to Run The Code

1. Find Assembly.py file in the repository
2. Run This file 
3. Enter The Username (Prefarablly: Taau)
4. Enter The pin/password (For Taau : 2707)
5. Mode selector menu will come in front. INPUT 1 for signing mode OR 2 for verification mode.
6. Enter the pdf path (use any of the pdf from test pdf; or simply copy paste the given example)
7. CRITICAL : please be cautious with the spaces in the path !!!!!!!!!
8. you will be provided with the desired output if everything goes well and good as expected.

# Aknowledgement
The programme contains certain things like usernames like Dr.Soni, VIT LOGO, some random words like MGISOFTLTD these are intentionally kept their for dedicated personnel who directly or indirectly affected and supported the development of this project.
Also this code contains mostly unexpected returns like (Password Bhul gye kya?) to prove this is not ai generated and I have invested my time and knowledge in this code.
Also i would like to confess that i have used AI tools and internet sources to learn the usage of PyMuPdf library and research on this concept but i haven't copy pasted any piece of code. 
I am also thankfull to the person testing this code and running this (or maybe trying to run this) code with atmost dedication and i am also grateful to him/her for ignoring unintentionall errors in this code.

